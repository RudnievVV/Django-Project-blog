# Generated by Django 2.2.4 on 2019-09-28 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_comment_related_to_comment_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='parent_comment',
            field=models.IntegerField(default=0),
        ),
    ]