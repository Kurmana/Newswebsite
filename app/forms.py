from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'content']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите имя'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Введите почту'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Введите текст'})
        }

