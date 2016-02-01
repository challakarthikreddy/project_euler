'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20? 
'''
elements = range(1,20)
def smallest_multiple():
    count =21 
    print count
    for  i in elements:
        print i
        if count%i==0:
            print count
        else:
            count = count + 1

smallest_multiple()
    
    
