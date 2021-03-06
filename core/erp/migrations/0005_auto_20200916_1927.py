# Generated by Django 3.0.4 on 2020-09-17 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0004_bussines'),
    ]

    operations = [
        migrations.CreateModel(
            name='Procedimientos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='Nombre')),
                ('desc', models.CharField(blank=True, max_length=500, null=True, verbose_name='Descripción')),
            ],
            options={
                'verbose_name': 'Cirugia',
                'verbose_name_plural': 'Cirugias',
                'ordering': ['id'],
            },
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['id'], 'verbose_name': 'Medico', 'verbose_name_plural': 'Medicos'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['date_joined'], 'verbose_name': 'Paciente', 'verbose_name_plural': 'Pacientes'},
        ),
        migrations.AddField(
            model_name='product',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='product/%Y/%m/%d', verbose_name='Imagen 2'),
        ),
        migrations.AddField(
            model_name='product',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to='product/%Y/%m/%d', verbose_name='Imagen 3'),
        ),
        migrations.AddField(
            model_name='product',
            name='image4',
            field=models.ImageField(blank=True, null=True, upload_to='product/%Y/%m/%d', verbose_name='Imagen 4'),
        ),
        migrations.AlterField(
            model_name='product',
            name='colgajo',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Colgajo D'),
        ),
        migrations.AlterField(
            model_name='product',
            name='colgajo2',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Colgajo I'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='product/%Y/%m/%d', verbose_name='Imagen 1'),
        ),
        migrations.AddField(
            model_name='product',
            name='procedimientos',
            field=models.ManyToManyField(to='erp.Procedimientos'),
        ),
    ]
