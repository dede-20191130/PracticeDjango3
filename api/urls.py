from django.urls import path

from api import views

app_name = 'api'

urlpatterns = [
    path('v1/vote/', views.CreateVoteView.as_view(), name='create_vote'),
]
