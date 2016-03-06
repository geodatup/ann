# -*- coding: utf-8 -*-

from django.utils.translation import ugettext_lazy as _
from django.utils.safestring import mark_safe

from menus.base import NavigationNode
from menus.menu_pool import menu_pool
from cms.menu_bases import CMSAttachMenu

from .models import Rubrique


class galerieSubMenu(CMSAttachMenu):

    name = _("Galerie Sous-Menu")

    def get_nodes(self, request):
        nodes = []

        for rubrique in Rubrique.objects.order_by('nom_rubrique').all():

             node = NavigationNode(
                 mark_safe(rubrique.nom_rubrique),
                 rubrique.get_absolute_url(),
                 rubrique.id,
             )

             nodes.append(node)

        return nodes

menu_pool.register_menu(galerieSubMenu)