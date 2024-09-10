from django.contrib import admin
from django.urls import path
from account.views import login_user as login_view
from app.views import home as home_view
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", login_view, name='login'),
    path("home/", home_view, name='home')
]
