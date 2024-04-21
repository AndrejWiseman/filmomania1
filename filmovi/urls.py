from django.urls import path

from .views import filmovi

app_name = 'filmovi'

urlpatterns = [
    path('', filmovi, name='filmovi'),
]
