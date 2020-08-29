
import split_punct
import tag_words
import split_phrases
import suggest_replacement
import nltk


def personalise_message():

	
	msg = input("Input your message: ")

	sents = split_punct.split_punct(msg)

	loop = True
	##Delete sentence  
	while loop:

		for index, item in enumerate(sents):
			print(str(index+1) + ". " + item)

		modification = input("Do you wish to delete a sentence? (y/n): ")

		if modification == 'y':
			sen_del = input("Choose sentence to delete: ")
			sents.pop(int(sen_del)-1) 
			loop = True
		elif modification == 'n':
			loop = False

	loop = True
	##Modify sentence 
	while loop:

		modification = input("Do you wish to modify a sentence? (y/n): ")

		if modification == 'n':
			loop = False

		elif modification == 'y':

			#POS and phrase splitting
			sen_mod = input("Choose sentence to modify: ")
			subsen = sents[int(sen_mod)-1]
			tags = tag_words.tag_words(subsen)
			chunks = split_phrases.split_phrases(tags)
			tags = dict(tags)

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


			##delete a phrase
			loop2 = True

			while loop2:

				for index, chunk in enumerate(chunks_output):
					print(str(index+1) + "." + chunk) 	

				modification = input("Do you wish to delete a phrase? (y/n): ")

				if modification == 'y':
					sen_del = input("Choose phrase to delete: ")
					chunks_output.pop(int(sen_del)-1)
					loop2 = True
				elif modification == 'n':
					loop2 = False

			##modify a phrase

			loop3 = True

			while loop3:

				modification = input("Do you wish to modify a phrase? (y/n): ")

				if modification == 'n':
					loop3 = False
				elif modification == 'y':

					phrase_mod = input("Choose phrase to modify: ")

					sub_phrase = chunks_output[int(phrase_mod)-1]

					words = sub_phrase.split()	

					loop4 = True

					while loop4:

						for index, word in enumerate(words):
							print(str(index+1) + "." + word)

						modification = input("Choose word to replace or type 'none': ")

						if modification == 'none':
							loop4 = False
						else:
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

					for index, chunk in enumerate(chunks_output):
						print(str(index+1) + "." + chunk) 	


		if loop == True:
			for index, item in enumerate(sents):
				print(str(index+1) + ". " + item)		
		
	print("Modified sentence: " + " ".join(sents))



if __name__ == '__main__':

	personalise_message()