from datetime import datetime

from django.db import models
from django.forms import model_to_dict

from config.settings import MEDIA_URL, STATIC_URL
from core.erp.choices import gender_choices
from core.models import BaseModel

class Bussines(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre')
    rut = models.CharField(max_length=20, verbose_name='R.U.T / I.D')
    address = models.CharField(max_length=150, verbose_name='Direccion')
    phone = models.CharField(max_length=15, verbose_name='Telefono', null=True, blank=True)
    email = models.EmailField('Email', max_length=254)
    about = models.TextField('Acerca De Nosotros', max_length=2000, null=True, blank=True)
    descripcion = models.TextField('Descripcion', max_length=2000, null=True, blank=True)
    logo = models.ImageField(upload_to='logob/%Y/%m/%d', null=True, blank=True, verbose_name='logo')

    def __str__(self):
        return self.name

    def toJSON(self):
        item = model_to_dict(self)
        item['logo'] = self.get_image()
        return item

    def get_image(self):
        if self.logo:
            return '{}{}'.format(MEDIA_URL, self.logo)
        return '{}{}'.format(STATIC_URL, 'img/logog.png')


    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'
        ordering = ['id']


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre', unique=True)
    desc = models.CharField(max_length=500, null=True, blank=True, verbose_name='Descripción')

    def __str__(self):
        return self.name

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['id']


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre', unique=True)
    image = models.ImageField(upload_to='product/%Y/%m/%d', null=True, blank=True, verbose_name='Imagen')
    edad = models.IntegerField(verbose_name='Edad', default=22)
    date_joined = models.DateField(default=datetime.now)
    identificacion = models.CharField('Identificacion', max_length=12, null=True, blank=True)
    cirugias = models.CharField('Cirugias', max_length=200, null=True, blank=True)
    cirujano = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True,related_name='cirujano')
    cirujano2 = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Cirujano2',related_name='cirujano2',null=True,blank=True)
    inicioanestesia = models.TimeField('Inicio Anestesia', null=True, blank=True)
    iniciocirugia = models.TimeField('Inicio Cirugia', null=True, blank=True)
    duracion = models.CharField('Duracion Cirugia', max_length=10, null=True, blank=True)
    finalizacioncirugia = models.TimeField('Finalizacion Cirugia', null=True, blank=True)
    finalizacionanestesia = models.TimeField('Finalizacion Anestesia', null=True, blank=True)
    klein = models.CharField('Klein', max_length=6, null=True, blank=True)
    extrae = models.CharField('Extrae', max_length=6, null=True, blank=True)
    transferencia = models.CharField('Transferencia', max_length=6, null=True, blank=True)
    md = models.CharField('MD', max_length=200, null=True, blank=True)
    mi = models.CharField('MI', max_length=200, null=True, blank=True)
    colgajo = models.CharField('Colgajo D', max_length=6, null=True, blank=True)
    colgajo2 = models.CharField('Colgajo I', max_length=6, null=True, blank=True)
    observaciones = models.TextField('Observaciones', max_length=999, null=True, blank=True)

    def __str__(self):
        return self.name

    def toJSON(self):
        item = model_to_dict(self)
        if self.cirujano is not None:
            item['cirujano'] = self.cirujano.toJSON()
        if self.cirujano2 is not None:
            item['cirujano2'] = self.cirujano2.toJSON()
        item['date_joined'] = self.date_joined.strftime('%Y-%m-%d')
        item['image'] = self.get_image()
        return item

    def get_image(self):
        if self.image:
            return '{}{}'.format(MEDIA_URL, self.image)
        return '{}{}'.format(STATIC_URL, 'img/empty.png')

    class Meta:
        verbose_name = 'Paciente'
        verbose_name_plural = 'Pacientea'
        ordering = ['date_joined']


class Client(models.Model):
    names = models.CharField(max_length=150, verbose_name='Nombres')
    surnames = models.CharField(max_length=150, verbose_name='Apellidos')
    dni = models.CharField(max_length=10, unique=True, verbose_name='Dni')
    date_birthday = models.DateField(default=datetime.now, verbose_name='Fecha de nacimiento')
    address = models.CharField(max_length=150, null=True, blank=True, verbose_name='Dirección')
    gender = models.CharField(max_length=10, choices=gender_choices, default='male', verbose_name='Sexo')

    def __str__(self):
        return self.names

    def toJSON(self):
        item = model_to_dict(self)
        item['gender'] = {'id': self.gender, 'name': self.get_gender_display()}
        item['date_birthday'] = self.date_birthday.strftime('%Y-%m-%d')
        return item

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['id']


class Sale(models.Model):
    cli = models.ForeignKey(Client, on_delete=models.CASCADE)
    date_joined = models.DateField(default=datetime.now)
    subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    iva = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    total = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)

    def __str__(self):
        return self.cli.names

    def toJSON(self):
        item = model_to_dict(self)
        item['cli'] = self.cli.toJSON()
        item['subtotal'] = format(self.subtotal, '.2f')
        item['iva'] = format(self.iva, '.2f')
        item['total'] = format(self.total, '.2f')
        item['date_joined'] = self.date_joined.strftime('%Y-%m-%d')
        item['det'] = [i.toJSON() for i in self.detsale_set.all()]
        return item

    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'
        ordering = ['id']


class DetSale(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
    prod = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    cant = models.IntegerField(default=0)
    subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)

    def __str__(self):
        return self.prod.name

    def toJSON(self):
        item = model_to_dict(self, exclude=['sale'])
        item['prod'] = self.prod.toJSON()
        item['price'] = format(self.price, '.2f')
        item['subtotal'] = format(self.subtotal, '.2f')
        return item

    class Meta:
        verbose_name = 'Detalle de Venta'
        verbose_name_plural = 'Detalle de Ventas'
        ordering = ['id']
