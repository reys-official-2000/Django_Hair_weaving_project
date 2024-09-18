from audioop import reverse
from django.db import models
from django.utils.text import slugify


class Model(models.Model):
    image = models.ImageField(upload_to="images/texturemodels")
    name_fa = models.CharField(max_length=150)
    name_en = models.CharField(max_length=150)
    combined = models.CharField(max_length=400, null=True, blank=True)
    more_details = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name_fa} <====> {self.combined}'


