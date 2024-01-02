from django.db import models
from django.db.models.query import QuerySet


class PublishedManager(models.Manager):
    def get_queryset(self) -> QuerySet:
        return super().get_queryset().filter(is_published=People.Status.PUBLISHED)


class People(models.Model):
    class Status(models.IntegerChoices):
        DRAFT = (0, "Черновик")
        PUBLISHED = (1, "Опусбликовано")

    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(choices=Status.choices, default=Status.DRAFT)
    category = models.ForeignKey('Categories', on_delete=models.PROTECT, related_name='posts')
    tags = models.ManyToManyField('TagPost', blank=True, related_name='tags')

    objects = models.Manager()
    published = PublishedManager()

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ("-time_create",)
        indexes = [models.Index(fields=("-time_create",))]


class Categories(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self) -> str:
        return self.name


class TagPost(models.Model):
    tag = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, db_index=True, unique=True)

    def  __str__(self) -> str:
        return self.tag
    