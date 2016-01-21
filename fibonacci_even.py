def fib(n):
    a,b = 1,1
    l=[]
    while a<4000000:
        a,b = b,a+b
        print str(a) + '\n'
        print 'length of value is'+str(len(str(a)))
        if a%2 ==0:
            l.append(a)            
    return sum(l)
 
print fib(4000000)

# def fib_new():
#     x,y = 0,1
#     while True:
#         yield x
#         x,y = y, x+y
#  
# def even(seq):
#     for number in seq:
#         if not number % 2:
#             yield number
#  
# def under_a_million(seq):
#     for number in seq:
#         if number > 4000000:
#             break
#         yield number   
#  
# print sum(even(under_a_million(fib_new())))
# 
# 
# class Test(object):
#     def TestFib(self):
#         a = 1
#         b = 2
#         c = 0
#         sum = 0
#         while(a < 4000000):
#             c = a + b
#             a = b
#             b = c
#             if a % 2 == 0:
#                 sum = sum + a
#         print sum
#  
# if __name__ == '__main__':
#     test = Test()
#     test.TestFib()
#     
# 
# 
#  
# def calcE():
#     x = y = 1
#     sum = 0
#     while (sum < 4000000):
#         sum += (x + y)
#         x, y = x + 2 * y, 2 * x + 3 * y
#     return sum
#   
# print calcE()



