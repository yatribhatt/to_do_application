from django import forms
from .models import List

class TodoForm(forms.ModelForm):
    class Meta:
        model = List
        fields = '__all__'