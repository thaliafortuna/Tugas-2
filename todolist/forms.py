from django import forms
from .models import ListToDo

class TaskForm(forms.ModelForm):
    class Meta:
        model = ListToDo
        fields = ['title', 'description',]