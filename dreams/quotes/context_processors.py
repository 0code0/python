from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse
from quotes.models import *

def categories(request):

	return {
		'categories': category.objects.all()[:3],
		'authors': author.objects.all()[:3]
	}