# Generated by Django 4.2.3 on 2023-07-25 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=150)),
                ('image', models.ImageField(blank=True, upload_to='images')),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
