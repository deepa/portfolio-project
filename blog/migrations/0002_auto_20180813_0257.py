# Generated by Django 2.1 on 2018-08-13 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='body',
            field=models.TextField(),
        ),
    ]