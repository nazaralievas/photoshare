from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return self.name


class Photo(models.Model):
    category = models.ForeignKey(
        to=Category, on_delete=models.SET_NULL,
        null=True, blank=True)
    image = models.ImageField(upload_to="my_images", null=False, blank=False)
    description = models.TextField()

    def __str__(self):
        return self.description
