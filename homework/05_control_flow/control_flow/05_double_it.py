"""Write a program that asks a user to enter a number. Your program will then double that number and print out the result. 
It will repeat that process until the value is 100 or greater."""

def main():
    user_input:int=int(input("Enter the number"))
    double_number= user_input * 2
    print(double_number)
    while double_number <=100:
        double_number *=2
        print(double_number )

if __name__=="__main__":
    main()
