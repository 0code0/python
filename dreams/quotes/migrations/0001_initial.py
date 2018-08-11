# Generated by Django 2.0 on 2018-06-27 11:10

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('submitedon', models.DateField(default=datetime.date.today)),
                ('isapproved', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('submitedon', models.DateField(default=datetime.date.today)),
                ('isapproved', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='quotes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quotesstring', models.CharField(max_length=500)),
                ('submitedon', models.DateField(default=datetime.date.today)),
                ('isapproved', models.BooleanField(default=False)),
                ('authorstring', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quotes.author')),
                ('categoryid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quotes.category')),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
                ('submitedon', models.DateField(default=datetime.date.today)),
            ],
        ),
        migrations.AddField(
            model_name='quotes',
            name='userid',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='quotes.user'),
        ),
        migrations.AddField(
            model_name='category',
            name='userid',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='quotes.user'),
        ),
        migrations.AddField(
            model_name='author',
            name='userid',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='quotes.user'),
        ),
    ]
