from django.urls import path
from .views import user_count_view

urlpatterns = [
    path('', user_count_view, name='user-count'),  # Корневой маршрут
]
