import twython, sys, random, pickle
from textblob import TextBlob
from twython import TwythonError
from secrets import *

twitter = twython.Twython(C_KEY, C_SECRET, A_TOKEN, A_TOKEN_SECRET)

freudText = open('texts/freud.txt', 'r')
taxNouns = 'texts/taxnouns.p'

class textGen(object):
	def __init__(self, nounFile, baseText):
		self.nounFile = nounFile
		self.baseText = baseText

	def getNouns(self):
		nounContainer = pickle.load(open(self.nounFile, 'rb'))
		return nounContainer
		

	def wordSwap(self, nounList):
		textHolder = ""
		nounCount = {}

		for line in self.baseText:
			#line = line.rstrip('\r\n')
		 	textHolder += line	

		textHolder.split()
		textHolder = textHolder.decode('utf-8')
		result = TextBlob(textHolder)

		for sentence in result.sentences:
			randSentence = random.choice(result.sentences)
		
		print "old: ", randSentence
		for word, tag in randSentence.tags:
			if tag == 'NN':
				nounCount[random.choice(nounList)] = 0
				temp = random.choice(nounCount.keys())
				if (nounCount[str(temp)]) == 0:
					randSentence = randSentence.replace(word, temp)
				else:
					pass
				nounCount[str(temp)] = 1

		return randSentence
		######

	def cleanup(self, sentence, userN, tweet_id):
		userLen = len(userN)
		sentLen = len(sentence)
		sentence = str(sentence)
		sentence = sentence.replace('"','')
		sentence = sentence.replace('_','')
		sentence = sentence.replace('Forec.', 'foreconscious')
		sentence = sentence.replace('Unc.', 'unconscious')
		if userLen + sentLen < 140:
			print "@", userN, " ", sentence
			try:
				print "hi"
				#twitter.update_status(status= "@" + userN + " " + sentence, in_reply_to_status_id=tweet_id)
			except TwythonError as e:
				print e
		else:
			pass




def getTweet(query):
	tweetInfo = {'username': "", 'tweetID': "", 'tweet': ""}
	response = twitter.search(q=query, result_type='recent', lang = 'en', count=1)
	if len(response['statuses']) > 0:
		first_tweet = response['statuses'][0]
		tweetInfo['username'] = first_tweet['user']['screen_name']
		tweetInfo['tweetID'] = first_tweet['id_str']
		tweetInfo['tweet'] = first_tweet['text']
		return tweetInfo
	else:
		pass


baseTweet = getTweet("@realDonaldTrump")
makeTweet = textGen(taxNouns, freudText)
loadNouns = makeTweet.getNouns()
getSentence = makeTweet.wordSwap(loadNouns)
cleaned = makeTweet.cleanup(getSentence, baseTweet['username'], baseTweet['tweetID'])





