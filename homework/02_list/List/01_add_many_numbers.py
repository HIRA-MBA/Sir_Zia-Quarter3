""" Write a function that takes a list of 
numbers and returns the sum of those numbers."""




def sum(my_list:list):
    sum :int = 0
    for num in my_list:
        sum +=num
    print(f" The sum of {my_list} is {sum}")

sum([4,2,1,5])





