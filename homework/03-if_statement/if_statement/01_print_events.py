""""Write a program that prints the first 20 even numbers. There are several correct 
approaches, but they all use a loop of some sort. Do no write twenty print statements"""

def main():
    for num in range(1,42):
        if num%2 ==0:
            print(num,end=",")


if __name__=="__main__":
    main()