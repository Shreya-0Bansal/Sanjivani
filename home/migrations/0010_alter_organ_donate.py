# Generated by Django 4.2.3 on 2023-08-02 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_alter_looking_require'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organ',
            name='donate',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]