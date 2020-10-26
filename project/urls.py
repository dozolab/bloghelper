"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from apps.telegram.views import webhook

web_hook_secret_url = settings.BOT_TOKEN + '/'
if settings.DEBUG:
    web_hook_secret_url = ''

urlpatterns = [
    path('admin/', admin.site.urls),
    path(f'webhook/{web_hook_secret_url}', csrf_exempt(webhook.web_hook_view))
]

