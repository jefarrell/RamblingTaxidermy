import twython, sys, random, pickle
from textblob import TextBlob
from twython import TwythonError
from secrets import *

twitter = twython.Twython(C_KEY, C_SECRET, A_TOKEN, A_TOKEN_SECRET)

freudText = open('texts/freud.txt', 'r')
taxNouns = 'taxnouns.p'

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
			line = line.strip()
		 	textHolder += line	
		textHolder.split()
		textHolder = textHolder.decode('utf-8')
		result = TextBlob(textHolder)

		for sentence in result.sentences:
			randSentence = random.choice(result.sentences)
		
		print randSentence
		for word, tag in randSentence.tags:
			if tag == "NN":
				nounCount[random.choice(nounList)] = 0
				temp = random.choice(nounCount.keys())
				if (nounCount[str(temp)]) == 0:
					randSentence = randSentence.replace(word, temp)
				else:
					pass
				nounCount[str(temp)] = 1

	
		print randSentence
		
		######
		# sentenceString.split()
		# sentenceString = sentenceString.decode('utf-8')
		# corpus = TextBlob(sentenceString)
		# swapOutput = random.choice(corpus.sentences)
		# return swapOutput
		#should have another function for analyzing and cleaning here



tweetInfo = {'username': "", 'usernameID': "", 'tweet': ""}

def getTweet(query):
	response = twitter.search(q=query, result_type='recent', lang = 'en', count=1)
	if len(response['statuses']) > 0:
		first_tweet = response['statuses'][0]
		tweetInfo['username'] = first_tweet['user']['screen_name']
		tweetInfo['usernameID'] = first_tweet['id_str']
		tweetInfo['tweet'] = first_tweet['text']
		print tweetInfo
		print len(tweetInfo['username'])
	else:
		pass


getTweet("@realDonaldTrump")
generate = textGen(taxNouns, freudText)
output1 = generate.getNouns()
output2 = generate.wordSwap(output1)
# fixer = output2[14:]
# advice = (fixer[:120]) if len(fixer) > 120 else fixer
# print advice




# try:
# 	twitter.update_status(status= "@" + target + " " + advice, in_reply_to_status_id=targetID)
# except TwythonError as e:
# 	print e



