import nltk
import gensim.downloader as api 
from nltk.corpus import wordnet as wn 


#Get similar words from WordNet 
def wordnet_sim(word,pos_tag):

	sim_words = []

	for syn in wn.synsets(word):
		print(syn)
		print(syn.name())
		print(syn.pos())
		print(syn.similar_tos())
	

#Get similar words from Word Embeddings
def vector_sim(word):

	word_vectors = api.load("glove-wiki-gigaword-50")
	sim_words = word_vectors.most_similar(word, topn=3)

	return(sim_words)



#Word Similarity
#suggest words to replace given word with
def suggest_replacement(word):
	return(vector_sim(word))


if __name__ == '__main__':

	word = 'netflix'
	print(suggest_replacement(word))
	#wordnet_sim(word,"JJ")