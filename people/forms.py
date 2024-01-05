from typing import Any
from django import forms
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.utils.deconstruct import deconstructible

from people.models import Partner, Categories


@deconstructible
class RussianValidator:
    ALLOWED_CHARS = (
        "ЙЦУКЕНГШЩЗХЪЭЖДЛОРПАВЫФЯЧСМИТЬБЮйцукенгшщзхъэждлорпавыыфячсмитьбю1234567890- "
    )
    code = "russian"

    def __init__(self, message=None) -> None:
        self.message = (
            message
            if message
            else "Должны присутствовать только русские символы, дефис и пробел"
        )

    def __call__(self, value, *args: Any, **kwds: Any) -> Any:
        if not set(value) <= set(self.ALLOWED_CHARS):
            raise forms.ValidationError(self.message, code=self.code)


class AddPostForm(forms.Form):
    title = forms.CharField(
        max_length=255,
        min_length=5,
        label="Заголовок",
        widget=forms.TextInput(attrs={"class": "form-input"}),
        error_messages={
            "min_length": "Слишком короткое название статьи",
            "requered": "Это поле обязательно",
        },
    )
    slug = forms.SlugField(
        max_length=255,
        label="URL",
        validators=[
            MinLengthValidator(5, message="Минимум 5 символов"),
            MaxLengthValidator(100, message="Максимум 5 символов"),
        ],
    )
    content = forms.CharField(
        widget=forms.Textarea(attrs={"cols": 50, "rows": 5}),
        required=False,
        label="Котнент",
    )
    is_published = forms.BooleanField(required=False, initial=True, label="Статус")
    category = forms.ModelChoiceField(
        queryset=Categories.objects.all(),
        empty_label="Категория не выбрана",
        label="Категории",
    )
    partner = forms.ModelChoiceField(
        queryset=Partner.objects.all(),
        empty_label="Не замужем/не женат",
        label="Семейное положение",
    )

    def clean_title(self) -> dict[str, Any]:
        title = self.cleaned_data["title"]
        allowed_chars = "ЙЦУКЕНГШЩЗХЪЭЖДЛОРПАВЫФЯЧСМИТЬБЮйцукенгшщзхъэждлорпавыыфячсмитьбю1234567890- "
        if not set(title) <= set(allowed_chars):
            raise forms.ValidationError(
                "Должны присутствовать только русские символы, дефис и пробел"
            )
