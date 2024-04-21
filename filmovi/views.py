from django.shortcuts import render


# Create your views here.
def  filmovi(request):

    return render(request, 'filmovi/film-list.html')
