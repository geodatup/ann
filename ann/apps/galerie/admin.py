from django.contrib import admin
from import_export import resources
from django import forms
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from cms.admin.placeholderadmin import PlaceholderAdminMixin




# Register your models here.
from .models import Rubrique, Oeuvre



class OeuvreResource(resources.ModelResource):

    class Meta:
        model = Oeuvre

class OeuvreAdmin(ImportExportModelAdmin):
  list_display = ('titre','rubrique','slug')
  fieldsets = [
        (None, {'fields': (
          'titre',
          'dimension',
          'technique',
          'article',
          'rubrique',          
          'photo'
        )         
        }),
        ('Options Avancées', {
            'classes': ('collapse',),
            'fields': ('slug',),
        }),
    ]
  prepopulated_fields = {'slug': ('titre','photo'), }
  resource_class = OeuvreResource



class RubriqueResource(resources.ModelResource):

    class Meta:
        model = Rubrique

class RubriqueAdmin(PlaceholderAdminMixin, ImportExportModelAdmin):
  list_display = ('nom_rubrique','annee')
  fieldsets = [
        (None, {'fields': (
          'nom_rubrique',
          'annee',
          'commentaire',
          'article',
          'icon'    
        )         
        }),
        ('Options Avancées', {
            'classes': ('collapse',),
            'fields': ('slug',),
        }),
        ]
  prepopulated_fields = {'slug': ('nom_rubrique','icon'), }



admin.site.register(Rubrique, RubriqueAdmin)
admin.site.register(Oeuvre, OeuvreAdmin)