"""Simulate rolling two dice, and prints results of each roll as well as the total."""
import random

sides:int=6
def main():
    dice1:int=random.randint(1,sides) # generate random integer from 1 to 6
    dice2:int=random.randint(1,6)
    total:int=dice1 + dice2 # sum of dice1 and dice2
    print(f"sum of {dice1} and {dice2 } ==> {total}")

if __name__=="__main__":
    main()