from fuzzywuzzy import fuzz
from collections import defaultdict
import copy

import sys


areasFile = open('chennaiAreas.txt', 'r')
LOCATIONS = map (lambda x:x.replace(' ', '').lower(), areasFile.read().split('\n'))
areasFile.close()

scoreMap = defaultdict(lambda:70)
scoreMap['bus'] = 90
scoreMap['boat'] = 90
scoreMap['train'] = 90
scoreMap['food'] = 95
scoreMap['hunger'] = 80
scoreMap['starvation'] = 80
scoreMap['shelter'] = 80
scoreMap['tneb'] = 90
scoreMap['army'] = 85
scoreMap['navy'] = 85
scoreMap['relief'] = 70
scoreMap['aid'] = 95
scoreMap['airport'] = 85
scoreMap['flight'] = 90
scoreMap['plane'] = 90

TRANSPORT_MAP = {
	'train'		:	['train', 'metro'],
	'bus'		:	['bus', 'busstop', 'auto'],
	'boat'		:	['boat', 'ship', 'waterscooter'],
	'flight'	:	['airport', 'plane', 'flight'],
}


SERVICE_MAP = {
	'food'		:	['food', 'foodpacket', 'hunger', 'starvation'],
	'stay'		:	['accomodation', 'shelter'],
	'power'		:	['electricity', 'power', 'tneb'],
	'helpline'	:	['help', 'helpline', 'army', 'navy', 'relief', 'aid']
}

def cloneTweet(tweet):
	return copy.copy(tweet)

def parseTweet(tweet):
	tweet['created_at'] = tweet['created_at'].split('+')[0]
	tweet['timestampint'] = int(tweet['timestamp_ms'])
	isFirst = True
	words = tweet["text"].split(' ')
	newTweets = []
	theTweet = tweet
	for location in LOCATIONS:
		for word in words:
			score = fuzz.ratio(word.lower(), location)
			if score > scoreMap[location]:
				if not isFirst:
					tweet = cloneTweet(theTweet)
				tweet["location"] = location
				isFirst = False
				newTweets.append(tweet)
				break
	for key, values in TRANSPORT_MAP.iteritems():
		done = False
		for value in values:
			if done:
				break
			for word in words:
				score = fuzz.ratio(word.lower(), value)
				if score > scoreMap[value]:
					if not isFirst:
						tweet = cloneTweet(theTweet)
					tweet["transport"] = key
					isFirst = False
					newTweets.append(tweet)
					done = True
					break
	for key, values in SERVICE_MAP.iteritems():
		done = False
		for value in values:
			if done:
				break
			for word in words:
				score = fuzz.ratio(word.lower(), value)
				if score > scoreMap[value]:
					if not isFirst:
						tweet = cloneTweet(theTweet)
					tweet["service"] = key
					isFirst = False
					newTweets.append(tweet)
					done = True
					break
	return newTweets

