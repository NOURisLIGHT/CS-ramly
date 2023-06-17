import random

words = ["Monkey", "Giraffe", "Lion", "Dog", "Cat", "Dolphin", "Elephant", "Rhinosorous", "Snake", "Rat"]
word = random.choice(words)

allowed_errors = 7
guesses = []
done = False

while not done:
    for letter in word:
        if letter.lower() in guesses:
            print(letter, end = " ")
        else:
            print("_", end = " ")
        
    print("")
    
    guess = input(f"You have {allowed_errors} lives left! Next guess: ").lower()
    if guess not in guesses:
        guesses.append(guess)
    else:
        while guess in guesses:
            guess = input(f"You chose the letter {guess} before! choose again: ").lower()
    if guess not in word:
        allowed_errors -= 1 
        if allowed_errors == 0:
            break
        
    done = True
    for letter in word:
        if letter.lower() not in guesses:
            done = False
            
if done:
    print(f"Congratulations you won, the word was {word}! ")
else:
    print(f"YOU LOST, the word was {word}! ")
    
