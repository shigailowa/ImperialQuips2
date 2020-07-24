import nltk

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


if __name__ == '__main__':

	msg = "I like watching netflix, playing football and eating pizza. How about you?"
	split_punct(msg)