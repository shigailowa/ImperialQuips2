
from message import Message
import nltk

#split Message into subphrases
def split_message(msg):
	return None

#split phrase into parts of speech 
def tag_words(phrase):
	text = nltk.word_tokenize(phrase)
	tags = nltk.pos_tag(text)

	return(tags)

#suggest words to replace given word with
def suggest_replacement(word):
	return None 



def personalise_message():

	phrase = input("Input your message: ")

	tags = tag_words(phrase)

	for index, item in enumerate(tags):
		print(str(index+1) + "." + item[1] + ": " + item[0])


	modification = input("Type 'd' to delete and 'r' to replace a word and 'n' to keep phrase: ")

	if modification == 'd':
		phrase = ""
	elif modification == 'n':
		print(phrase)		
	elif modification == 'r':
		replace_word = input("Choose word to replace: ")
		print("replace word: " + tags[int(replace_word)-1][0])
		#suggest_replacement(tags[replace_word-1][0])



if __name__ == '__main__':

	#msg = "i like to read, play video games and watch netflix. what about you? do you have any hobbies?"
	#phrase = "i like to read, play video games and watch netflix"

	personalise_message()