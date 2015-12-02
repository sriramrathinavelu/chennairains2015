from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.home, name='home'),
	url(r'locationtweets', views.locationTweets, name='Tweets'),
	url(r'transporttweets', views.transportTweets, name='Tweets'),
	url(r'servicetweets', views.serviceTweets, name='Tweets'),
	url(r'contact', views.contactUs, name='contact')
]
