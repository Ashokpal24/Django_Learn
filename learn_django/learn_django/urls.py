from django.contrib import admin
from django.urls import path
from account.views import login_user as login_view
from account.views import logout_user as logout_view
from account.views import register_user as register_view
from article.views import create_article as create_article_view
from article.views import list_article as list_article_view
from article.views import update_article as update_article_view
from article.views import list_all_article as list_all_article_view
from article.views import detail_article as detail_article_view
from article.views import delete_article as delete_article_view


from app.views import home as home_view
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", login_view, name='login'),
    path("logout/", logout_view, name='logout'),
    path("register/", register_view, name='register'),
    path("home/", list_all_article_view, name='home'),
    path("article/", list_article_view, name="article-list"),
    path("articles/create/", create_article_view, name="article-create"),
    path("article/update/<int:id>", update_article_view, name="article-update"),
    path("article/detail/<int:id>", detail_article_view, name="article-detail"),
    path("article/delete/<int:id>", delete_article_view, name="article-delete")
]
