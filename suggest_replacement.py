import nltk
import gensim.downloader as api 
from nltk.corpus import wordnet as wn 
import read_files
import re
import random
from wiki_ru_wordnet import WikiWordnet


#Get similar words from WordNet 
def wordnet_sim(word,pos_tag):

	sim_words = []

	wv_tag = ""

	if pos_tag == r"N.*" or pos_tag =='n':
		wv_tag = "n"
	elif pos_tag == r"V.*" or pos_tag =='v':
		wv_tag = "v"
	elif pos_tag == "JJ" or pos_tag == "RB" or pos_tag == 'a':
		wv_tag = "a"

	for i in range(1,10):
		try:
			for lemma in wn.synset(word+'.'+wv_tag+'.'+'0'+str(i)).lemma_names():
				sim_words.append(lemma)
		except:
			pass

	return(sim_words)
		
	

#Get similar words from Word Embeddings
def vector_sim(word):

	word_vectors = api.load("glove-wiki-gigaword-50")
	sim_words = word_vectors.most_similar(word, topn=3)

	return(sim_words)



#Word Similarity
#suggest words to replace given word with
def suggest_replacement(word,pos_tag):
	
	sim_words = []

	wv_tag = ""

	if re.match(r"N.*",pos_tag):
		wv_tag = "n"
	elif re.match(r"V.*",pos_tag):
		wv_tag = "v"
	elif pos_tag == "JJ" or pos_tag == "RB":
		wv_tag = "a"

	#print(wv_tag)	

	for i in range(1,10):
		try:
			lemmas = wn.synset(word+'.'+wv_tag+'.'+'0'+str(i)).lemma_names()
		except:
			continue
		while len(sim_words) < 3 and lemmas:
			r = random.randint(0,len(lemmas)-1)
			if (lemmas[r] != word):
				sim_words.append(lemmas[r])
			lemmas.pop(r)


	return(sim_words)

def eval_methods():

	
	rg = read_files.read_rg_file()
	ws = read_files.read_wordsim_file()
	#sc = read_files.read_scws_file()
	#sl = read_files.read_simlex_file()

	"""
	matches = 0
	####Evaluation of wordnet
	for pos,entry in sl.items():
		for key, value in entry.items():
			sim_words = wordnet_sim(key,pos)
			for word in sim_words:
				if word == value:
					matches = matches+1

	return(matches)
	"""

	
	###Evaluation of embeddings
	word_vectors = api.load("glove-wiki-gigaword-50")
	#word_vectors = api.load("word2vec-google-news-300")

	matches1 = 0
	matches2 = 0
	#for pos, entry in ws.items():
	for key, value in rg.items():
		try:
			sim_words3 = word_vectors.most_similar(key, topn=3)
			sim_words10 = word_vectors.most_similar(key, topn=10)
			for word in sim_words3:
				if word[0] == value:
					matches1 = matches1 + 1

			for word in sim_words10:
				if word[0] == value:
					matches2 = matches2 + 1		
		except:
			pass

	
	matches3 = 0
	matches4 = 0				
	for key, value in ws.items():
		try:
			sim_words3 = word_vectors.most_similar(key, topn=3)
			sim_words10 = word_vectors.most_similar(key, topn=10)
			for word in sim_words3:
				if word[0] == value:
					matches3 = matches3 + 1

			for word in sim_words10:
				if word[0] == value:
					matches4 = matches4 + 1
		except:
			pass
	

	matches = [matches1,matches2,matches3,matches4]
	return(matches)


def eval_rus():

	simlex = read_files.read_simlex_rus_file()
	wordsim = read_files.read_wordsim_rus_file()

	wn = WikiWordnet()

	"""
	#evaluation of wordnet
	matches = 0
	for key,value in wordsim.items():
		synset = wn.get_synsets(key)
		for syn in synset:
			for w in syn.get_words():
				word = w.lemma()
				if value == word:
					matches = matches + 1
	"""

	#evaluation of word vectors 
	word_vectors = api.load('word2vec-ruscorpora-300')

	matches1 = 0
	matches2 = 0
	matches3 = 0
	matches4 = 0

	for key, value in simlex.items():
		try: 
			sim_words3 = word_vectors.most_similar(key+'_NOUN', topn=3)
			sim_words10 = word_vectors.most_similar(key+'_NOUN', topn=10)
		except:
			try:
				sim_words3 = word_vectors.most_similar(key+'_VERB', topn=3)
				sim_words10 = word_vectors.most_similar(key+'_VERB', topn=10)
			except:
				try:
					sim_words3 = word_vectors.most_similar(key+'_ADJ', topn=3)
					sim_words10 = word_vectors.most_similar(key+'_ADJ', topn=10)
				except:
					continue

		#print(sim_words10)
		for word in sim_words3:
			if word[0].split('_')[0] == value:
				matches1 = matches1 + 1

		for word in sim_words10:
			if word[0].split('_')[0] == value:
				matches2 = matches2 + 1		



	for key, value in wordsim.items():
		try: 
			sim_words3 = word_vectors.most_similar(key+'_NOUN', topn=3)
			sim_words10 = word_vectors.most_similar(key+'_NOUN', topn=10)
		except:
			try:
				sim_words3 = word_vectors.most_similar(key+'_VERB', topn=3)
				sim_words10 = word_vectors.most_similar(key+'_VERB', topn=10)
			except:
				try:
					sim_words3 = word_vectors.most_similar(key+'_ADJ', topn=3)
					sim_words10 = word_vectors.most_similar(key+'_ADJ', topn=10)
				except:
					continue

		for word in sim_words3:
			if word[0].split('_')[0] == value:
				matches3 = matches3 + 1

		for word in sim_words10:
			if word[0].split('_')[0] == value:
				matches4 = matches4 + 1		
			

	return [matches1, matches2, matches3, matches4]


if __name__ == '__main__':

	#word = 'talk'
	#print(suggest_replacement(word,'VBZ'))
	#print(wordnet_sim(word,"n"))
	print(eval_methods())
	#print(eval_methods())