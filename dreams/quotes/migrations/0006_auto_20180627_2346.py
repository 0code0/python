# Generated by Django 2.0 on 2018-06-27 18:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0005_auto_20180627_2336'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quotes',
            old_name='authorstring',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='quotes',
            old_name='quotesstring',
            new_name='quotes',
        ),
    ]
