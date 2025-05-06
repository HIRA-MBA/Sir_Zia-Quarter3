""" Guess my number """
import random

my_number=random.randint(1,10)
attempt=1

def main():
    print("I am thinking a number from 0 to 10")
    global attempt
    user_number:int=int(input("Enter any number to match my number ==> "))

    while user_number!=my_number:
        if user_number > my_number:
            print("your number is too high")
        else:
            print("your number is too loo")

        attempt +=1

        user_number=int(input("enter another number ==> "))

    print(f"Congrat your guess is correct in {attempt} attempts")
    
if __name__ =="__main__":
    main()   