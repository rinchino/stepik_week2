# Create your views here.
from django.shortcuts import render
from django.http import HttpResponseNotFound
from django.http import HttpResponseServerError


def custom_handler500(request):
    return HttpResponseServerError('Внутреняя ошибка сервера')


def custom_handler404(request, exception):
    return HttpResponseNotFound('Ой, что то сломалось... Простите извините!')


def MainView(request):
    return render(request, 'index.html')


def DepartureView(request, departure):
    return render(request, 'departure.html')


def TourView(request, id):
    return render(request, 'tour.html')
