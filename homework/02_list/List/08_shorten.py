"""Fill out the function shorten(lst) which removes elements from the end of lst, 
which is a list, and prints each item it removes until lst is MAX_LENGTH items long. 
If lst is already shorter than MAX_LENGTH you should leave it unchanged.
 """
import math
import random 
MAX_LENGTH : int = random.randint(1,5)

def shorten(lst):
    while len(lst) > MAX_LENGTH:
        last_elem = lst.pop()
        print(last_elem)

# There is no need to edit code beyond this point

def get_lst():
    """
    Prompts the user to enter one element of the list at a time and returns the resulting list.
    """
    lst = []
    elem = input("Please enter an element of the list or press enter to stop. ")
    while elem != "":
        lst.append(elem)
        elem = input("Please enter an element of the list or press enter to stop. ")
    return lst

def main():
    lst = get_lst()
    shorten(lst)


if __name__ == '__main__':
    main()