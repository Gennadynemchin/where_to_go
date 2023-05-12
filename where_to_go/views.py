from django.http import HttpResponse
from django.shortcuts import render


def blank_page(request):
    print('Кто-то зашёл на главную!')
    return render(request, 'index.html')
