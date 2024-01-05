from django.db import models
from django.db.models.query import QuerySet
from django.core.validators import MinLengthValidator, MaxValueValidator


class PublishedManager(models.Manager):
    def get_queryset(self) -> QuerySet:
        return super().get_queryset().filter(is_published=People.Status.PUBLISHED)


class People(models.Model):
    class Status(models.IntegerChoices):
        DRAFT = (0, "Черновик")
        PUBLISHED = (1, "Опубликовано")

    title = models.CharField(max_length=255)
    slug = models.SlugField(
        max_length=255,
        unique=True,
        db_index=True,
        verbose_name="Slug",
        validators=[
            MinLengthValidator(5, message="Минимум 5 символов"),
            MaxValueValidator(100, message="Максимум 100 символов"),
        ],
    )
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(
        choices=tuple(map(lambda x: (bool(x[0]), x[1]), Status.choices)),
        default=Status.DRAFT,
    )
    category = models.ForeignKey(
        "Categories", on_delete=models.PROTECT, related_name="posts"
    )
    tags = models.ManyToManyField("TagPost", blank=True, related_name="tags")
    partner = models.OneToOneField(
        "Partner",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="partner",
    )

    objects = models.Manager()
    published = PublishedManager()

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = "Известные люди"
        verbose_name_plural = "Известные люди"
        ordering = ("-time_create",)
        indexes = [models.Index(fields=("-time_create",))]


class Categories(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self) -> str:
        return self.name


class TagPost(models.Model):
    tag = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, db_index=True, unique=True)

    def __str__(self) -> str:
        return self.tag


class Partner(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(null=True)

    def __str__(self) -> str:
        return self.name
