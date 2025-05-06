"""Write a program which prompts the user for an adjective, then a noun, then a verb,
 and then prints a fun sentence with those words!"""

starter_sentence:str="I enjoy learing new things."
def main():
    adjective:str=input("Enter the adjective  =  ")
    noun:str=input("\n Enter the noun  =  ")
    verb:str=input(" \n Enter the verb  = ")
    new_sentence=starter_sentence +" "  +adjective+ " "+ noun +" "+ verb
    print(new_sentence)
    pass

if __name__=="__main__":
    main()