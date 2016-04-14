# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import djangocms_text_ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('galerie', '0004_auto_20160406_1710'),
    ]

    operations = [
        migrations.AddField(
            model_name='oeuvre',
            name='article',
            field=djangocms_text_ckeditor.fields.HTMLField(blank=True, null=True),
        ),
    ]
