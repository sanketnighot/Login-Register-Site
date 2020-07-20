from django import forms
from .models import Register


class RegisterForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = ['name', 'email' ]

        def __str__(self):
            return self.name
