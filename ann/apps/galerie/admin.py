from django.contrib import admin
from import_export import resources
from django import forms
from import_export import resources
from import_export.admin import ImportExportModelAdmin

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

class RubriqueAdmin(ImportExportModelAdmin):
	fieldsets = [
        (None, {'fields': (
          'nom_rubrique',
          'commentaire',
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