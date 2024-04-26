from django.urls import path
from . import views

app_name = 'user_profile'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>/update/', views.update, name='update'),
]