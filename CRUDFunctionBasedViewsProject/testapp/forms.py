from testapp.models import FBV_MODEL
from django import forms

class FBV_FORM(forms.ModelForm):
    class Meta:
        model=FBV_MODEL
        fields='__all__'
