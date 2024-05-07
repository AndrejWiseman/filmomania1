from django.shortcuts import render, get_object_or_404
from .models import DomaceSerije, Epizoda
from taggit.models import Tag
from django.db.models import Count


# Create your views here.
def domace_serije(request):

    queryset = DomaceSerije.objects.all().order_by('-date')

    common_tags = DomaceSerije.tags.most_common().annotate(num_times=Count('taggit_taggeditem_items')).order_by(
        '-num_times')

    context = {
        'queryset': queryset,
        'common_tags': common_tags
    }
    return render(request, 'domace-serije/domace-s-list.html', context)


def tagged(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    common_tags = DomaceSerije.tags.most_common()
    queryset = DomaceSerije.objects.filter(tags=tag)

    context = {
        'tag': tag,
        'queryset': queryset,
        'common_tags': common_tags
    }
    return render(request, 'domace-serije/domace-s-list.html', context)


def domace_s_detail(request, slug):
    obj = get_object_or_404(DomaceSerije, slug=slug)
    epiz = Epizoda.objects.filter(epizode=obj).order_by('-epizode_date')

    context = {
        'object': obj,
        'epiz': epiz
    }
    return render(request, 'domace-serije/domace-s-detail.html', context)






