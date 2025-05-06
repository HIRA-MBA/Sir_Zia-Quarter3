"""Print 10 random numbers in the range 1 to 100.

Here is an example run:

45 79 61 47 52 10 16 83 19 12"""
import random

def main():

    for i in range(1,11):
        num=random.randint(1,100) # any random integer from 10to 100
        print(num, end=" ")

if __name__=="__main__":
    main()
     