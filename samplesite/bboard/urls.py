from django.urls import path

from .views import *

# Этот файл не создает маршруты а только получает их
urlpatterns = [
    path('add/', BbCreateView.as_view(), name='add'),
    path('<int:rubric_id>/', by_rubric, name='by_rubric'),
    path('', index, name='index'),
]
