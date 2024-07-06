# Generated by Django 4.2.3 on 2023-07-28 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Donor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, unique=True)),
                ('email', models.CharField(max_length=80, unique=True)),
                ('phone', models.CharField(max_length=20)),
                ('dob', models.DateField(unique=True)),
                ('gender', models.CharField(max_length=40)),
                ('address', models.TextField(blank=True)),
                ('state', models.CharField(max_length=80)),
                ('city', models.CharField(max_length=80)),
                ('district', models.CharField(max_length=80)),
                ('med_history', models.TextField(blank=True)),
                ('blood', models.TextField(blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Looking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, unique=True)),
                ('patient', models.CharField(max_length=40, unique=True)),
                ('email', models.CharField(max_length=80, unique=True)),
                ('phone', models.CharField(max_length=20)),
                ('dob', models.DateField(unique=True)),
                ('address', models.TextField(blank=True)),
                ('state', models.CharField(max_length=80)),
                ('city', models.CharField(max_length=80)),
                ('district', models.CharField(max_length=80)),
                ('units', models.IntegerField(blank=True)),
                ('blood', models.TextField(blank=True)),
                ('require', models.CharField(max_length=80)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Organ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, unique=True)),
                ('email', models.CharField(max_length=80, unique=True)),
                ('phone', models.CharField(max_length=20)),
                ('dob', models.DateField(unique=True)),
                ('gender', models.CharField(max_length=40)),
                ('address', models.TextField(blank=True)),
                ('state', models.CharField(max_length=80)),
                ('city', models.CharField(max_length=80)),
                ('district', models.CharField(max_length=80)),
                ('donate', models.CharField(max_length=20)),
                ('donate_tissue', models.CharField(max_length=20)),
                ('proof', models.FileField(upload_to='organ_proofs/')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Questions',
        ),
    ]
