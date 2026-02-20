import random

def guess_the_number():
    """
    A simple number guessing game where the user tries to guess a number
    randomly selected by the computer.
    """
    secret_number = random.randint(1, 100) 
    guess = 0
    attempts = 0
    tot_att = 10

    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100.")

    while (guess != secret_number) :
        try:
            guess_str = input("Enter your guess: ")
            guess = int(guess_str)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue 

        attempts += 1


        if guess < secret_number:
            print("Too low, try a higher number.")
        elif guess > secret_number:
            print("Too high, try a lower number.")
            
        tot_att= tot_att-1
        print(f"You have {tot_att} tries left")
        
        if(tot_att == 0):
            print("You have run out of tries! The number is :" + secret_number)
        
    print(f"Congratulations! You guessed the correct number {secret_number} in {attempts} attempts!")
if __name__ == "__main__":
    guess_the_number()
