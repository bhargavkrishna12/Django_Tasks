"""registration_form URL Configuration

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
from one import views


urlpatterns = (
    path('admin/', admin.site.urls),
    path('', views.home_page.as_view(), name='home'),
    path('signup', views.signup.as_view(), name='signup'),
    path('login/', views.login_page.as_view(), name='login'),
    path('profile/', views.profile_page, name='profile'),
    path('logout/', views.logoutuser, name='logout'),
    path('crud/', views.Crud.as_view(), name='crud'),
    path('update/<int:id>/', views.update_view.as_view(), name='update'),
    path('delete/<int:id>/', views.delete_view.as_view(), name='delete'),
    path('get_sess', views.get_session, name='get1'),
    path('del_sess', views.del_session, name='del1'),
    path('del_coo', views.del_cookie, name='del2'),
    path('get_coo', views.get_cookie, name='get2'),

)
