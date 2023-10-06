from django import forms
from app.models import *

class StudentForms(forms.ModelForm):
    class Meta:
        model=StudentTable
        fields='__all__'