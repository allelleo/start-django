from django.urls import path, re_path

from .views import index, about, new_article, contact, sign_in, show_post, show_category

urlpatterns = [
    path("", index, name="home"),
    path('about/', about, name="about"),
    path('new-article/', new_article, name="new_article"),
    path('contact/', contact, name="contact"),
    path('sign-in/', sign_in, name="sign_in"),
    path('post/<int:post_id>/', show_post, name="post"),
    path('category/<int:cat_id>/', show_category, name="category"),
]

