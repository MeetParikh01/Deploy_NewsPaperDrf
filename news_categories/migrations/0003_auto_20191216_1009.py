# Generated by Django 2.2 on 2019-12-16 10:09

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news_categories', '0002_addnewsmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addnewsmodel',
            name='news_body',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
