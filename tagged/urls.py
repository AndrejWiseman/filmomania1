from django.urls import path
from .views import tagged

app_name = 'tagged'

urlpatterns = [
    # path('', tagged, name='tagged'),
    path('zanr/<slug:slug>/', tagged, name='tagged'),
]