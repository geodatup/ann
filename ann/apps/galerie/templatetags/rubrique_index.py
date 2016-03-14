from django import template

from ann.apps.galerie.models import Rubrique
from django.template.loader import get_template

register = template.Library()



@register.inclusion_tag('rubriqueMenu.html',takes_context=True)
def show_index(context, rubrique):
    request = context['request']
    rubriqueList = Rubrique.objects.order_by('annee')
    
    return {'rubriqueList': rubriqueList, 'request':request}