import random
print("Welcome to the Guessing Game!")
print("I have selected number between 1 to 20.")
secret_number=random.randint(1,20)
attempts=0
while True:
    guess=input("Enter your guess: ")
    if not guess.isdigit():
        print("Please enter a number!")
        continue
    guess=int(guess)
    attempts+=1
    if guess < secret_number:
     print("To low try again!")
    elif guess>secret_number:
     print("To high Try again")
    else:
     print("Congrats!. You Guessed it right!")
    print(" The number was",secret_number)
    print("Total attempts",attempts)
    break
