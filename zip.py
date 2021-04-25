#syntax:
  #zip(iterables)
listA = [1,4,9,16]
listB = [10,20,40,50]
listC = ['Apple','Ball','Cat','Dog']

#print(list(zip(listA, listB, listC)))

#Column A | Column B | Column C
#1           10        Apple
#4           20        Ball
#9           40        Cat
#16          50        Dog


#1         4      9        16
#10        20     40       50
#Apple    Ball    Cat      Dog

#unzip the list:

zipedList = zip(listA, listB, listC)
print(list(zip(*zipedList)))