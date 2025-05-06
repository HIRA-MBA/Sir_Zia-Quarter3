"""Ask the user for two numbers, one at a time, and then print the result of dividing the first number by the second and also the remainder of the division.

"""

def main():
    dividened=int(input("please enter the dividend "))
    divisor=int(input("Please enter the divisor "))
    
    remainder=float(dividened % divisor)
    quotient=float(dividened / divisor)
    print(f"\n {dividened} / {divisor} the quotient is {quotient} and remainder is {remainder}")


if __name__=="__main__":
    main()