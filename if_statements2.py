#num1 = 10
#num2 = 15

#print("num1 is grater") if num1>num2 else print("num2 is grater")

num1 = int(input("enter your number : "))
num2 = int(input("enter your number : "))

#if num1%3==0 and num2%5==0:
#if num1%3==0 or num2%5==0:
#if not num1%3==0 or num2%5==0:
if not num1%3==0 and num2%5==0:
    print("num1 is multiple of 3")
    print("num2 is multiple of 5")
else:
        print("bad numbers")

#T and T = T, F and T = F, T and F = F, F and F = F

#T or T = T ,F or T = T ,T or F = T, F or F = F

#T Xor T = F ,F Xor T = F ,T Xor F = F, F Xor F = T

#T Nand T = F, F Nand T = T, T Nand F = T, F Nand F = T
