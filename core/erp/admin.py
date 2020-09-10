from django.contrib import admin
from core.erp.models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from django import forms

# Register your models here.

class Categoryresource(resources.ModelResource):
    class Meta:
        model = Category

class Categoryadmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('name', 'desc')
    list_filter = ['name',]
    search_fields = ('name',)
    resource_class=Categoryresource
admin.site.register(Category,Categoryadmin)

class Productresource(resources.ModelResource):
    class Meta:
        model = Product


class Productadmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('name', 'identificacion','cirujano','date_joined')
    list_filter = ['name','cirujano','date_joined','cirugias']
    search_fields = ('name','cirujano','cirugias','date_joined')
    resource_class=Productresource
admin.site.register(Product,Productadmin)


class Bussinesresource(resources.ModelResource):
    class Meta:
        model = Bussines

class Bussinesadmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('name', 'logo')
    list_filter = ['name',]
    search_fields = ('name',)
    resource_class=Bussines
admin.site.register(Bussines,Bussinesadmin)