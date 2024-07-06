# Generated by Django 4.2.3 on 2023-07-31 10:05

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_alter_donor_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='looking',
            name='dob',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='looking',
            name='name',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='looking',
            name='patient',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='looking',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None),
        ),
        migrations.AlterField(
            model_name='organ',
            name='dob',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='organ',
            name='name',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='organ',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None),
        ),
    ]
