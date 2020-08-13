import nltk
import gensim.downloader as api 
from nltk.corpus import wordnet as wn 
import read_files


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
def suggest_replacement(word):
	return(vector_sim(word))


def eval_methods():

	#rg = read_files.read_rg_file()
	#ws = read_files.read_wordsim_file()
	sc = read_files.read_scws_file()

	matches = 0
	####Evaluation of wordnet
	for pos,entry in sc.items():
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

	for key, value in ws.items():
		try:
			sim_words3 = word_vectors.most_similar(key, topn=3)
			sim_words10 = word_vectors.most_similar(key, topn=10)
			for word in sim_words3:
				if word[0] == value:
					matches1 = matches1 + 1

			for word in sim_words10:
				if word[0] == value:
					matches1 = matches2 + 1		
		except:
			pass

	matches3 = 0
	matches4 = 0				
	for key, value in sc.items():
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

	"""


if __name__ == '__main__':

	#word = 'gem'
	#print(suggest_replacement(word))
	#print(wordnet_sim(word,"n"))

	print(eval_methods())