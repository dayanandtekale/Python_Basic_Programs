#functions with aeguments and default values

#def multi(a=10, b=20):
#    return a * b
#print(multi(5))



#def area_of_circle(radius, pi=3.14):
#    return pi * radius * radius
#print(area_of_circle(10))    


#def square(a):
#    print(a * a)
#print(square(5))  


#def multi_dynamic(*arge):            #(*------)- [positional args]
#    print(args)
#    mul = 1
#    for arg in args:
#        mul = mul * arg
#    return mul
#print(multi_dynamic(10, 20, 3, 4, 2))        
                   





#multi_dynamic(10, 20, 30, key1='one', key2='two', key3='three', key5='five') 



def multi_dynamic(*args):
    print(args)
    mul = 1
    for arg in args:
        mul = mul * arg
    return mul
print(multi_dynamic(10,  20, 3, 4, 2))        