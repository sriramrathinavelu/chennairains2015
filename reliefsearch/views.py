from django.shortcuts import render
from models import *

# Create your views here.

areasFile = open('chennaiAreas.txt', 'r')
LOCATIONS = map (lambda x:x.replace(' ', ''), areasFile.read().split('\n'))
areasFile.close()

def home(request):
	return render(request, 'home.html', {'locations':LOCATIONS})

def locationTweets(request):
	location = request.GET.get('location')
	tweets = ChennaiRains.objects.filter(location=location)
	context = {'tweets' : tweets}
	return render(request, 'locationtweets.html', context)
