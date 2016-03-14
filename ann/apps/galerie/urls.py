from django.conf.urls import patterns, url
from . import views
from .views import RubriqueListView, RubriqueDetailView, OeuvreListView, OeuvreDetailView


app_name = 'galerie'
urlpatterns = patterns('',
	url(r'^$', views.OeuvreListView.as_view(), name='oeuvreIndex'),
	url(r'^accueil/$', views.accueil.as_view(), name='acceuil'),
    url(r'^rubrique/$', views.RubriqueListView.as_view(), name='rubriqueIndex'),
    url(r'^rubrique/(?P<slug>[^/]+)', views.RubriqueDetailView.as_view(), name='rubriqueDetail'),
    url(r'^oeuvre/$', views.OeuvreListView.as_view(), name='oeuvreIndex'),
    url(r'^oeuvre/(?P<slug>[^/]+)', views.OeuvreDetailView.as_view(), name='oeuvreDetail'),
   
)