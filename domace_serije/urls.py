from django.urls import path
from .views import domace_serije, domace_s_detail, tagged

app_name = 'domace_serije'

urlpatterns = [
    path('', domace_serije, name='domace_serije'),
    path('<slug:slug>/', domace_s_detail, name='domace_s_detail'),
    path('zanr/<slug:slug>/', tagged, name='tagged'),
]