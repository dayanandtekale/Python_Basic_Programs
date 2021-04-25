# Parent  -Child
# Super   -Sub
# Base    -Child

# 5 Types of Inheritance in OOP:

#CHILD class which access the data of PARENT class but, PARENT class can not access the data of PARENT class

#Single Level Inheritance:[in which single parent and only one child class is prasent]
#class Parent:
#    def function_parent(self):
#        print("Parent Class")

#class Child(Parent):
#    def function_child(self):
#        print("Child Class")
#objChild = Child()
#objChild.function_parent()
#objChild.function_child()    


##Multi Level inheritance:
##[in which 2 parents r prasent for child class (child will be only 1) i.e. Grandparent & Father ]

#class GrandParent:
#    def __int__(self, grandname):
#        self.grandname = grandname

#class Father(GrandParent):
#    def __init__(self, fathername, grandname):
#        self.fathername = fathername

#        #GrandParent>__init__(self, grandname)

#class Child(Father):
#    def __init__(self, childname, fathername, grandname):
#        self.childname = childname

#        Father.__init__(self, fathername, grandname)

#    def print_name(self):
#        print("GrandParent Name = " + self.grandname)
#        print("Father Name = " + self.fathername) 
#        print("Child Name = " + self.childname)

#1)father = Father('PQR', 'ABC')
#1)print(father.fathername, father.grandname)

#2)child = Child('XYZ', 'PQR', 'ABC')
#child.print_name()
#print(child.grandname)


#Multiple Inheritance
#[In which the Parents class are 2 or more but , Child class will be only 1]

#class Father:
#    fathername = ""


    #1)def father_name(self):              //#1st method 1)
        #1)print(self.fathername)
#    def father_name(self, fathername):      #2nd method 
#        print(fathername)    

#class Mother:
#    mothername = ""
    #1)def mother_name(self):
        #1)print(self.mothername)
#    def mother_name(self, mothername):
#        print(mothername)   

#class Child(Father, Mother):
#    def function(self):
        #1)print("Father Name is = "+self.fathername)
        #1)print("Mother Name is = "+self.mothername)
#        print("Father Name is = "+self.fathername)
#        print("Mother Name is = "+self.mothername)

#child = Child()

#1)child.fathername = "XYZ"
#1)child.mothername = "PQR"
#1)child.function()                        

#child.father_name("XYZ")
#child.mother_name("PQR")



#Hirachical Inheritance:
#[More than one class is Inherited from a single parent ]

#class Car():
#    #1)def Speed(self, HP, volume, name):
#    def Speed(self, HP, volume):
#        #1)print(name+" Speed is " + str(HP*volume))
#        print(self.name+" Speed is " + str(HP*volume))

#class BMW(Car):
#    name = "BMW"
#    def Color(self):
#        print("BMW's Color is Black")

#class Audi(Car):
#    name = "Audi"
#    def Type(self):
#        print("Audi's Sport Car")

#bmw = BMW()
#audi = Audi()
#bmw.Speed(2, 600, BMW.name)
##1)bmw.Speed(2, 600)
#bmw.Color()
#audi.Speed(3.5,400, Audi.name)
##1)audi.Speed(3.5,400)
#audi.Type() 




#Hybrid Inheritance
#[One Child class having 2 or more than 2 Parents r prasent]

class Student():
    def info(self, name, roll_number):
        print(name + "'s roll_number is "+str(roll_number))

class Marks(Student):
    def sub_total(self, sub1, sub2, sub3):
        print("Total Marks are "+ (str(sub1 + sub2 + sub3)))

class Sports(Student):
    def sport_grade(self, grade):
        print("grade is "+grade)

class Result(Marks,Sports):
    def final_result(self, subjects, grade):
        sub1, sub2, sub3 = subjects
        Marks.sub_total(self, sub1, sub2, sub3)
        Sports.sport_grade(self, grade)

result = Result()
result.info("XYZ", 30)
result.final_result((100, 68, 82), "A")                                
            