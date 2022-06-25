from django import forms
from .models import TodoItem

class ItemCreateForm(forms.ModelForm):
    class Meta:
        model = TodoItem
        fields = [
            "title",
            "description",
        ]