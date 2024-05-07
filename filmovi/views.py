from django.shortcuts import render, get_object_or_404
from .models import Filmovi
from taggit.models import Tag
from django.db.models import Count


# Create your views here.
def filmovi(request):

    queryset = Filmovi.objects.all().order_by('-date')

    common_tags = Filmovi.tags.most_common().annotate(num_times=Count('taggit_taggeditem_items')).order_by(
        '-num_times')

    context = {
        'queryset': queryset,
        'common_tags': common_tags
    }
    return render(request, 'filmovi/film-list.html', context)


def tagged(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    common_tags = Filmovi.tags.most_common()
    queryset = Filmovi.objects.filter(tags=tag)

    context = {
        'tag': tag,
        'queryset': queryset,
        'common_tags': common_tags
    }
    return render(request, 'filmovi/film-list.html', context)


def filmovi_detail_view(request, slug):
    object = get_object_or_404(Filmovi, slug=slug)
    context = {
        'object': object
    }
    return render(request, 'filmovi/detail.html', context)





