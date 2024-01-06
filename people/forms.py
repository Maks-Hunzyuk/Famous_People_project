from typing import Any

from django import forms
from django.utils.deconstruct import deconstructible

from people.models import Categories, Partner, People


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


class AddPostForm(forms.ModelForm):
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

    class Meta:
        model = People
        fields = (
            "title",
            "slug",
            "content",
            'photo',
            "is_published",
            "category",
            "partner",
            "tags",
        )
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-input"}),
            "content": forms.Textarea(attrs={"cols": 50, "rows": 5}),
        }
        labels = {"slug": "URL"}

        def clean_title(self):
            title = self.cleaned_data["title"]
            print(type(len(title)))
            if len(title) > 50:
                raise forms.ValidationError("Длинна превышает 50 символов")
            return title


class UploadFileForm(forms.Form):
    file = forms.ImageField(label="Фаил")
