from math import sqrt

# Function to Check the Prime Number
def is_prime(number:int):
   if number <= 1:
      print("Not a prime number")
      return
   for i in range(2,round(sqrt(number))+1):
      if number % i == 0:
        print("Not Prime Number")
        return
   print("Prime Number")

