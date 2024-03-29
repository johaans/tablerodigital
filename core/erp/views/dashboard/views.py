from datetime import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum
from django.db.models.functions import Coalesce
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView

from core.erp.models import Product,Category,Procedimientos

from random import randint


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        request.user.get_group_session()
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'get_graph_sales_year_month':
                data = {
                    'name': 'Cantidad de Procedimientos',
                    'showInLegend': False,
                    'colorByPoint': True,
                    'data': self.get_graph_sales_year_month()
                }
            elif action == 'get_graph_sales_products_year_month':
                data = {
                    'name': 'Porcentaje Procedimientos',
                    'colorByPoint': True,
                    'data': self.get_graph_sales_products_year_month(),
                }
            elif action == 'get_graph_sales_products_year_month2':
                data = {
                    'name': 'Porcentaje Procedimientos',
                    'colorByPoint': True,
                    'data': self.get_graph_sales_products_year_month2(),
                }
            elif action == 'get_graph_procedimientos_year_month':
                data = {
                    'name': 'Porcentaje',
                    'colorByPoint': True,
                    'data': self.get_graph_procedimientos_year_month(),
                }

            elif action == 'get_graph_online':
                data = {'y': randint(1, 100)}
                print(data)
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_graph_sales_year_month(self):
        data = []
        try:
            year = datetime.now().year
            for m in range(1, 13):
                total = Product.objects.filter(date_joined__year=year, date_joined__month=m).count()
                data.append(int(total))
        except:
            pass
        return data

    def get_graph_sales_products_year_month(self):
        data = []
        year = datetime.now().year
        month = datetime.now().month
        try:
            for p in Category.objects.all():
                total = Product.objects.filter(date_joined__year=year,
                                               cirujano_id=p.id).count()
                if total > 0:
                    data.append({
                        'name': p.name,
                        'y': float(total)
                    })
        except:
            pass
        return data

    def get_graph_sales_products_year_month2(self):
        data = []
        year = datetime.now().year
        month = datetime.now().month
        try:
            for p in Category.objects.all():
                total = Product.objects.filter(date_joined__year=year,
                                               cirujano2_id=p.id).count()
                if total > 0:
                    data.append({
                        'name': p.name,
                        'y': float(total)
                    })
        except:
            pass
        return data

    def get_graph_procedimientos_year_month(self):
        data = []
        year = datetime.now().year
        month = datetime.now().month
        try:
            # a=Product.objects.all()
            # for p in a:
            #     total=5
            #     print(total)
            #     total = Product.objects.filter(date_joined__year=year,procedimientos_id=p.id).count()
                
                                               
            #     if total > 0:
            #         data.append({
            #             'name': p.name,
            #             'y': float(total)
            #         })
            for p in Procedimientos.objects.all():
                total = Product.objects.filter(date_joined__year=year,
                                               procedimientos__id=p.id).count()
                if total > 0:
                    print(p.name,total)
                    data.append({
                        'name': p.name,
                        'y': float(total)
                    })
        except:
            pass
        return data

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Inicio'
        context['panel'] = 'Panel de administrador'
        context['graph_sales_year_month'] = self.get_graph_sales_year_month()
        return context
