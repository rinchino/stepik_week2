# Create your views here.
from django.shortcuts import render
from django.http import HttpResponseNotFound
from django.http import HttpResponseServerError


def custom_handler500(request):
    return HttpResponseServerError('Внутреняя ошибка сервера')


def custom_handler404(request, exception):
    return HttpResponseNotFound('Страница не найдена!')


def main_view(request):
    return render(request, 'index.html')


def departure_view(request, departure):
    return render(request, 'departure.html')


def tour_view(request, id):
    return render(request, 'tour.html')
