import nltk

#Sentence Segmentation
#split Message into subphrases 
#according to puctuation
def split_punct(msg):

   	#use nltk sentence tokenizer first
	sents = nltk.sent_tokenize(msg)
	
	#then split additionally on commas
	final_sents = []

	for sent in sents:

		sent = sent.split(",")

		for index, item in enumerate(sent[:-1]):
			sent[index] = item + ","

		for item in sent:
			final_sents.append(item)

	return final_sents 


if __name__ == '__main__':

	msg = "I like watching netflix, playing football and eating pizza. How about you?"
	print(split_punct(msg))