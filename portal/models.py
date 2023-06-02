from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=65)

    def __str__(self):
        return self.name


class portal(models.Model):
    title = models.CharField(max_length=65)
    mini_description = models.CharField(max_length=165)
    slug = models.SlugField(unique=True)
    days = models.IntegerField(default=0)
    status = models.CharField(max_length=20)
    rua = models.CharField(max_length=70, null=True)
    bairro = models.CharField(max_length=70, null=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    cover = models.ImageField(
        upload_to='portal/covers/%Y/%m/%d/', blank=True, default='')
    Category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True,
        default=None)
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            slug = f'{slugify(self.title)}'
            self.slug = slug

        return super().save(*args, **kwargs)
