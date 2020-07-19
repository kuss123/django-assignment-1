from django.urls import path

from blog.views import blog_view, author_view, home_view

app_name = 'blog'

urlpatterns = [
    path('view/', blog_view, name='view'),
    path('author/<int:id>', author_view),
    path('', home_view, name='home'),

]