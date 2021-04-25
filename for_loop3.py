#list1 = [[[45, 67, 27], [92, 30, 71]],

        [[91, 54, 67], [28, 71, 45]],

        [[91, 54, 67], [92, 30, 71]]]
#for item in list1:                        #1st method
#    print(item)
#    for inneritem in list1[6]:
#        print(inneritem)        


#for idx, item in enumerate(list1):       #next method
#    if isinstance(item, list):
#        for inneritem in item:
#           print(inneritem)
#    else:
#        print(item)    


a = [45, 67, 27, 92, 30, 71]              #next method
b = [91, 54, 67, 28, 71,45]

#for item in a:                         
#    for itemb in b:
#        if itema == itemb:
#            print(itema)


#for item in a:                         
#    for itemb in b:
#        print(itema)


for item in b:                         
    if not  itemb in a:
        print(itemb)


#print(set(a).intersection(set(b)))