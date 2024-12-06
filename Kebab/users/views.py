from django.shortcuts import render

from django.contrib.auth.models import User
from django.shortcuts import render
from .models import Visit

def user_count_view(request):
    # Получаем или создаём объект для хранения количества посещений
    visit, created = Visit.objects.get_or_create(id=1)
    visit.total_visits += 1  # Увеличиваем счётчик посещений
    visit.save()

    user_count = User.objects.count()  # Считаем количество пользователей
    return render(request, 'user_count.html', {
        'user_count': user_count,
        'total_visits': visit.total_visits,  # Передаём счётчик в шаблон
    })
