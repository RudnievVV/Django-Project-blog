# Generated by Django 2.2.4 on 2019-11-02 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20191102_1435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='review_star',
            field=models.IntegerField(),
        ),
    ]
