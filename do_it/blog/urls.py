from django.urls import path
from blog import views

app_name = 'blog'
urlpatterns = [
    path('', views.PostList.as_view(), name='post_list'),
    path('<int:pk>/', views.PostDetail.as_view(), name='post_detail'),
    path('<int:pk>/new_comment/', views.new_comment),
    path('create_post/', views.PostCreate.as_view(), name='create_post'),
    path('update_post/<int:pk>/', views.PostUpdate.as_view(), name='update_post')
]
