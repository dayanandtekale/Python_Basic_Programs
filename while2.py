#num = -10
#while(num<10):
#    if num%2==0:
#        print("even number "+ str(num))
#    else:
#        print("odd number "+ str(num))
#    num = num + 1        

import time
num = 10
end = num * 10
while(num<=end):
    print(num, end)
    time.sleep(1)
    num = num + 10