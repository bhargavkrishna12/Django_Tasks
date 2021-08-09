"""CLASS_BASED_VIEWS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from CRUD .views import *


urlpatterns = [
    path('admin/', admin.site.urls),

    path('',IndexView.as_view(),name='home'),

    path('<slug:slug>', DetailedView.as_view(), name="post_detail_view"),

    path('manage_post_list/', ManagePostList.as_view(), name="manage_post_list"),

    path('add_post/', AddView.as_view(), name="add_post"),

    path('edit_post/<int:pk>', EditView.as_view(), name="edit_post"),

    path('delete_post/<int:pk>', DeletePostView.as_view(), name="delete_post"),

]
