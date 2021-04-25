#generators type1

#def cube_generator(n):
#    for i in n:
#        return i**3
      
        

#print(cube_generator([1,2,3,4,5]))
#genC = cube_generator([1,2,3,4,5]).......#due to return function loop not iterate ,so the op of program is 1



def cube_generator(n):
    for i in n:
        yeild (i**3)
      
genC = cube_generator([1,2,3,4,5])

print(next(genC))
print(next(genC))
print(next(genC))
print(next(genC))
print(next(genC))  

#for num in genC:
#    print(num)      
