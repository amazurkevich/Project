import importlib
from django.shortcuts import render
from django.http import response

# Create your views here.

def rectangle(request, width, height):
    return response.HttpResponse(f"Площадь прямоугольника размером {width}х{height} равна {width*height}")


def square(request, width):
    return response.HttpResponse(f"Площадь квадрата размером {width}х{width} равна {width*width}")


def circle(request, radius):
    return response.HttpResponse(f"Площадь круга радиуса {radius} равна {(radius**2)*3.14}")
