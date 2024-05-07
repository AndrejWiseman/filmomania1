from django.contrib import admin
from .models import Filmovi


class FilmoviAdmin(admin.ModelAdmin):
    list_display = ['title']
    prepopulated_fields = {"slug": ("title", )}



# Register your models here.
admin.site.register(Filmovi, FilmoviAdmin)
