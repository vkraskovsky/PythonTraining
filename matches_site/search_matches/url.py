from django.urls import path

from . import views

app_name = 'search_matches'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:team_id>/', views.detail, name='detail'),
]
