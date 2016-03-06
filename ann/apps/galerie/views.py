from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone
from .models import Rubrique, Oeuvre
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def index(request):
   
    return render(request, 'galerie/annIndex.html')



class RubriqueListView(generic.ListView):
    template_name = 'galerie/rubriqueIndex.html'
    context_object_name = 'latest_rubrique_list'
    queryset = Rubrique.objects.all
    

class RubriqueDetailView(generic.DetailView):
    model = Rubrique
    context_object_name = 'rubrique'
    template_name = 'galerie/rubriqueDetail.html'


class OeuvreListView(generic.ListView):
    model = Oeuvre
    template_name = 'galerie/oeuvreIndex.html'
    
    context_object_name = 'latest_oeuvre_list'
    queryset = Oeuvre.objects.order_by('titre')
    paginate_by = 12




class OeuvreDetailView(generic.DetailView):
    model = Oeuvre
    context_object_name = 'oeuvre'
    template_name = 'galerie/oeuvreDetail.html'
    

