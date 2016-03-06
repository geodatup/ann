# -*- coding: utf-8 -*-

from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _

#from .menu import DocumentSubMenu


class galerieApp(CMSApp):
    name = _('galerie')
    urls = ['ann.apps.galerie.urls', ]
    app_name = "galerie"
   # menus = [DocumentSubMenu, ]

apphook_pool.register(galerieApp)