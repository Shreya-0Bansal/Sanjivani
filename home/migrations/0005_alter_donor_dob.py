# Generated by Django 4.2.3 on 2023-07-31 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_donor_dob_alter_looking_dob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donor',
            name='dob',
            field=models.DateField(null=True),
        ),
    ]
