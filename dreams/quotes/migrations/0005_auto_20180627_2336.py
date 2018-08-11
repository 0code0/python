# Generated by Django 2.0 on 2018-06-27 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0004_author_isdeleted'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quotes',
            old_name='categoryid',
            new_name='category',
        ),
        migrations.AddField(
            model_name='quotes',
            name='isdeleted',
            field=models.BooleanField(default=False),
        ),
    ]
