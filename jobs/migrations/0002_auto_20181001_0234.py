# Generated by Django 2.1 on 2018-10-01 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='summary',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='job',
            name='image',
        ),
        migrations.AddField(
            model_name='job',
            name='detail',
            field=models.TextField(default='None'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='job',
            name='link',
            field=models.CharField(default='http://example.com', max_length=100),
            preserve_default=False,
        ),
    ]
