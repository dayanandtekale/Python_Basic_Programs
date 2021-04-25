a = [4,6,1,9,11]
#max_number = max(a)
#    print("max(a)")
#    print(max(a))
max_number = a[0]
for number in a:
    if number>max_number:
        max_number = number
        print (max_number)
