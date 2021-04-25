#Normal Steps:

a = [10, 2, 67, 89, 32]
b = [2, 3]
print([ele**2 for ele in a if ele%2==0])
print([[ele* ele2 for ele2 in b ] for ele in a])

x=31
if x>=32:print("number is grater than or equal to 32")
print("number is grater than or equal to 32") if x>=32 else print("number i les than 32")

for x in a:
    if x<=32:
        print(x*x)
    else:
        print(x/2)



#Second way list_comprehension:        

a = [10, 2, 67, 89, 32]

print([x*x if x<=32 else x/2 for x in a])