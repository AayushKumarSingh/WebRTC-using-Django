"""
URL configuration for djangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from Learning.views import homepage_view, contact_view, social_view, blood_donation_form, blood_request_form, success_page

urlpatterns = [
    path('admin/', admin.site.urls, name="admin"),
    path("blood-request", blood_request_form, name="blood-request"),
    path('success/', success_page, name='success_page'),
    path("blood-donation/", blood_donation_form, name="blood-donation"),
    path("", homepage_view, name="home"),
    path("contact/", contact_view, name="contact"),
    path("social", social_view, name="social")
]
