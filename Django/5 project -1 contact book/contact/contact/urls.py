"""
URL configuration for contact project.

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
from book import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.login_view),
    path('dashboard/',views.dashboard_view),
    path('register/',views.register_view),
    path('add/',views.add_contact_view),
    path('view/',views.view_contact_view),
    path('c_password/',views.change_password_view),
    path('set_password/',views.set_new_password),
    path('edit/<id>/',views.edit_contact_view,name='edit'),
    path('update/<id>/data',views.update_contact_view),
    path('logout/',views.logout_view),
    path('profile/',views.update_profile),
    path('duration/',views.duration),
]
