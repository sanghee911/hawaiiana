from django.shortcuts import render
from django.http import HttpResponse
from .models import Nigiri, Bento


def nigiri(request):
    nigiries = Nigiri.objects.all().order_by('name')
    bentoes = Bento.objects.all().order_by('name')
    context = {
        'nigiries': nigiries,
        'bentoes': bentoes,
    }

    return render(request, 'nigiri.html', context)


def roll(request):
    return HttpResponse('Rolls')


def donburi(request):
    return HttpResponse('Donburi')


def others(request):
    return HttpResponse('Others')