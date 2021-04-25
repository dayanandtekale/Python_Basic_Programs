#def add(*args):
#    print(sum(args))

#sum(5, 6)   

#def add(*args):
#    print(args[0])
#    print(args[1])
#    print(args[2])

#add(5, 5, 2)



def multi_dynamics(*args):
    print(args)
    sum = 0
    for num in args:
        sum = sum + num
    return sum
print(multi_dynamics(3, 6, 8, 10))  
      

