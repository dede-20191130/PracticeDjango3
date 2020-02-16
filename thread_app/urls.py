from django.urls import path

from . import views

app_name = 'thread'

urlpatterns = [
    path('<int:pk>/', views.TopicDetailView.as_view(), name='topic'),
    path('create_topic/', views.topic_create, name='create_topic'),
]
