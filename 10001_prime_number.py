count = 1
for num in range(2,10000000):
    prime = True
    for i in range(2,num):
        if (num%i==0):
            prime = False
    if prime:
        count = count +1
        print str(num) + '-----' + str(count) +'st prime'