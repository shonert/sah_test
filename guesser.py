#!/usr/bin/env python
"""guesser.py, by Shaun Hutchinson, 2017-07-08
This program has the user guess a number between 1 and 100
"""
import random

def main():
	print ("Guess a number between 1 and 100.")
	randomNumber = random.randint(1,100)
	found = False #flag variable if they guess it
	numberOfGuesses = 0

	while not found:
		guessIsNumber = False #flag var to make sure guess is number
		guessIsInBoundary = False #flag var to make sure guess is in specified boundaries

		userGuess = input("Your guess: ")
		guessIsNumber = isGuessNumber(userGuess)
		numberOfGuesses = numberOfGuesses + 1
		
		if guessIsNumber == True:
			userGuess = int(userGuess)
			guessIsInBoundary = isGuessInBoundaries(userGuess,1,100)
			if guessIsInBoundary == True:
				found = checkGuess(int(userGuess),randomNumber)

	print ("Congrats, You solved this in " + str(numberOfGuesses) + " guesses")

def isGuessNumber(guess):
	try:
		guess = int(guess)
		return True
	except ValueError:
		print("That is not a number, try again.")
		return False

def isGuessInBoundaries(guess,startBoundary,endBoundary):
	if guess < startBoundary:
		print ("Your guess is below the boundary, please try a number between 1 and 100.")
		return False
	elif guess > endBoundary:
		print ("Your guess is above the boundary, please try a number between 1 and 100.")
		return False
	else:
		return True

def checkGuess(guess,randomNumber):
	if guess == randomNumber:
		print ("You got it!")
		return True
	elif guess > randomNumber:
		print ("Guess lower")
		return False
	else:
		print ("Guess Higher")
		return False


if __name__ == "__main__":
	main()	