from django import forms

from portal.models import portal
from utils.django_forms import add_attr


class AuthorPortalForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        add_attr(self.fields.get('cover'), 'class', 'span-2')
        add_attr(self.fields.get('description'), 'class', 'span-2')
    class Meta:
        model = portal
        fields = 'title', 'mini_description', 'description', 'days', 'status', 'cover'
