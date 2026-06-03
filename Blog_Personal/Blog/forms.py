from django import forms
from .models import Post, Perfil

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'asunto', 'contenido']

        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. Mi primer proyecto...'}),
            'asunto': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Breve resumen del post'}),
            'contenido': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Desarrolla aquí tu idea...'}),
        }

class PerfilFrom(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['foto_perfil']
        widgets = {
            'foto_perfil': forms.FileInput(attrs={'class': 'form-control'}),
        }