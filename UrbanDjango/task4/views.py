from django.shortcuts import render
import os
from pathlib import Path

# Create your views here.

def main_page(request):
    return render(request, 'main_page.html')


def services(request):
    services_data = [
        {
            "title": "Классический маникюр",
            "description": "Классический маникюр - это уникальный и неповторимый маникюр, который может быть создан только для вас. Мы используем только лучшие материалы и инструменты, чтобы создать уникальный и красивый маникюр, который будет отличаться от всех остальных.",
            "time": "Время сеанса: 1 час",
            "price": "Цена: 1000 рублей",
        },
        {
            "title": "Европейский маникюр",
            "description": "Европейский маникюр – это необрезной маникюр без использования металлических инструментов для обрезания кожи. Кожа вокруг ногтя не обрезается, а размягчается и отодвигается. Следовательно, исключается риск пораниться и занести инфекцию.",
            "time": "Время сеанса: 45 минут",
            "price": "Цена: 850 рублей",
        },
        {
            "title": "Классический педикюр",
            "description": "Классический (или обрезной) педикюр – первая появившаяся техника ухода за ногтями и кожей ног, она заключается в использовании режущих косметических инструментов для коррекции формы ногтей, срезания огрубевшей кожи, мозолей и натоптышей",
            "time": "Время сеанса: 35 минут",
            "price": "Цена: 550 рублей",
        },
    ]

    context = {
        "head": "Подчеркните свою индивидуальность",
        "services": services_data,
    }
    return render(request, 'services.html', context)


def gallery(request):
    try:
        # Example data; replace with your actual data
        images = [
            {'image_url': 'images/image1.jpg', 'caption': 'Маникюр 1'},
            {'image_url': 'images/image2.jpg', 'caption': 'Маникюр 2'},
        ]
        # Crucial step to use the static file system:
        image_files = [os.path.join('static', i['image_url']) for i in images]

        # Make sure you have your photo folder inside the static folder
        # and static folder in your root django project
        return render(request, 'gallery.html', {'images': images})

    except FileNotFoundError:
        return render(request, 'gallery.html', {'images': None})
