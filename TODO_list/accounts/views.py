from django.contrib.auth import login
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.urls import reverse

from TODO_list.settings import HOST_NAME
from accounts.models import Token
from .forms import UserCreationForm


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