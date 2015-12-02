from nltk.corpus import stopwords
import nltk
import re

hTag = re.compile(' #[^ ]+')
uRef = re.compile(' @[^ ]+')
sym = re.compile('[^a-zA-z ]+')
url = re.compile(' https?.* ')

stop = stopwords.words('english')

locFile = open('chennaiAreas.txt')
locations = locFile.read().split('\n')
for loc in locations:
	stop.extend(map(lambda x:x.lower(), loc.split()))
locFile.close()

stop.append('chennai')
stop.append('rt')
stop.append('am')

def get_words_in_tweets(tweets):
	all_words = []
	for (words, sentiment) in tweets:
		all_words.extend(words)
	return all_words

def get_word_features(wordlist):
	wordlist = nltk.FreqDist(wordlist)
	word_features = wordlist.keys()
	return word_features


def sanitizeTweet(tweet):
	tweet = tweet.lower()
	tweet = hTag.sub('', tweet)
	tweet = uRef.sub('', tweet)
	tweet = sym.sub('', tweet)
	tweet = url.sub('', tweet)
	tweet = [x for x in tweet.split(' ') if x not in stop]
	return tweet

posFile = open('offer-rescue.txt', 'r')
pos_tweets = []
for line in posFile.readlines():
	pos_tweets.append((sanitizeTweet(line), True))
posFile.close()


negFile = open('need-rescue.txt', 'r')
neg_tweets = []
for line in negFile.readlines():
	neg_tweets.append((sanitizeTweet(line), False))
negFile.close()

tweets = []

for (words, sentiment) in pos_tweets + neg_tweets:
	words_filtered = [e.lower() for e in words]
	tweets.append((words_filtered, sentiment))

word_features = get_word_features(get_words_in_tweets(tweets))

def extract_features(document):
	document_words = set(document)
	features = {}
	for word in word_features:
		features['contains(%s)' % word] = (word in document_words)
	return features

training_set = nltk.classify.apply_features(extract_features, tweets)

classifier = nltk.NaiveBayesClassifier.train(training_set)

print classifier.show_most_informative_features(32)

def getSentiment(tweet):
	ret = classifier.classify(extract_features(tweet.split()))
	print ret
	return ret

#getSentiment('#ChennaiRainsHelp a house flooded in pallikaranai requires help immdtly Mr U.K .Srinivas 350A 1st for 9 th st kamakothi nagar no mobile')
#getSentiment('@Actor_Siddharth @RJ_Balaji can provide lemon rice, jeera rice, plain rice for help #chennairains #mrcnagar ch-28')
#getSentiment('Southern Railway help line numbers #ChennaiFloods 044-29015204 044-29015208 044-28190216 044-25330714 https://t.co/zUysr3w0sb')
#getSentiment('#Medical_Emergency For Medical Help Oxygen Cylinder Or Generator . Contact : 9840997657 #Chennairains')
#getSentiment('VELACHERY helpline #verified 9381069919 -Boat service 7358236210 -Rescue operations #ChennaiRainsHelp #ChennaiFloods RT! Spread the word')
