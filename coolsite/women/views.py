from django.http import HttpResponse
from django.shortcuts import render
#для хранения представлений(контролеры) текущего приложения
def index(reques):
    return HttpResponse('главная страница вумен')
def categories(request):
    return HttpResponse('<h1>Категории</h1>')
def categor(request):
    return HttpResponse('<i>Курсив</i>')