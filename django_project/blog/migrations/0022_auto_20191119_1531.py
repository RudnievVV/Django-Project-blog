# Generated by Django 2.2.5 on 2019-11-19 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0021_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('Undefined', 'UNDEFINED'), ('Sport', 'SPORT'), ('Art', 'ART'), ('Nature', 'NATURE'), ('Tech', 'TECH'), ('Culture', 'CULTURE'), ('Programming', 'PROGRAMMING')], default='Undefined', max_length=20),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
