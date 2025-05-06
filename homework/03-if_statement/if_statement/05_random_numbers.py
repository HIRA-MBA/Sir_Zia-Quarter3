"""Print 10 random numbers in the range 1 to 100.

Here is an example run:

45 79 61 47 52 10 16 83 19 12

Each time you run your program you should get different numbers"""
import random
max_limit=100
min_limit=1
numbers_to_print=11

def main():
    for i in range(1,numbers_to_print): 
        num=random.randint(min_limit,max_limit)
        print(num,end=",")

if __name__=="__main__":
    main()