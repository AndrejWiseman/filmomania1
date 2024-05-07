from django.contrib import admin
from .models import DomaciFilmovi


class FilmoviAdmin(admin.ModelAdmin):
    list_display = ['title']
    prepopulated_fields = {"slug": ("title", )}



# Register your models here.
admin.site.register(DomaciFilmovi, FilmoviAdmin)
