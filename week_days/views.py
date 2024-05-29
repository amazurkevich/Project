from django.shortcuts import render
from django.http import response

# Create your views here.


def monday(request):
    text = """
    <h3>Monday routine</h3>
    <p>1. work</p>
    <p>2. train</p>
    <p>3. sleep</p>
    """
    return response.HttpResponse(text)

def tuesday(request):
    text = """
    <h3>Tuesday routine</h3>
    <p>1. work</p>
    <p>2. train</p>
    <p>3. sleep</p>
    """
    return response.HttpResponse(text)
