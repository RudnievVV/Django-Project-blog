from django.urls import include, path
from rest_framework import routers
from . import views
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView
)


router = routers.DefaultRouter()
router.register(r'posts', views.PostViewSet)


urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add-comment-to-post'),
    path('post/<int:pk>/<int:comm>/<int:comm_sub>/', views.add_comment_to_comment, name='add-comment-to-comment'),
    path('post/<int:pk>/<int:comm>/', views.remove_comment, name='remove-comment'),
    path('about/', views.about, name='blog-about'),
]
