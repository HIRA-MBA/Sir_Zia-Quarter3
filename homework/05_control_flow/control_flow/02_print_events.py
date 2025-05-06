"""Write a program that prints the first 20 even numbers. There are several correct
 approaches, but they all use a loop of some sort. Do no write twenty print statements"""


def main():
   count =1
   num=0

   while count <=20:
       
         if num % 2 ==0:
            print(num, end=",")
            count+=1
         num+=1

if __name__=="__main__":
    main()