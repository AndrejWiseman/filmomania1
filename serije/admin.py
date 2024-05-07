from django.contrib import admin
from .models import Serije, Epizoda


class EpizodaInline(admin.StackedInline):
    model = Epizoda
    extra = 0
    fields = ['sezona', 'ep', 'epizode_preuzmi', 'epizode_link']


class SerijeAdmin(admin.ModelAdmin):
    list_display = ['title']
    prepopulated_fields = {"slug": ("title", )}
    inlines = [EpizodaInline]


# Register your models here.
admin.site.register(Serije, SerijeAdmin)
