"""The sum of the squares of the first ten natural numbers is,

1**2 + 2**2 + ... + 10**2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first 
ten natural numbers and the square of the sum is 

Find the difference between the sum of the squares of the 
first one hundred natural numbers and the square of the sum."""

class diff():
    def sum_of_square_of_first_hundred_natural_numbers(self):
        count  =0 
        for i in range(1,101):
            count = count + i**2
            
        return  count
    def square_of_sum_of_first_hundred_natural_numbers(self):
        count  =0 
        for i in range(1,101):
            count = count + i
        return count**2    

dif = diff()
sum_of_square = dif.sum_of_square_of_first_hundred_natural_numbers()
square_of_sum = dif.square_of_sum_of_first_hundred_natural_numbers()
            
print square_of_sum-sum_of_square
            