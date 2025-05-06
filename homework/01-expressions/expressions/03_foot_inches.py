""" write a program to convert feets into inches"""

def main():
    feet:float=float(input("Enter the length into feets = "))
    inches:float=feet * 12
    print(f"{feet} fts = {inches} inches")

if __name__=="__main__":
    main()