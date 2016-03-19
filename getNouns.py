import pickle
from textblob import TextBlob
taxText = open('texts/taxidermy.txt', 'r')

nouns=[]

def strip(text):
	for line in text:
		line = line.decode('utf-8').strip()
		blob = TextBlob(line)

		for word, tag in blob.tags:
			if tag == "NN":
				nouns.append(word)


strip(taxText)
with open('taxnouns.p', 'wb') as f:
	pickle.dump(nouns, f)
	f.close()