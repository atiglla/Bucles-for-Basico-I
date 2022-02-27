for i in range (151):
    print (i)

for i in range (5, 5001, 5):
    print(i)

for i in range (1,101):
    if i%10==0:
        print ("Coding Dojo")
    elif i%5==0:
        print("Coding")
    else: print(i)

sumafinal=0
for i in range(0,501):
    if i%2==1:
        sumafinal+=i
print(sumafinal)       

for i in range (2018, 0, -4):
    print(i)

lowNum=2
highNum=9
mult=3

for i in range (lowNum,highNum+1):
    if i%mult==0:
        print (i)
