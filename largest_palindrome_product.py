# coding=utf-8
""" A palindromic number reads the same both ways. The largest palindrome made 
from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers."""

# class palindrome_product():
#     count_1 = 999
#     def max_palindrom(self):
#         while True:
#             
#             self.count_1 = self.count_1 -1
#             
#             
#         
#         
# obj = palindrome_product()
# obj.max_palindrom()



# def _chkpalindrome(str):
#     for i in xrange(len(str)/2):
#         if(int(str[i]) !=int(str[len(str)-1-i])):
#             return False
#     return True
# 
# def multiplyNumbers(i,j):
#         if (isinstance(i, int) and isinstance(j, int)):
#             if(_chkpalindrome(str(i * j))):
#                 print i," * ",j," = ",i*j
#                 return None
#             if(j > 900):
#                 multiplyNumbers(i,j-1)
#             else:
#                 if(i > 900):
#                     j = 999
#                     multiplyNumbers(i-1,j)
#         return None
# 
# multiplyNumbers(999,999)



def _chkpalindrome(str):
    for i in xrange(len(str)/2):
        if(int(str[i]) !=int(str[len(str)-1-i])):
            return False
    return True

def multiplyNumbers(i,j):
        if (isinstance(i, int) and isinstance(j, int)):
            if(_chkpalindrome(str(i * j))):
                print i," * ",j," = ",i*j
                return None
            if(j > 900):
                multiplyNumbers(i,j-1)
            else:
                if(i > 900):
                    j = 999
                    multiplyNumbers(i-1,j)
        return None

multiplyNumbers(999,999)