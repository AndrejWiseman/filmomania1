from django.shortcuts import render, get_object_or_404
from .models import DomaciFilmovi
from taggit.models import Tag
from django.db.models import Count


# Create your views here.
def domaci_filmovi(request):

    queryset = DomaciFilmovi.objects.all().order_by('-date')

    common_tags = DomaciFilmovi.tags.most_common().annotate(num_times=Count('taggit_taggeditem_items')).order_by(
        '-num_times')

    context = {
        'queryset': queryset,
        'common_tags': common_tags
    }
    return render(request, 'domaci-filmovi/domaci-f-list.html', context)


def tagged(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    common_tags = DomaciFilmovi.tags.most_common()
    queryset = DomaciFilmovi.objects.filter(tags=tag)

    context = {
        'tag': tag,
        'queryset': queryset,
        'common_tags': common_tags
    }
    return render(request, 'domaci-filmovi/domaci-f-list.html', context)


def domaci_f_detail(request, slug):
    object = get_object_or_404(DomaciFilmovi, slug=slug)
    context = {
        'object': object
    }
    return render(request, 'domaci-filmovi/domaci-f-detail.html', context)


def video(request, slug):
    obj = get_object_or_404(DomaciFilmovi, slug=slug)

    context = {
        'obj': obj
    }

    return render(request, 'video.html', context)




