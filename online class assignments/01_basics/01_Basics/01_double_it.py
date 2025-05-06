"""Write a program that asks a user to enter a number. Your program will then double that number and print out the result. It will repeat that process until the value is 100 or greater.

For example if the user enters the number 2 you would then print:

4 8 16 32 64 128"""

def main():
    user_number=int(input("enter the number from where doubles are required ==> "))
    max_number=int(input("enter the max number for double number ==> "))
    double_number = user_number * 2
    print(double_number)

    while double_number < max_number:
        double_number *=2
        print(double_number)

if __name__=="__main__":
    main()