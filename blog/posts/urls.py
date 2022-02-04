from django.urls import path

from .views import PostsList, DetailView, PostCreate, PostUpdate, PostDelete, CustomLoginView, RegisterPage

from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),

    path('', PostsList.as_view(), name='posts'),
    path('post/<int:pk>/', DetailView.as_view(), name='post-detail'),
    path('post-create/', PostCreate.as_view(), name='post-create'),
    path('post-update/<int:pk>', PostUpdate.as_view(), name='post-update'),
    path('post-delete/<int:pk>', PostDelete.as_view(), name='post-delete'),
    ]
