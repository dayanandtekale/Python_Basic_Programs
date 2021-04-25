def SimpleGenerator():
   
    #this will execute at first call         3in generator we use the "yield" 
    yield "First yield"

    #This will execute at second call
    yield "Second yield"

    #This will execute at Third call
    yield "Third yield"

genC = SimpleGenerator()
print(next(genC))
print(next(genC))
print(next(genC))   


#genC = SimpleGenerator()            #2nd method for printing output directly using for loop
#for i in SimpleGenerator():
#    print(i)