# Generated by Django 2.2.5 on 2019-09-27 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20190927_1233'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='title',
            field=models.CharField(default='Default Title', max_length=50),
        ),
    ]
