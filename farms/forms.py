from django import forms
from django.forms import ModelForm
from localflavor.us.forms import USStateSelect
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from farms.models import Farmer


class SignUpForm():

    class Meta:
        model = Farmer
        fields = [
            'username', 'password',
            'email', 'phone_number',
        ]


class LoginForm(ModelForm):


    class Meta:
        model = Farmer
        fields = [
            'username', 'password',
        ]


class ProfileForm(ModelForm):

    state = forms.CharField(widget=USStateSelect(), initial='HI')

    class Meta:
        model = Farmer
        fields = [
            'first_name', 'last_name',
            'email', 'phone_number',
            'street_address',
            'city', 'state', 'zipcode',
        ]




# class AlertForm(forms.Form):
#
#     validation_text = forms.CharField(
#         label='',
#         max_length=15,
#     )
#
#     def __init__(self, *args, **kwargs):
#         self.send_text = kwargs.pop('send_text')
#         super(AlertForm, self).__init__(*args, **kwargs)
#         self.fields['validation_text'].widget = forms.TextInput(
#             attrs = {
#                 'placeholder': self.send_text
#             }
#         )
#
#     def clean_validation_text(self):
#         validation_text = self.cleaned_data['validation_text']
#         print(self.send_text)
#         if validation_text != self.send_text:
#             raise forms.ValidationError("Incorrect verification message!")
#         return validation_text
#
#
#
#

