from django import forms
from django.forms import *

from .models import *


class ResumeForm(ModelForm):
    class Meta:
        model = Files
        fields = ['file']


class EditorForm(ModelForm):
    class Meta:
        model = Editor
        fields = ['source', 'result', 'command', 'empty_views']
        widgets = {
            "source": TextInput(attrs={
                "class": "form-control",
                "placeholder": "...",
                "id": "source"
            }),
            "result": TextInput(attrs={
                "class": "form-control",
                "placeholder": "...",
                "id": "result"
            }),

        }
        empty_views = ChoiceField(choices=[("1", 'пробел'), ("2", 'Nan'), ("3", 'none')])
        command = ChoiceField(choices=[("1", 'соединить'), ("2", 'разъединить'), ("3", 'переименовать')])
