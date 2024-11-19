"""
URL configuration for UrbanDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

from task2.views import func_temp, class_temp
from task4.views import main_page, services, gallery
from task5.views import sign_up_by_django, sign_up_by_html

urlpatterns = [
    path('admin/', admin.site.urls),
    path('func/', func_temp),
    path('class/', class_temp.as_view()),
    path('nails/', main_page, name="main"),
    path('nails/services/', services, name='nails_services'),
    path('nails/gallery/', gallery, name='nails_gallery'),
    path('sign_up_by_django/', sign_up_by_django, name='Registraciya'),
    path('sign_up_by_html/', sign_up_by_html, name='Registraciya'),

]