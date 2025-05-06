"""high-Low gAME"""

import random

def main():
    rounds = int(input("How many rounds do you want to play? "))
    count = 1
    score = 0

    while count <= rounds:
        print(f"\nRound {count}:\n")
        
        user_number = random.randint(1, 100)
        computer_number = random.randint(1, 100)
        
        print(f"Your number is {user_number}")
        guess = input("Do you think your number is 'higher' or 'lower' than the computer's? ").strip().lower()
        
        if (guess == "higher" and user_number > computer_number) or \
           (guess == "lower" and user_number < computer_number):
            print(" Your guess is correct!")
            score += 1
        else:
            print("Your guess is wrong.")
        
        print(f"The computer's number was {computer_number}")
        print(f"Current score: {score}/{count}")
        
        count += 1

    print("\n🎮 Game Over!")
    print(f" Your final score: {score} out of {rounds}")

if __name__ == "__main__":
    main()
