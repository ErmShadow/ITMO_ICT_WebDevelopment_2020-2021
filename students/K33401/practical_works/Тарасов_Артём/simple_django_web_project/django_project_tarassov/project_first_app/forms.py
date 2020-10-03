from django import forms
from .models import Driver


class DriverForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = [
            "first_name",
            "last_name",
            "date_of_birthday",
        ]
