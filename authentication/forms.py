from django import forms
from django.utils.translation import gettext_lazy as _

# class SignupForm(ModelForm):
#   class Meta:
#     model = User
#     fields = '__all__'

#   def save(self, commit=True):
#     levelMap = {
#       'student': 200,
#       'instructor': 300,
#       'admin': 100
#     }
#     user = super(ModelForm, self).save(commit=False)
#     user.level = levelMap[self.cleaned_data['account_type']]
#     if commit:
#       user.save()
#     return user

ACCOUNT_TYPE = (
  ('STUDENT', 'Student'),
  ('INSTRUCTOR', 'Instructor'),
  ('ADMIN', 'Admin')
)

class SignupForm(forms.Form):
  first_name = forms.CharField(max_length=200)
  last_name = forms.CharField(max_length=200)
  password = forms.CharField(max_length=300, widget=forms.PasswordInput())
  password_again = forms.CharField(max_length=300, widget=forms.PasswordInput())
  username = forms.CharField(max_length=300)
  email = forms.EmailField(max_length=300)
  account_type = forms.ChoiceField(choices=ACCOUNT_TYPE)

  help_texts = {
    'email': _('Please enter your personal email id')
  }
  labels = {
    'first_name': _('First Name'),
    'last_name': _('Last Name')
  }
  error_messages = {
    'first_name': {
      'max_length': _('The first name is more than 200 characters!')
    },
    'last_name': {
      'max_length': _('The last name is more than 200 characters!')
    }
  }

