#num = -10
#while(num<10):
#    if num%2==0:
#        print("even number "+ str(num))
#    else:
#        print("odd number "+ str(num))
#    num = num + 1

#import time
#num = 10
#end = num * 10
#while(num<=num * 10):
#    print(num, num * 10)
#    time.sleep(1)
#    num = num + 10

#a = [30, 54, 67, 12, 89, 45]
#i = 0 #initialization\value assignment
#length = len(a)
#while(i < length):  #condition check
#    print(a[i])
#    i += 1  #stride\step

a = {'A' :30, 'B':54, 'C':67, 'D':12, 'E':89, 'F':45}

b = list(a.keys())

i = 0 #initialization / value assignment 
length = len(b)
while(i < length):  #condition check
   print(a[b[i]])
   i += 1  #stride / step