# Generated by Django 2.0 on 2018-06-27 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0003_category_isdeleted'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='isdeleted',
            field=models.BooleanField(default=False),
        ),
    ]
