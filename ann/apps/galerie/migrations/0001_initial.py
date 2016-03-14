# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import filer.fields.image
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0002_auto_20150606_2003'),
    ]

    operations = [
        migrations.CreateModel(
            name='Oeuvre',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('titre', models.CharField(max_length=50)),
                ('dimension', models.CharField(blank=True, max_length=50, null=True)),
                ('technique', models.CharField(blank=True, max_length=50, null=True)),
                ('slug', models.SlugField(max_length=64, help_text='mettre un slug unique pour cette oeuvre', verbose_name='slug', default='')),
                ('photo', filer.fields.image.FilerImageField(on_delete=django.db.models.deletion.SET_NULL, null=True, blank=True, to='filer.Image')),
            ],
        ),
        migrations.CreateModel(
            name='Rubrique',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('nom_rubrique', models.CharField(max_length=30)),
                ('annee', models.PositiveIntegerField(blank=True, null=True)),
                ('commentaire', models.TextField(blank=True, null=True)),
                ('slug', models.SlugField(max_length=64, help_text='mettre un slug unique pour cette rubrique', verbose_name='slug', default='')),
                ('icon', filer.fields.image.FilerImageField(on_delete=django.db.models.deletion.SET_NULL, null=True, blank=True, to='filer.Image')),
            ],
        ),
        migrations.AddField(
            model_name='oeuvre',
            name='rubrique',
            field=models.ForeignKey(null=True, blank=True, to='galerie.Rubrique'),
        ),
    ]
