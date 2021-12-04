from django.urls import path
from .views import detail_blog_view, create_blog_view, edit_blog_view, post

app_name = 'blog'


urlpatterns = [
    path('', post, name='post'),
    path('create/', create_blog_view, name="create"),
    path('<slug>/', detail_blog_view, name="detail"),
    path('<slug>/edit/', edit_blog_view, name="edit"),
 ]