# Generated by Django 4.2.3 on 2023-07-28 10:29

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_donor_looking_organ_delete_questions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donor',
            name='blood',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AlterField(
            model_name='donor',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='donor',
            name='med_history',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='donor',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True),
        ),
        migrations.AlterField(
            model_name='looking',
            name='blood',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AlterField(
            model_name='looking',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='looking',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True),
        ),
        migrations.AlterField(
            model_name='organ',
            name='dob',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='organ',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='organ',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True),
        ),
        migrations.AlterField(
            model_name='organ',
            name='proof',
            field=models.FileField(upload_to='organ_proofs/%Y/%m'),
        ),
    ]