from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

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

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# prva baza podataka
# PGHOST='ep-winter-grass-a2tqpm2x.eu-central-1.aws.neon.tech'
# PGDATABASE='neondb'
# PGUSER='AndrejWiseman'
# PGPASSWORD='VplMtR5hUF9q'
