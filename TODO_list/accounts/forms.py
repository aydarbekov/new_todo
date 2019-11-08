from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError


from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from accounts.models import Profile


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


class UserChangeForm(forms.ModelForm):
    avatar = forms.ImageField(label='Аватар', required=False)
    about = forms.CharField(label='О себе', required=False)
    github_profile = forms.URLField(label='Профиль GitHub', required=False)

    def get_initial_for_field(self, field, field_name):
        if field_name in self.Meta.profile_fields:
            return getattr(self.instance.profile, field_name)
        return super().get_initial_for_field(field, field_name)

    def save(self, commit=True):
        user = super().save(commit=commit)
        self.save_profile(commit)
        return user

    def save_profile(self, commit=True):
        profile, _ = Profile.objects.get_or_create(user=self.instance)
        for field in self.Meta.profile_fields:
            setattr(profile, field, self.cleaned_data.get(field))
        if commit:
            profile.save()

    def clean_github_profile(self):
        github_profile = self.cleaned_data.get('github_profile')
        if 'https://github.com/' not in github_profile:
            raise ValidationError('Invalid url.', code='invalid_url')
        return github_profile


    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'avatar', 'about', 'github_profile']
        profile_fields = ['avatar', 'about', 'github_profile']


class UserChangePasswordForm(forms.ModelForm):
    password = forms.CharField(max_length=100, required=True, label='New Password', widget=forms.PasswordInput)
    password_confirm = forms.CharField(max_length=100, required=True, label='New Password confirm', widget=forms.PasswordInput)
    old_password = forms.CharField(max_length=100, required=True, label='Old Password', widget=forms.PasswordInput)

    def clean_old_password(self):
        old_password = self.cleaned_data.get('old_password')
        user = self.instance
        if not user.check_password(old_password):
            raise ValidationError('Invalid password.', code='invalid_password')
        return old_password

    def save(self, commit=True):
        user = self.instance
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

    def clean(self):
        super().clean()
        password_1 = self.cleaned_data['password']
        password_2 = self.cleaned_data['password_confirm']
        if password_1 != password_2:
            raise ValidationError('Passwords do not match', code='passwords_do_not_match')
        return self.cleaned_data

    class Meta:
        model = User
        fields = ['password', 'password_confirm', 'old_password']