"""Guess My Number

I am thinking of a number between 0 and 99... Enter a guess: 50 Your guess is too high"""

import random
random_number:int=random.randint(1,10) # any number from 1 to 99
attempt:int=1 #  number of attempts


def main():
    global attempt

    user_number:int=int(input("Enter any number from 1 to 10 = "))
    while random_number!=user_number:
     
    
       attempt +=1
       if user_number > random_number:
          print("your guess is too high")
       else :
          print("your guess is too low")

       user_number=int(input("enter a new guess "))
    
    print(f"congratulations your guess is correct in {attempt} attempts")

if __name__=="__main__":
     main()