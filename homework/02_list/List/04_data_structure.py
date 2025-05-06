""" fill out the add_three_copies(...) function which takes a list and some data and then adds three copies of the data to the list. Don't return anything and see what happens! 
Compare this process to the x = change(x) example and note the differences."""




def add_three_copies(my_list, data):
    for i in range(3):
        my_list.append(data)

def change(x):
    x = x + 1
    return x


def main():
    message = input("Enter a message to copy: ")
     # Mutable example
    my_list = []
    print("List before:", my_list)
    add_three_copies(my_list, message)
    print("\n List after:", my_list)

    # Immutable example
    num = 5
    print("\n Before change: num =", num)
    change(num)
    print("\n After change (without reassigning): num =", num)  # Still 5

   

if __name__ == "__main__":
    main()



