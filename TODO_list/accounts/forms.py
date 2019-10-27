from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError


from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class UserCreationForm(forms.Form):
    username = forms.CharField(max_length=100, label='Username', required=True)
    password = forms.CharField(max_length=100, label='Password', required=True,
                               widget=forms.PasswordInput)
    password_confirm = forms.CharField(max_length=100, label='Password Confirm', required=True,
                                       widget=forms.PasswordInput)
    email = forms.EmailField(label='Email', required=True)

    first_name = forms.CharField(max_length=100, label='first_name', required=False,)
    last_name = forms.CharField(max_length=100, label='last_name', required=False,)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        try:
            User.objects.get(email=email)
            raise ValidationError('User with this email already exists',
                                  code='user_email_exists')
        except User.DoesNotExist:
            return email

    def clean_username(self):
        username = self.cleaned_data.get('username')
        try:
            User.objects.get(username=username)
            raise ValidationError('User with this username already exists',
                                  code='user_username_exists')
        except User.DoesNotExist:
            return username

    def clean(self):
        super().clean()
        password_1 = self.cleaned_data['password']
        password_2 = self.cleaned_data['password_confirm']
        first_name = self.cleaned_data['first_name']
        last_name = self.cleaned_data['last_name']
        if password_1 != password_2:
            raise ValidationError('Passwords do not match',
                                  code='passwords_do_not_match')
        elif first_name == '' and last_name == '':
            raise ValidationError('You should to write first or last name',
                            code='user_name')
        # elif first_name != '':
        #     return first_name
        # elif last_name != '':
        #     return last_name

        return self.cleaned_data

