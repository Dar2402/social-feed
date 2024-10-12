from django.urls import path
from . import views

app_name = 'feed'

urlpatterns = [
    path('', views.feed_page, name='feed_page'),
    path('message/<int:message_id>/comment/', views.add_comment, name='add_comment'),
    path('message/<int:message_id>/like/', views.like_message, name='like_message'),
    path('comment/<int:comment_id>/like/', views.like_comment, name='like_comment'),
    path('message/<int:message_id>/update/', views.update_message, name='update_message'),
    path('message/<int:message_id>/delete/', views.delete_message, name='delete_message'),
]


