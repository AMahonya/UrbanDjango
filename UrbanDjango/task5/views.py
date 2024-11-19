from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister

# Create your views here.

users = ['Filin23', 'DrAqula45', 'Pinki4']


def sign_up_by_django(request):
    info = {}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            if username in users:
                info['error'] = 'Пользователь уже существует'
            elif password != repeat_password:
                info['error'] = 'Пароли не совпадают'

            elif age < 18:
                info['error'] = 'Вы должны быть старше 18'
            else:
                info['message'] = f'Приветствуем, {username}!'

        else:
            info['error'] = form.errors
            info['form'] = form

    else:
        info['form'] = UserRegister()

    return render(request, 'registration_page.html', {'info': info})


def sign_up_by_html(request):
    info = {}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        repeat_password = request.POST['repeat_password']
        try:
            age = int(request.POST.get('age'))
        except (ValueError, TypeError):
            age = -1

        if username in users:
            info['error'] = 'Пользователь уже существует'
        elif password != repeat_password:
            info['error'] = 'Пароли не совпадают'

        elif age < 18:
            info['error'] = 'Вы должны быть старше 18'
        else:
            info['message'] = f'Приветствуем, {username}!'

    return render(request, 'registration_page.html', {'info': info})