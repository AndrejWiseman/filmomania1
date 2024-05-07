from django.shortcuts import render, get_object_or_404
from django.db.models import Count
from itertools import chain
import itertools
from operator import attrgetter

from django.shortcuts import render

from filmovi.models import Filmovi
from serije.models import Serije
from domaci_filmovi.models import DomaciFilmovi
from domace_serije.models import DomaceSerije

from taggit.models import Tag

# Create your views here.
def tagged(request, slug):
    # Dohvaćanje taga koji odgovara slug-u
    tag = get_object_or_404(Tag, slug=slug)

    # Filtriranje filmova i serija po tagu
    common_tags_film = Filmovi.tags.most_common().annotate(num_times=Count('taggit_taggeditem_items')).order_by(
        '-num_times')
    common_tags_serija = Serije.tags.most_common().annotate(num_times=Count('taggit_taggeditem_items')).order_by(
        '-num_times')
    common_tags_domaci_f = DomaciFilmovi.tags.most_common().annotate(num_times=Count('taggit_taggeditem_items')).order_by(
        '-num_times')
    common_tags_domace_s = DomaciFilmovi.tags.most_common().annotate(
        num_times=Count('taggit_taggeditem_items')).order_by(
        '-num_times')
    # Spajanje tagova iz oba modela i uklanjanje duplikata
    common_tags = list(set(list(common_tags_film) + list(common_tags_serija) + list(common_tags_domaci_f) + list(common_tags_domace_s)))

    queryset_f = Filmovi.objects.filter(tags=tag)
    queryset_s = Serije.objects.filter(tags=tag)
    queryset_df = DomaciFilmovi.objects.filter(tags=tag)
    queryset_ds = DomaceSerije.objects.filter(tags=tag)


    # Kombiniranje filmova i serija u jedan queryset
    kombinirani_qs = list(set(list(queryset_s) + list(queryset_f) + list(queryset_df) + list(queryset_ds)))


    # Sortiranje kombiniranog queryseta po datumu
    # sortirano_po_datumu = sorted(kombinirani_qs, key=attrgetter('date'), reverse=True)

    context = {
        'tag': tag,
        'common_tags': common_tags,
        'kombinirani_qs': kombinirani_qs,

    }
    return render(request, 'tagged.html', context)
