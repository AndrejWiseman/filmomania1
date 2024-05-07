from django.db import models
from django.urls import reverse

from taggit.managers import TaggableManager


# Create your models here.
class Filmovi(models.Model):
    title = models.CharField(max_length=120)
    originalni_naziv = models.CharField(max_length=120, null=False)
    slug = models.SlugField(default="", null=False)
    godina = models.CharField(max_length=120, null=False, blank=False)
    tags = TaggableManager()
    imdb_ocena = models.CharField(max_length=120, null=False)
    description = models.TextField()
    link_za_preuzimanje = models.CharField(default="", max_length=320)
    link_za_prevod = models.CharField(default="", max_length=320)
    link_za_gledanje = models.CharField(default="", max_length=320)
    image = models.FileField(upload_to='movie-images', null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True, null=False, blank=False)

    def get_absolute_url(self):
        return reverse('filmovi:filmovi_detail', kwargs={'slug': self.slug})
