"""HR_Managements URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path

from HR import admin_urls, applicant_urls, employee_urls, hr_urls
from HR.views import IndexView, AppRegister, LoginView, HRRegister
from HR_Managements import settings

urlpatterns = [
    path('', IndexView.as_view()),
    path('app_register', AppRegister.as_view()),
    path('hr_register', HRRegister.as_view()),
    path('login_view', LoginView.as_view()),
    path('admin/',admin_urls.urls()),
    path('applicants/',applicant_urls.urls()),
    path('employee/',employee_urls.urls()),
    path('hr/',hr_urls.urls()),
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)