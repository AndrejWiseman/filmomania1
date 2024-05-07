from django.urls import path
from .views import serije, serije_detail, tagged

app_name = 'serije'
urlpatterns = [
    path('', serije, name='serije'),

    path('<slug:slug>/', serije_detail, name='serije-detail'),
    path('zanr/<slug:slug>/', tagged, name='tagged'),

]
