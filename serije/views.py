from django.shortcuts import render, get_object_or_404
from taggit.models import Tag
from django.db.models import Count

from .models import Serije, Epizoda

# Create your views here.
def serije(request):

    queryset = Serije.objects.all().order_by('-date')

    common_tags = Serije.tags.most_common().annotate(num_times=Count('taggit_taggeditem_items')).order_by(
        '-num_times')

    context = {
        'queryset': queryset,
        'common_tags': common_tags
    }
    return render(request, 'serije/serije-lista.html', context)



def tagged(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    common_tags = Serije.tags.most_common()
    queryset = Serije.objects.filter(tags=tag)

    context = {
        'tag': tag,
        'queryset': queryset,
        'common_tags': common_tags
    }
    return render(request, 'serije/serije-lista.html', context)




def serije_detail(request, slug):

    obj = get_object_or_404(Serije, slug=slug)

    epiz = Epizoda.objects.filter(epizode=obj).order_by('-epizode_date')

    context = {
        'object': obj,
        'epiz': epiz
    }
    return render(request, 'serije/serije-detail.html', context)
