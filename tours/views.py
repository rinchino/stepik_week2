# Create your views here.
import random

from django.http import Http404, HttpResponseNotFound
from django.http import HttpResponseServerError
from django.views.generic.base import TemplateView

from tours import data


class MainView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(MainView, self).get_context_data(**kwargs)
        context['title'] = data.title
        context['subtitle'] = data.subtitle
        context['description'] = data.description
        context['departures'] = data.departures
        context['tours'] = data.tours
        context['tours'] = random.sample(data.tours.items(), 6)
        return context


class TourView(TemplateView):
    template_name = "tour.html"

    def get_context_data(self, **kwargs):
        context = super(TourView, self).get_context_data(**kwargs)
        context['title'] = data.title
        context['departures'] = data.departures
        context['tours'] = data.tours
        return context


class DepartureView(TemplateView):
    template_name = "departure.html"

    def get_context_data(self, departure, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = data.title
        context['departures'] = data.departures
        if departure not in data.departures:
            raise Http404
        context['tours'] = dict((key, value) for (key, value) in data.tours.items() if value['departure'] == departure)
        context['departure'] = departure
        return context


def custom_handler500(request):
    return HttpResponseServerError('Внутреняя ошибка сервера')


def custom_handler404(request, exception):
    return HttpResponseNotFound('Страница не найдена!')
