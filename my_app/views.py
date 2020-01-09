# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import requests 
from django.shortcuts import render
from bs4 import BeautifulSoup
# Create your views here.


def home(request):
    return render(request, 'base.html')


def new_search(request):
    search = request.POST.get('search')
    stuff_frontend = {
        "search": search
    }
    return render(request, 'my_app/new_search.html', stuff_frontend)
