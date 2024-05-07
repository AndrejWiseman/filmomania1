from django.db import models
from django.urls import reverse

from taggit.managers import TaggableManager


# Create your models here.
class DomaceSerije(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(default="", null=False)
    godina = models.CharField(max_length=120, null=False, blank=False)
    description = models.TextField()
    tags = TaggableManager()
    image = models.FileField(upload_to='movie-images', null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True, null=False, blank=False)

    def get_absolute_url(self):
        return reverse('domace_serije:domace_s_detail', kwargs={'slug': self.slug})


class Epizoda(models.Model):
    epizode = models.ForeignKey(DomaceSerije, on_delete=models.CASCADE)
    epizode_date = models.DateField(auto_now_add=True)
    sezona = models.CharField(max_length=120, null=True, blank=True)
    ep = models.CharField(max_length=120, null=True, blank=True)
    epizode_link = models.CharField(max_length=300)
    epizode_preuzmi = models.CharField(default='', max_length=300)

    def __str__(self):
        return self.ep

