from django.urls import path
from .views import domaci_filmovi, domaci_f_detail, tagged, video

app_name = 'domaci_filmovi'

urlpatterns = [
    path('', domaci_filmovi, name='domaci_filmovi'),
    path('<slug:slug>/', domaci_f_detail, name='domaci_f_detail'),
    path('video/<slug:slug>/', video, name='video'),
    path('zanr/<slug:slug>/', tagged, name='tagged'),
]
