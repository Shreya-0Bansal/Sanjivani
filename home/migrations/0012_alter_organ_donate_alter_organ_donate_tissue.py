# Generated by Django 4.2.3 on 2023-08-02 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_alter_organ_donate_tissue'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organ',
            name='donate',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='organ',
            name='donate_tissue',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]