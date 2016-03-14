# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galerie', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rubrique',
            name='article',
            field=models.TextField(blank=True, null=True),
        ),
    ]
