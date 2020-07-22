
from message import Message
import nltk
import gensim.downloader as api 
from nltk.corpus import wordnet as wn


#Sentence Segmentation
#split Message into subphrases 
#according to puctuation
def split_punct(msg):

   	#use nltk sentence tokenizer first
	sents = nltk.sent_tokenize(msg)
	#return sents 

	
	#then split additionally on commas and semicolons
	seps = [',',';']
	default_sep = seps[0]

	final_sents = []

	for sent in sents:
		for sep in seps[1:]:
			sent = sent.replace(sep,default_sep)

		sent = sent.split(default_sep)

		for item in sent:
			final_sents.append(item)

	return final_sents 
	


#Part-of-Speech Tagging
#split phrase into parts of speech 
def tag_words(phrase):
	text = nltk.word_tokenize(phrase)
	tags = nltk.pos_tag(text)
	#trigram = nltk.TrigramTagger(training data)
	#tags = trigram.tag(phrase)

	return tags

#Word Similarity
#suggest words to replace given word with
def suggest_replacement(word):

	#GloVe Vectors, cosine similarity
	word_vectors = api.load("glove-wiki-gigaword-50")
	sim_words = word_vectors.most_similar(word,topn=3)

	#WordNet
	sim_words_wn = []

	for syn in wn.synsets(word):
		for l in syn.lemmas():
			sim_words_wn.append(l)


	return sim_words


def personalise_message():

	
	msg = input("Input your message: ")


	#gets updated after each modification
	final_output = ""

	"""
	sents = split_punct(msg)

	for index, item in enumerate(sents):
		print(str(index+1) + ". " + item)

	modification = input("Type 'd' to delete a sentence, 'm' to modify a sentence and 'n' to do nothing: ")

	if modification == 'd':
		sen_del = input("Choose sentence to delete: ")
		final_output = sents.pop(int[sen_del]-1)
	elif modification == 'm':
		sen_mod = input("Choose sentence to modify: ")
		#TODO: phrase segmentation
	"""

	print(split_phrases(msg))




	"""
	phrase = input("Input your phrase: ")
	
	tags = tag_words(phrase)

	for index, item in enumerate(tags):
		print(str(index+1) + ". " + item[1] + ": " + item[0])


	modification = input("Type 'd' to delete, 'r' to replace a word and 'n' to keep phrase: ")

	if modification == 'd':
		phrase = ""
	elif modification == 'n':
		print(phrase)		
	elif modification == 'r':
		replace_word = input("Choose word to replace: ")
		print("replace word: " + tags[int(replace_word)-1][0])
		#suggest_replacement(tags[replace_word-1][0])
	"""
	

	"""
	word = input("Input word: ")
	replacement = suggest_replacement(word)
	print(replacement)
	"""


if __name__ == '__main__':

	#msg = "i like to read, play video games and watch netflix. what about you? do you have any hobbies?"
	#phrase = "i like to read, play video games and watch netflix"

	personalise_message()