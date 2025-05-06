"""Write a program that displays the terms in the Fibonacci sequence, 
starting with Fib(0) and continuing as long as the terms are less than 10,000"""



def main():
    curr_term = 0  # The 0th Fibonacci Number
    next_term = 1  # The 1st Fibonacci Number
    MAX_TERM_VALUE : int =int(input("Enter the max number to print febonacci series = "))
    
    while curr_term <= MAX_TERM_VALUE:
        print(curr_term)
        term_after_next = curr_term + next_term
        curr_term = next_term
        next_term = term_after_next


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()