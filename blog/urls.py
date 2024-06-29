from django.urls import path
from .views import post_list, post_detail, PostListView

app_name = 'blog'

urlpatterns = [
 # представления поста
 path('', post_list, name='post_list'),
 path('<int:post_id>share/', post_detail, name='post_detail')
]