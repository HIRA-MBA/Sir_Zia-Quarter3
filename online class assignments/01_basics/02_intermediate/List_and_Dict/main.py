# List Problems
"""# Print the length of the list.
# Add 'mango' at the end of the list
# Print the updated list."""

def List():
    print("\n Problem #1: List Practice \n ")
    fruits:list=["apple","banana","grapes","orange","pineapple"]
    print(f" \n the list contains {len(fruits)} elements")
    # adding mango at end
    fruits.append("mango")
    # updated list
    print(f"\n the updated list is {fruits}")



def index_game(lst: list, index: int):
    try:
        print(f'the item on {index} index is = ', lst[index], "\n")
    except IndexError:
        print("Error: Index does not exist")




def main():
    print("Hello from list-and-dict!")
    List()
    print("\n ##########\n\n")
    print("\n\n Problem no: accessing the index element \n\n")
    index_game(["hi","buy","bi","my","tie"],2)


if __name__ == "__main__":
    main()
