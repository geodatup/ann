# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import djangocms_text_ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('galerie', '0002_rubrique_article'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rubrique',
            name='article',
            field=djangocms_text_ckeditor.fields.HTMLField(null=True, blank=True),
        ),
    ]
