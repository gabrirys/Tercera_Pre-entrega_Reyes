# Generated by Django 4.2.3 on 2023-07-25 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=128)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('telefono', models.CharField(blank=True, max_length=20)),
                ('mensaje', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Posteo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=128)),
                ('contenido', models.TextField(blank=True)),
                ('fecha_publicado', models.DateTimeField(auto_now_add=True)),
                ('autor', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=64)),
                ('apellido', models.CharField(max_length=64)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('nacimiento', models.DateField(null=True)),
                ('usuario', models.CharField(max_length=64)),
            ],
        ),
    ]