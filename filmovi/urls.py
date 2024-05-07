from django.urls import path

from .views import filmovi, filmovi_detail_view, tagged

app_name = 'filmovi'

urlpatterns = [
    path('', filmovi, name='filmovi'),

    path('<slug:slug>/', filmovi_detail_view, name='filmovi_detail'),
    path('zanr/<slug:slug>/', tagged, name='tagged'),

]
