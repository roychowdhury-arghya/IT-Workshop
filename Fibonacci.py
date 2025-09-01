#print first N fibonacci number using while loop
n = int(input("Enter a number :"))
a,b = 0,1
count = 0
print("Fibonacci Series : ")
while count<n:
    print(a , end = " ")
    a,b = b ,a+b
    count +=1

# end  = " "  used for means stay on the same line with a space 
# (instead of moving to a new line every time).
# print(a , end = " ") similar to printf("%d ", a);
