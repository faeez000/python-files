import random
print("Hey What is Your name?")
name = input()
print("Wlcome" +name+ "to the guessing game")
secret_number = random.randint(1,20)
print ("Now guess the number between 1 and 20")



for guess_number in range(1,7):
    guess = int(input())
    if guess < secret_number:
        print("Guess number is to Low")
    elif  guess > secret_number:
        print("Guess number is to High")
    else:
        break

if guess == secret_number:
    print("Good Job!!" +name+ "You have guess the correct number in" +str(guess_number)+ "guesses")
else:
    print("Sorry" +name+ "You Have failed to guess the number. The Correct number was" +str(secret_number))
