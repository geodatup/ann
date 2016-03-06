from django import template

from ann.apps.galerie.models import Rubrique
from django.template.loader import get_template

register = template.Library()



@register.inclusion_tag('rubriqueMenu.html')
def show_index(rubrique):
    rubriqueList = Rubrique.objects.order_by('nom_rubrique')
    
    return {'rubriqueList': rubriqueList}