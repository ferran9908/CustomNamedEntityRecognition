from flask import Flask,jsonify,request
import spacy
import json

from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
app = Flask(__name__)



def removeStopWords(text):

	stop_words = ['a',
	 'about',
	 'above',
	 'after',
	 'again',
	 'against',
	 'ain',
	 'all',
	 'am',
	 'an',
	 'and',
	 'any',
	 'are',
	 'aren',
	 "aren't",
	 'as',
	 'at',
	 'be',
	 'because',
	 'been',
	 'before',
	 'being',
	 'below',
	 'between',
	 'both',
	 'but',
	 'by',
	 'can',
	 'couldn',
	 "couldn't",
	 'd',
	 'did',
	 'didn',
	 "didn't",
	 'do',
	 'does',
	 'doesn',
	 "doesn't",
	 'doing',
	 'don',
	 "don't",
	 'down',
	 'during',
	 'each',
	 'few',
	 'for',
	 'from',
	 'further',
	 'had',
	 'hadn',
	 "hadn't",
	 'has',
	 'hasn',
	 "hasn't",
	 'have',
	 'haven',
	 "haven't",
	 'having',
	 'he',
	 'her',
	 'here',
	 'hers',
	 'herself',
	 'him',
	 'himself',
	 'his',
	 'how',
	 'i',
	 'if',
	 'in',
	 'into',
	 'is',
	 'isn',
	 "isn't",
	 'it',
	 "it's",
	 'its',
	 'itself',
	 'just',
	 'll',
	 'm',
	 'ma',
	 'me',
	 'mightn',
	 "mightn't",
	 'more',
	 'most',
	 'mustn',
	 "mustn't",
	 'my',
	 'myself',
	 'needn',
	 "needn't",
	 'nor',
	 'now',
	 'o',
	 'of',
	 'off',
	 'on',
	 'once',
	 'only',
	 'or',
	 'other',
	 'our',
	 'ours',
	 'ourselves',
	 'out',
	 'over',
	 'own',
	 're',
	 's',
	 'same',
	 'shan',
	 "shan't",
	 'she',
	 "she's",
	 'should',
	 "should've",
	 'shouldn',
	 "shouldn't",
	 'so',
	 'some',
	 'such',
	 't',
	 'than',
	 'that',
	 "that'll",
	 'the',
	 'their',
	 'theirs',
	 'them',
	 'themselves',
	 'then',
	 'there',
	 'these',
	 'they',
	 'this',
	 'those',
	 'through',
	 'to',
	 'too',
	 'under',
	 'until',
	 'up',
	 've',
	 'very',
	 'was',
	 'wasn',
	 "wasn't",
	 'we',
	 'were',
	 'weren',
	 "weren't",
	 'what',
	 'when',
	 'where',
	 'which',
	 'while',
	 'who',
	 'whom',
	 'why',
	 'will',
	 'with',
	 'won',
	 "won't",
	 'wouldn',
	 "wouldn't",
	 'y',
	 'you',
	 "you'd",
	 "you'll",
	 "you're",
	 "you've",
	 'your',
	 'yours',
	 'yourselves']
	word_tokens = word_tokenize(text)
	filtered_sentence = [w for w in word_tokens if not w in stop_words]
	filtered_sentence = []
	for w in word_tokens:
		if w not in stop_words:
			filtered_sentence.append(w)
	return filtered_sentence

  


@app.route('/api/flaskcall',methods=['POST'])
def transform_text():
	print('TEXT: ')
	k = request.get_json()
	print(len(k))
	print(k);
	res = []
	for item in k:
		it = k["text"].lower()

		dic={}
		nlp2 = spacy.load("./DiseasesModel")


		doc = nlp2(it)
		for ent in doc.ents:
			dic[ent.label_]=ent.text
		# 	r=['']
		# 	print(ent.text)
		# 	f=removeStopWords(ent.text)
		# 	r.append(f)
		# dic[ent.label_]=r
	    
		nlp2 = spacy.load("./MedicineModel")
		doc = nlp2(it)
		for ent in doc.ents:
			dic[ent.label_]=ent.text
		# 	r=['']
		# 	f=removeStopWords(ent.text)
		# 	r.append(f)
		# dic[ent.label_]=r
		nlp2 = spacy.load("./SymptomsModel")
		doc = nlp2(it)
		for ent in doc.ents:
			dic[ent.label_]=ent.text
			
		# 	r=['']
		# 	f=removeStopWords(ent.text)
		# 	r.append(f)
		# dic[ent.label_]=r
		res.append(dic)
	return jsonify({"response":dic})



    	