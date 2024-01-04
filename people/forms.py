from django import forms

from people.models import Partner, Categories


class AddPostForm(forms.Form):
    title = forms.CharField(max_length=255)
    slug = forms.SlugField(max_length=255)
    content = forms.CharField(widget=forms.Textarea())
    is_published = forms.BooleanField()
    category = forms.ModelChoiceField(queryset=Categories.objects.all())
    partner = forms.ModelChoiceField(queryset=Partner.objects.all())
