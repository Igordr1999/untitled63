from django.db import models


# Create your models here.
class RadioStation(models.Model):
    name = models.CharField(verbose_name="Название (ru)", max_length=100)
    name_en = models.CharField(verbose_name="Название (en)", max_length=100)
    description = models.TextField(verbose_name="Описание", max_length=2000)
    logo = models.ImageField(upload_to="radio/logo/", default="radio/logo/default.png")
    url_broadcasting = models.URLField(verbose_name="URL вещания")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Радиостанция"
        verbose_name_plural = "Радиостанции"
        ordering = ['name']
