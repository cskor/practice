from __future__ import print_function
import capitals
import string
import states
import pairs

def game() :
	game = raw_input("States or Capitals? ")
	if game.upper() == "STATES" :
		word = states.states()
	elif game.upper() == "CAPITALS" :
		word =  capitals.capitals()
	else :
		print("You did not say States or Capitals. Sick One.")
		exit()
	length = len(word)
	print("Let's begin our game of Hangman!")
	print("Here is your word: ", end='')
	gameboard = ['_ '] * length
	output(gameboard)
	letters = []
	incorrect = []
	guesses = []
	for i in range(0, length) :
		letters.append(word[i])
	correct = 0
	while(length != correct) :
		guess =raw_input("Guess a letter: ")
		if guess in guesses :
			print("You already guessed that. Try again.")
			continue
		if guess.upper() == "I WANT TO DIE" :
			print("The answer was ", word,". Goodbye.")
			exit()
		if guess.upper() in letters :
			for i in range(0,length) :
				if(guess.upper() == letters[i]) :
					correct = correct + 1
					gameboard[i] = guess.upper()
			output(gameboard)
		else :
			print("Ope. Not in the word.")
			if guess.upper() not in incorrect :
				incorrect.append(guess.upper())
			print("Your incorrect letters are: ", end='')
			output(incorrect)
			print("The current puzzle is: ", end='')
			output(gameboard)
		guesses.append(guess)
	if game.upper() == "STATES" :
		print("Congrats! You solved the puzzle. The state was", word)
	else :	
		pair = pairs.pairs()
		print("Congrats! You solved the puzzle.",word,"is the capital of",pair.get(word))
	tries(len(incorrect))
	if(word.upper() == "SOUTHDAKOTA") :
		print("Lucky you. You got the best state in America.")

def output( list ) :
	for i in range(0, len(list)) :
		print(list[i], " ", end = '')
	print()
	
def tries(count) :
	print("You had",count,"failed guesses.")
	if count == 0 :
		print("Perfection. Is this Cassidy playing?.")
	elif count < 4 :
		print("You are God.")
	elif count < 8 :
		print("You are incredibly average")
	else :	
		print("Brush up on your geography.")

if __name__ == "__main__" :	
	game()
