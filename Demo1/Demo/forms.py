from django import forms
from django.forms import ModelForm
from .models import Demo
class DemoForm(forms.ModelForm):  
    class Meta:  
        model = Demo
        fields = "__all__"  