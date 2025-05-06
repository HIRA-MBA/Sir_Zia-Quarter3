""""Write a program which asks the user how tall they are and prints whether or not they're 
taller than a pre-specified minimum height.

In amusement parks , rollercoasters frequently have minimum height requirements for
 safety reasons."""

def main():
    height:float=float(input("how tall you are in ft = "))
    max_height=5
    if height >= max_height:
        print("you are eligible for all rides")
    elif height >=4:
        print("you are eligible for all rides except roller-coaster and free-fall")
    elif height >=3.5:
        print("you are not eligible for roller-coaster")
    else:
        print("you are only eligible for cars")

if __name__=="__main__":
    main()

     