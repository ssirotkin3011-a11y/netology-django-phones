from django.db import models
from django.template.defaultfilters import slugify


class Phone(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)
    price = models.FloatField()
    image = models.CharField(max_length=256, blank=True)  # путь к изображению из csv
    release_date = models.DateField()
    lte_exists = models.BooleanField(default=False)
    slug = models.SlugField(max_length=128, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
