from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('home.urls')),
    path('filmovi/', include('filmovi.urls')),
    path('serije/', include('serije.urls')),
    path('domaci-filmovi/', include('domaci_filmovi.urls')),
    path('domace-serije/', include('domace_serije.urls')),
    path('tag/', include('tagged.urls')),

    path('video/', include('video.urls')),

]

# prva baza podataka
# PGHOST='ep-winter-grass-a2tqpm2x.eu-central-1.aws.neon.tech'
# PGDATABASE='neondb'
# PGUSER='AndrejWiseman'
# PGPASSWORD='VplMtR5hUF9q'
