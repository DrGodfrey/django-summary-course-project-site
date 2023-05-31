from django import forms

from .models import Participant

# Old code:
# class RegistrationForm(forms.ModelForm):
#     class Meta:
#         model = Participant
#         fields = ['email']


# this one is just there to create user data through a form
class RegistrationForm(forms.Form):
    email = forms.EmailField(label='Your email')

