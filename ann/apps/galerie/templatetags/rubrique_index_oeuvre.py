from django import template

from ann.apps.galerie.models import Rubrique, Oeuvre
from django.template.loader import get_template

register = template.Library()



@register.inclusion_tag('rubriqueMenu_oeuvre.html',takes_context=True)
def show_index(context, rubrique, slugOeuvre):
    request = context['request']
    rubriqueList = Rubrique.objects.order_by('annee')
    
    urlRubMatchOeuvre = Rubrique.objects.filter(oeuvre__slug=slugOeuvre)[0].get_absolute_url()

    
    return {'rubriqueList': rubriqueList, 'request':request, 'urlRubMatchOeuvre':urlRubMatchOeuvre}