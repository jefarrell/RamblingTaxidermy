from textblob import TextBlob
import random
import time
import twython
from twython import TwythonError
import sys


api_key, api_secret, access_token, token_secret = sys.argv[1:]
twitter = twython.Twython(api_key, api_secret, access_token, token_secret)

nouns = []
adjective = []
marriageText = open('marriage.txt', 'r')
taxText = open('taxidermy.txt', 'r')


class textGen(object):
	def __init__(self, text1, text2):
		self.text1 = text1
		self.text2 = text2


	def strip(self):
		for line in self.text1:
			line = line.decode('utf-8').strip()
			blob = TextBlob(line)

			for word, tag in blob.tags:
				if tag == "NN":
					nouns.append(word)


	def wordSwap(self):
		textIn = ""
		placeholder = []

		for line in self.text2:
			line = line.strip()
			textIn += line + " "
		textIn.split()
		textIn = textIn.decode('utf-8')
		result = TextBlob(textIn)

		for sentence in result.sentences:
			for word, tag in sentence.tags:
				if tag == "NN":
					sentence = sentence.replace(word, random.choice(nouns))
			placeholder.append(sentence)

		stringTest = str(placeholder)
		
		stringTest.split()
		stringTest = stringTest.decode('utf-8')
		corpus = TextBlob(stringTest)
		swapOutput = random.choice(corpus.sentences)
		return swapOutput
		

generate = textGen(taxText, marriageText)
output1 = textGen.strip(generate)
output2 = str(textGen.wordSwap(generate))
fixer = output2[14:]
advice = (fixer[:120]) if len(fixer) > 120 else fixer
print advice

response = twitter.search(q="marriage", result_type='recent', lang = "en", count=1)
if len(response['statuses']) > 0:
	first_tweet = response['statuses'][0]
	target = first_tweet['user']['screen_name']
	targetID = first_tweet[u'id_str']
	
else:
	
	print line
time.sleep(0.5)


try:
	twitter.update_status(status= "@" + target + " " + advice, in_reply_to_status_id=targetID)
except TwythonError as e:
	print e
