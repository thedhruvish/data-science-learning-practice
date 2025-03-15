"""
URL configuration for dashboard project.

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
from myapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.login),
    path('dashboard/', views.dashboard),

    path('admin/', views.view_admin),
    path('admin/add/', views.add_admin),
    path('admin/delete/<id>/', views.delete_admin),
    path('admin/update/<id>/', views.update_admin),

    path('branch/', views.view_Branch),
    path('branch/add/', views.add_Branch),
    path('branch/delete/<id>/', views.delete_Branch),
    path('branch/update/<id>/', views.update_Branch),


    path('course/', views.view_course),
    path('course/add/', views.add_course),
    path('course/delete/<id>/', views.delete_Course),
    path('course/update/<id>/', views.update_course),

    path('inquiry/', views.view_inquiry),
    path('inquiry/add/', views.add_inquiry),
    path('inquiry/delete/<id>/', views.delete_inquiry),
    path('inquiry/update/<id>/', views.update_inquiry),
    
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
