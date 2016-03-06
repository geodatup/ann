
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models
from filer.fields.image import FilerImageField
from cms.models.fields import PlaceholderField

# Create your models here.
class Rubrique(models.Model):
    nom_rubrique = models.CharField(max_length=30)
    commentaire = models.TextField(blank=True, null=True)
    slug = models.SlugField(
        u'slug',
        blank=False,
        default='',
        help_text=u'mettre un slug unique pour cette rubrique',
        max_length=64,
    )
    icon = FilerImageField(blank=True, null=True,on_delete=models.SET_NULL,)


    def get_absolute_url(self):
        return reverse('galerie:rubriqueDetail', kwargs={'slug': self.slug, })
        
    def __str__(self):
    	return self.nom_rubrique



class Oeuvre(models.Model):
    titre = models.CharField(max_length=50)
    dimension = models.CharField(max_length=50, null=True, blank=True)
    technique = models.CharField(max_length=50, null=True, blank=True)
    rubrique = models.ForeignKey(Rubrique, blank=True, null=True)
    photo = FilerImageField(blank=True, null=True,on_delete=models.SET_NULL,)
    slug = models.SlugField(
        u'slug',
        blank=False,
        default='',
        help_text=u'mettre un slug unique pour cette oeuvre',
        max_length=64,
    )
    def get_absolute_url(self):
        return reverse('galerie:oeuvreDetail', kwargs={'slug': self.slug, })
    def __str__(self):
        return self.titre