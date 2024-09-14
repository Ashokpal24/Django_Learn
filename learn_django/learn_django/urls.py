from django.contrib import admin
from django.urls import path
from account.views import login_user as login_view
from account.views import logout_user as logout_view
from account.views import register_user as register_view

from app.views import home as home_view
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", login_view, name='login'),
    path("logout/", logout_view, name='logout'),
    path("register/", register_view, name='register'),
    path("home/", home_view, name='home')
]
