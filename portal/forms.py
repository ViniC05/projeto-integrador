from django import forms
from django.core.exceptions import ValidationError

from .models import Comment


def validacao_comentario(value):
    if len(value) < 10:
        raise ValidationError('O comentário deve ter no mínimo 10 caracteres!')
        

class CommentForm(forms.ModelForm):
    content = forms.CharField(validators=[validacao_comentario], min_length=10,)

    class Meta:
        model = Comment
        fields = ['content']
