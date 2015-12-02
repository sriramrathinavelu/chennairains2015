from django.shortcuts import render
from models import *

# Create your views here.

areasFile = open('chennaiAreas.txt', 'r')
LOCATIONS = map (lambda x:x.replace(' ', ''), areasFile.read().split('\n'))
areasFile.close()

def home(request):
	latestHotlineTweets = HotlineNumber.objects.all().order_by('-timestampint').limit(10) 
	return render(request, 'home.html', {
		'locations'		:LOCATIONS,
		'transport'		:['train', 'bus', 'boat', 'flight'],
		'service'		:['food', 'stay', 'power', 'helpline'],
		'hotlineTweets'	:latestHotlineTweets,
	})

def serviceTweets(request):
	service = request.GET.get('service').lower()
	limit = int(request.GET.get('limit', 1000))
	tweets = ChennaiRains.objects.filter(service=service).order_by('-timestampint').limit(limit)
	context = {'tweets' : tweets}
	return render(request, 'locationtweets.html', context)

def transportTweets(request):
	transport = request.GET.get('transport').lower()
	limit = int(request.GET.get('limit', 1000))
	tweets = ChennaiRains.objects.filter(transport=transport).order_by('-timestampint').limit(limit)
	context = {'tweets' : tweets}
	return render(request, 'locationtweets.html', context)

def locationTweets(request):
	location = request.GET.get('location').lower()
	limit = int(request.GET.get('limit', 1000))
	tweets = ChennaiRains.objects.filter(location=location).order_by('-timestampint').limit(limit)
	context = {'tweets' : tweets}
	return render(request, 'locationtweets.html', context)

def hotlineNumber(request):
	limit = int(request.GET.get('limit', 1000))
	latestHotlineTweets = HotlineNumber.objects.all().order_by('-timestampint').limit(limit) 
	context = {'tweets' : latestHotlineTweets}
	return render(request, 'locationtweets.html', context)

def needRescue(request):
	limit = int(request.GET.get('limit', 1000))
	tweets = NeedRescue.objects.all().order_by('-timestampint').limit(limit) 
	context = {'tweets' : tweets}
	return render(request, 'locationtweets.html', context)

def offerRescue(request):
	limit = int(request.GET.get('limit', 1000))
	tweets = OfferRescue.objects.all().order_by('-timestampint').limit(limit) 
	context = {'tweets' : tweets}
	return render(request, 'locationtweets.html', context)

def contactUs(request):
	return render(request, 'contact.html', {})
