
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
	modification = ""
	chunks_output = []
	words = []

	while True:

		for index, item in enumerate(sents):
			print(str(index+1) + ". " + item)#

		modification = input("Type 'd' to delete a sentence, 'm' to modify a sentence: ")

		if modification == 'd':
			sen_del = input("Choose sentence to delete: ")
			sents.pop(int(sen_del)-1) 
			continue
		elif modification == 'm':
			#POS and phrase splitting
			sen_mod = input("Choose sentence to modify: ")
			subsen = sents[int(sen_mod)-1]
			tags = tag_words.tag_words(subsen)
			chunks = split_phrases.split_phrases(tags)
			tags = dict(tags)

			
			for index, chunk in enumerate(chunks):
				temp = ""
				if type(chunk) is nltk.Tree:
					for word,tag in chunk:
						temp = temp + word + " "
					chunks_output.append(temp)
				else:
					temp = chunk[0]
					chunks_output.append(temp)

			while True:

				for index, chunk in enumerate(chunks_output):
					print(str(index+1) + "." + chunk) 

				modification = input("Type 'd' to delete a phrase, 'm' to modify a phrase: ")

				if modification == "d":
					sen_del = input("Choose phrase to delete: ")
					chunks_output.pop(int(sen_del)-1)
					continue
				elif modification == 'm':
					phrase_mod = input("Choose phrase to modify: ")
					#print(chunks_output)
					sub_phrase = chunks_output[int(phrase_mod)-1]

					words = sub_phrase.split()	
					for index, word in enumerate(words):
						print(str(index+1) + "." + word)

					modification = input("Choose word to replace: ")
					word = words[int(modification)-1]
					tag = tags[word]
					sim_words = suggest_replacement.suggest_replacement(word,tag)
					for index, word in enumerate(sim_words):
						print(str(index+1) + "." + word)

					replace = input("Choose replacement word or type in own replacement: ")
					if replace == "1" or replace == "2" or replace == "3":
						words[int(modification)-1] = sim_words[int(replace)-1]
					else:
						words[int(modification)-1] = replace

					sub_phrase = " ".join(words)
					chunks_output[int(phrase_mod)-1] = sub_phrase
					sents[int(sen_mod)-1] = " ".join(chunks_output)

					break
			break			
		
	print("Modified sentence: " + " ".join(sents))

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