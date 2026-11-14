from django import forms
from .models import Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'deadline'] # Поля, которые нужно заполнить
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Название проекта', 'class': 'form-input'}),
            'deadline': forms.DateInput(attrs={'type': 'date', 'class': 'form-input'}),
        }