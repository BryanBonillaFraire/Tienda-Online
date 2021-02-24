# Generated by Django 3.1.2 on 2020-10-22 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Domicilio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=10)),
                ('calle1', models.CharField(max_length=50)),
                ('calle2', models.CharField(max_length=50)),
                ('ciudad', models.CharField(max_length=50)),
                ('estado', models.CharField(max_length=50)),
                ('cp', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('marca', models.CharField(max_length=30)),
                ('modelo', models.CharField(max_length=30)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=6)),
                ('stock', models.IntegerField()),
                ('oferta', models.IntegerField(null=True)),
                ('imagen', models.ImageField(upload_to=None)),
            ],
        ),
    ]
