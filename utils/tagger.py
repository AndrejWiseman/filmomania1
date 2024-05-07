# from django.shortcuts import render, get_object_or_404
# from filmovi.models import Filmovi
# from serije.models import Serije
# from taggit.models import Tag
#
# from operator import attrgetter
# from itertools import chain
#
#
# def tagged(request, slug):
#     # list(Articles.objects.all())
#     film = list(Filmovi.objects.all())
#     serija = list(Serije.objects.all())
#
#     # sortirano = sorted(chain(film, serija), key=attrgetter('date'), reverse=True)
#     sortirano = film | serija
#
#
#     tag = get_object_or_404(Tag, slug=slug)
#     # common_tags = Filmovi.tags.most_common()
#     common_tags = sortirano.tags.most_common()
#     # queryset = Filmovi.objects.filter(tags=tag)
#     # kombinovano = sortirano.objects.filter(tags=tag)
#     kombinovano = sortirano.objects.filter(tags=tag)
#
#     context = {
#         'tag': tag,
#         # 'queryset': queryset,
#         'common_tags': common_tags,
#         'sortirano': sortirano,
#         'kombinovano': kombinovano
#     }
#     return render(request, 'filmovi/film-list.html', context)
#
