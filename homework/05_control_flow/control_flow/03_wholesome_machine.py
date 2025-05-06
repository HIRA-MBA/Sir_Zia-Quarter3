"""Write a program which prompts the user to type an affirmation of your choice 
(we'll use "I am capable of doing anything I put my mind to.") until they type it correctly."""

affirmation="I am capable of doing anything I put my mind to"

def main():
   print("Enter the following statement correctly ==> \n",affirmation)

   user_input=input()

   while user_input != affirmation:  # While the user's input isn't the affirmation
        # Tell the user that they did not type the affirmation correctly
        print("That was not the affirmation.")

        # Ask the user to type the affirmation again!
        print("Please try again.\n Type the following affirmation:\n " + affirmation)
        user_input = input()

   print("That's right! :)")

if __name__ =="__main__":
    main()