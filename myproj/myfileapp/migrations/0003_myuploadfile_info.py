# Generated by Django 3.2.3 on 2021-05-18 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myfileapp', '0002_remove_myuploadfile_f_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuploadfile',
            name='info',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
