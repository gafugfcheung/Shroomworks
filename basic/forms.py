from django import forms
from .models import Pic


class PicForm(forms.ModelForm):
    class Meta:
        model = Pic
        fields = ('lat', 'lng')
