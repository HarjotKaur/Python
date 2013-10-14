print "Time to play a guessing game"
answer=45
game=True
number_of_guesses=0
guess=int(raw_input( 'Enter the number between 1 and 100:'))
number_of_guesses+=1
while (game):
	if (guess < answer):
		guess=input("Too low, try again:") 
		number_of_guesses +=1
		continue
	if (guess > answer):
		guess=input("Too high , try again:") 
		number_of_guesses +=1
		continue
  	if (guess==answer):
  		print ("congratulations you guessed it in %d guesses!!")%(number_of_guesses)
	game=False
 	
