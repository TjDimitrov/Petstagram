from django.urls import path, include
from workshop.photos import views

urlpatterns = [
    path('add/', views.PhotoAddView.as_view(), name='add photo'),
    path('<int:pk>/', include([
        path('', views.details_photo, name='photo details'),
        path('edit/', views.edit_photo, name='photo edit'),
        path('delete/', views.delete_photo, name='photo delete')
    ]))
]