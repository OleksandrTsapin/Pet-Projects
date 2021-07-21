from django.urls import path
from . import views


urlpatterns = [
    path('', views.ListPostView.as_view(), name='home'),
    path('<int:pk>/', views.DetailPostView.as_view()),
    path('create/', views.CreatePostView.as_view()),
    path('update/<int:pk>/', views.UpdatePostView.as_view()),
]
