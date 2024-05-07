from django.urls import path
from .views import home, tagged

app_name = 'home'

urlpatterns = [
    path('', home, name='home'),
    path('zanr/<slug:slug>/', tagged, name='tagged'),
]
