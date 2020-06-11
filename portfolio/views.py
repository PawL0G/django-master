from django.shortcuts import render


def homepage(request):
    return HttpResponse('Hello, World')
