"""Write a program that doubles each element in a list of numbers. """


def main():
    numbers: list[int] = [2, 4, 3, 8, 7]  # Creates a list of numbers
    original_numbers = numbers[:]  # Create a copy of the original list
    doubled_numbers = [] # create a new list to store doubled numbers

    for i in range(len(numbers)):  # Loop through the indices of the list
        element_at_index = numbers[i]  # Get the element at index i in the numbers list
        numbers[i] = element_at_index * 2  # Set the element at index i to be equal to the previous element times 2
        doubled_numbers.append(element_at_index * 2) # append the doubled element to the new list
    print(f"\n The {original_numbers} doubles are {doubled_numbers} \n ")  # This should print the doubled list



if __name__ == '__main__':
    main()
