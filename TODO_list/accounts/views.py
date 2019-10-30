from django.contrib.auth import login
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import DetailView, UpdateView, ListView

from TODO_list.settings import HOST_NAME
from accounts.models import Token
from .forms import UserCreationForm, UserChangeForm, UserChangePasswordForm


def register_view(request):
    if request.method == 'GET':
        form = UserCreationForm()
        return render(request, 'user_create.html', {'form': form})
    elif request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            user = User(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                is_active=False
            )
            user.set_password(form.cleaned_data['password'])
            user.save()

            token = Token.objects.create(user=user)
            activation_url = HOST_NAME + reverse('accounts:user_activate') + \
                             '?token={}'.format(token)

            user.email_user('Регистрация на сайте localhost',
                            'Для активации перейдите по ссылке: {}'.format(activation_url))

            return redirect("webapp:index")
        else:
            return render(request, 'user_create.html', {'form': form})


def user_activate(request):
    token_value = request.GET.get('token')
    try:
        # найти токен
        token = Token.objects.get(token=token_value)

        # активировать пользователя
        user = token.user
        user.is_active = True
        user.save()

        # удалить токен, он больше не нужен
        token.delete()

        # войти
        login(request, user)

        # редирект на главную
        return redirect('webapp:index')
    except Token.DoesNotExist:
        # если токена нет - сразу редирект
        return redirect('webapp:index')


class UserDetailView(DetailView):
    model = User
    template_name = 'user_detail.html'
    context_object_name = 'user_obj'


class UserChangeView(UserPassesTestMixin, UpdateView):
    model = User
    template_name = 'user_update.html'
    context_object_name = 'user_obj'
    form_class = UserChangeForm

    def test_func(self):
        return self.get_object() == self.request.user

    def get_success_url(self):
        return reverse('accounts:user_detail', kwargs={'pk': self.object.pk})


class UserPasswordChangeView(UpdateView):
    model = User
    template_name = 'user_password_change.html'
    form_class = UserChangePasswordForm
    context_object_name = 'user_obj'

    def text_func(self):
        return self.get_object() == self.request.user

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('accounts:login')


class ProfilesListView(ListView):
    template_name = 'profiles.html'
    context_object_name = 'profiles'
    model = User
    paginate_by = 10
    paginate_orphans = 1