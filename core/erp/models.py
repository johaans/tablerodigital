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
        verbose_name = 'Medico'
        verbose_name_plural = 'Medicos'
        ordering = ['id']

class Procedimientos(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre', unique=True)
    desc = models.CharField(max_length=500, null=True, blank=True, verbose_name='Descripción')
    def __str__(self):
        return self.name

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = 'Cirugia'
        verbose_name_plural = 'Cirugias'
        ordering = ['id']

class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre', unique=True)
    image = models.ImageField(upload_to='product/%Y/%m/%d', null=True, blank=True, verbose_name='Imagen 1')
    image2 = models.ImageField(upload_to='product/%Y/%m/%d', null=True, blank=True, verbose_name='Imagen 2')
    image3 = models.ImageField(upload_to='product/%Y/%m/%d', null=True, blank=True, verbose_name='Imagen 3')
    image4 = models.ImageField(upload_to='product/%Y/%m/%d', null=True, blank=True, verbose_name='Imagen 4')
    edad = models.IntegerField(verbose_name='Edad', default=0)
    date_joined = models.DateField(default=datetime.now)
    identificacion = models.CharField('Identificacion', max_length=15, null=True, blank=True)
    cirugias = models.CharField('Cirugias', max_length=200, null=True, blank=True)
    cirujano = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True,related_name='cirujano')
    cirujano2 = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Cirujano2',related_name='cirujano2',null=True,blank=True)
    inicioanestesia = models.TimeField('Inicio Anestesia', null=True, blank=True)
    iniciocirugia = models.TimeField('Inicio Cirugia', null=True, blank=True)
    duracion = models.CharField('Duracion Cirugia', max_length=20, null=True, blank=True)
    finalizacioncirugia = models.TimeField('Finalizacion Cirugia', null=True, blank=True)
    finalizacionanestesia = models.TimeField('Finalizacion Anestesia', null=True, blank=True)
    klein = models.CharField('Klein', max_length=10, null=True, blank=True)
    extrae = models.CharField('Extrae', max_length=10, null=True, blank=True)
    transferencia = models.CharField('Transferencia', max_length=10, null=True, blank=True)
    md = models.CharField('MD', max_length=20, null=True, blank=True)
    mi = models.CharField('MI', max_length=20, null=True, blank=True)
    colgajo = models.CharField('Colgajo D', max_length=10, null=True, blank=True)
    colgajo2 = models.CharField('Colgajo I', max_length=10, null=True, blank=True)
    observaciones = models.TextField('Observaciones', max_length=999, null=True, blank=True)
    procedimientos=models.ManyToManyField(Procedimientos)

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
        item['image2'] = self.get_image2()
        item['image3'] = self.get_image3()
        item['image4'] = self.get_image4()
        item['procedimientos'] = [{'id': procedimientos.id, 'name': procedimientos.name} for procedimientos in self.procedimientos.all()]
        return item

    def get_image(self):
        if self.image:
            return '{}{}'.format(MEDIA_URL, self.image)
        return '{}{}'.format(STATIC_URL, 'img/empty.png')

    def get_image2(self):
        if self.image2:
            return '{}{}'.format(MEDIA_URL, self.image2)
        return '{}{}'.format(STATIC_URL, 'img/logog.png')

    def get_image3(self):
        if self.image3:
            return '{}{}'.format(MEDIA_URL, self.image3)
        return '{}{}'.format(STATIC_URL, 'img/logog.png')

    def get_image4(self):
        if self.image4:
            return '{}{}'.format(MEDIA_URL, self.image4)
        return '{}{}'.format(STATIC_URL, 'img/logog.png')

    class Meta:
        verbose_name = 'Paciente'
        verbose_name_plural = 'Pacientes'
        ordering = ['date_joined']



