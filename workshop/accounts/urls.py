from django.urls import path, include
from workshop.accounts import views

urlpatterns = [
    path('register/', views.RegisterUserView.as_view(), name='register'),
    path('login/', views.LoginUserView.as_view(), name='login'),
    path('logout/', views.LogoutUserView.as_view(), name='logout'),
    path('profile/<int:pk>/', include([
        path('', views.DetailsUserView.as_view(), name='profile details'),
        path('edit/', views.EditUserView.as_view(), name='profile edit'),
        path('delete/', views.DeleteUserView.as_view(), name='profile delete')
    ]))
]
