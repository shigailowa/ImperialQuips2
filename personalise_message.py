
import split_punct
import tag_words
import split_phrases
import suggest_replacement
import nltk


def personalise_message():

	
	msg = input("Input your message: ")


	#gets updated after each modification
	final_output = ""

	sents = split_punct.split_punct(msg)

	for index, item in enumerate(sents):
		print(str(index+1) + ". " + item)


	modification = input("Type 'd' to delete a sentence, 'm' to modify a sentence and 'n' to do nothing: ")

	if modification == 'd':
		sen_del = input("Choose sentence to delete: ")
		final_output = sents.pop(int[sen_del]-1)
	elif modification == 'm':
		#POS and phrase splitting
		sen_mod = input("Choose sentence to modify: ")
		subsen = sents[int(sen_mod)-1]
		tags = tag_words.tag_words(subsen)
		chunks = split_phrases.split_phrases(tags)

		chunks_output = []
		for index, chunk in enumerate(chunks):
			temp = ""
			if type(chunk) is nltk.Tree:
				for word,tag in chunk:
					temp = temp + word + " "
				chunks_output.append(temp)
			else:
				temp = chunk[0]
				chunks_output.append(temp)

			print(str(index+1) + "." + temp)

		modification = input("Type 'd' to delete a phrase, 'm' to modify a phrase and 'n' to do nothing: ")

		if modification == 'm':
			sen_mod = input("Choose phrase to modify: ")
			print(chunks_output)
			sub_phrase = chunks_output[int(sen_mod)-1]

			words = sub_phrase.split()	
			for index, word in enumerate(words):
				print(str(index+1) + "." + word)

			modification = input("Choose word to replace: ")
			word = words[int(modification)-1]
			sim_words = suggest_replacement.suggest_replacement(word)
			for index, word in enumerate(sim_words):
				print(str(index+1) + "." + word[0])


	#print(split_phrases(msg))




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