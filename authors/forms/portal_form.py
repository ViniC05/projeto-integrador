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
            ),
            'title' : forms.TextInput(attrs={'placeholder':'Digite o titulo aqui' }),
            'mini_description' : forms.TextInput(attrs={'placeholder' : 'Digite a mini descrição aqui'}),
            'rua' : forms.TextInput(attrs={'placeholder' : 'Ex: Rua vinte'}),
            'bairro' : forms.TextInput(attrs={'placeholder' : 'Ex: Centro'}),
            'description' : forms.Textarea(attrs={'placeholder' : 'Digite a descrição aqui'}),
            
        }
        labels = {
            'title': 'Titulo',
            'mini_description' : 'Mini descrição',
            'description' : 'Descrição',
            'cover' : 'Imagem',
        }

        place_holders = {
            'title' : 'Digite o titulo'
        }
