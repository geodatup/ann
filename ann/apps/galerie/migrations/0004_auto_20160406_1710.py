# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galerie', '0003_auto_20160313_1926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oeuvre',
            name='rubrique',
            field=models.ForeignKey(to='galerie.Rubrique'),
        ),
    ]
