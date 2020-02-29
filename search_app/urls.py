from django.urls import path

from search_app import views

app_name = 'search'

urlpatterns = [
    path('', views.SearchResultView.as_view(), name='result'),
]
