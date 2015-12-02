from fuzzywuzzy import fuzz
import copy


areasFile = open('chennaiAreas.txt', 'r')
LOCATIONS = map (lambda x:x.replace(' ', ''), areasFile.read().split('\n'))
areasFile.close()


def cloneTweet(tweet):
	return copy.copy(tweet)

def parseTweet(tweet):
	isFirst = True
	words = tweet["text"].split(' ')
	newTweets = []
	theTweet = tweet
	for word in words:
		for location in LOCATIONS:
			score = fuzz.ratio(word, location)
			if score > 75:
				if not isFirst:
					tweet = cloneTweet(theTweet)
				tweet["location"] = location
				isFirst = False
				newTweets.append(tweet)
	return newTweets

