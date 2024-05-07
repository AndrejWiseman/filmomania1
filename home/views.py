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
def home(request):

    film = Filmovi.objects.all().order_by('-date')
    serija = Serije.objects.all().order_by('-date')
    domaci_f = DomaciFilmovi.objects.all().order_by('-date')
    domace_s = DomaceSerije.objects.all().order_by('-date')

    sortirano = sorted(chain(film, serija, domaci_f, domace_s), key=attrgetter('date'), reverse=True)
    combined = sortirano[0:4]

    common_tags_film = Filmovi.tags.most_common().annotate(num_times=Count('taggit_taggeditem_items')).order_by(
        '-num_times')
    common_tags_serija = Serije.tags.most_common().annotate(num_times=Count('taggit_taggeditem_items')).order_by(
        '-num_times')
    common_tags_domaci_f = DomaciFilmovi.tags.most_common().annotate(
        num_times=Count('taggit_taggeditem_items')).order_by(
        '-num_times')
    common_tags_domace_s = DomaceSerije.tags.most_common().annotate(
        num_times=Count('taggit_taggeditem_items')).order_by(
        '-num_times')

    # Spajanje tagova iz oba modela i uklanjanje duplikata
    common_tags = list(set(list(common_tags_film) + list(common_tags_serija) + list(common_tags_domaci_f) + list(common_tags_domace_s)))


    # common_tags_film = Filmovi.tags.most_common()
    # common_tags_serija = Serije.tags.most_common()

    broj = len(sortirano)

    context = {
        'combined': combined,
        'tagged': tagged,
        'sortirano': sortirano,
        'common_tags': common_tags,
        'broj': broj,
    }
    return render(request, 'home/home.html', context)





def tagged(request, slug):
    # Dohvaćanje taga koji odgovara slug-u
    tag = get_object_or_404(Tag, slug=slug)

    # Filtriranje filmova i serija po tagu
    common_tags_film = Filmovi.tags.most_common().annotate(num_times=Count('taggit_taggeditem_items')).order_by(
        '-num_times')
    common_tags_serija = Serije.tags.most_common().annotate(num_times=Count('taggit_taggeditem_items')).order_by(
        '-num_times')
    common_tags_domaci_f = DomaciFilmovi.tags.most_common().annotate(
        num_times=Count('taggit_taggeditem_items')).order_by(
        '-num_times')
    # Spajanje tagova iz oba modela i uklanjanje duplikata
    common_tags = list(set(list(common_tags_film) + list(common_tags_serija)))

    queryset_f = Filmovi.objects.filter(tags=tag)
    queryset_s = Serije.objects.filter(tags=tag)

    # Kombiniranje filmova i serija u jedan queryset
    kombinirani_qs = list(chain(queryset_f, queryset_s))


    # Sortiranje kombiniranog queryseta po datumu
    # sortirano_po_datumu = sorted(kombinirani_qs, key=attrgetter('date'), reverse=True)

    context = {
        'tag': tag,
        'common_tags': common_tags,
        'kombinirani_qs': kombinirani_qs
    }
    return render(request, 'home/home.html', context)


# def tagged(request, slug):
#     # film = list(Filmovi.objects.all())
#     # serija = list(Serije.objects.all())
#
#     film = Filmovi.objects.all().order_by('-date')
#     serija = Serije.objects.all().order_by('-date')
#
#     tag = get_object_or_404(Tag, slug=slug)
#
#     sortirano = sorted(chain(film, serija), key=attrgetter('date'), reverse=True)
#     common_tags = Tag.objects.most_common()
#
#     # sort = sortirano.objects.filter(tags=tag)
#     sort = [obj for obj in sortirano if tag in obj.tags.all()]
#
#
#     context = {
#         'tag': tag,
#         'sort': sort,
#         'common_tags': common_tags,
#         'sortirano': sortirano,
#         # 'kombinovano': kombinovano
#     }
#     return render(request, 'home/home.html', context)

