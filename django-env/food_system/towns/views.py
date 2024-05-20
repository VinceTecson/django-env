from django.shortcuts import render
import requests
from .models import *
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

def get_food():
    response = requests.get()