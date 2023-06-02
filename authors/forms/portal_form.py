from django import forms

from portal.models import portal
from utils.django_forms import add_attr


class AuthorPortalForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


        add_attr(self.fields.get('description'), 'class', 'span-2')
    class Meta:
        model = portal
        fields = 'title', 'mini_description', 'rua', 'bairro', 'description', 'cover'
        widgets = {
            'cover': forms.FileInput(
                attrs={'class': 'span-2'
                       }
            )
        }
