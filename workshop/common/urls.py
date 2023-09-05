from django.urls import path
from workshop.common import views

urlpatterns = (
    path('', views.homepage, name='homepage'),
    path('like/<int:photo_id>/', views.like_photo, name='like photo'),
    path('share/<int:photo_id>/', views.copy_link_to_clipboard, name='share'),
    path('comment/<int:photo_id>/', views.add_comment, name='comment'),
)
