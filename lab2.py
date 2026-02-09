# marks = int(input("Enter marks: "))

# if marks >= 90:
#     print("Grade A")
# elif marks >= 75:
#     print("Grade B")
# elif marks >= 50:
#     print("Grade C")
# else:
#     print("Fail")

# # day = "Monday"
# day = str(input("Enter today : "))

# if day == "Sunday":
#     print("Holiday")
# else:
#     if day == "Monday":
#         print("Go to gym")
#     else:
#         print("Go to work")


# a = 10
# b = 20
# c = 15
# a = int(input("Enter first numebr :"))
# b = int(input("Enter second numebr :"))
# c = int(input("Enter third numebr :"))

# a,b,c = map(int , input("Enter three numbers: ").split())

# if a > b:
#     if a > c:
#         print("a is largest",a)
#     else:
#         print("c is largest")
# else:
#     if b > c:
#         print("b is largest")
#     else:
#         print("c is largest")


#               Loops

# for i in range(1, 6):
#     print(i)

# #sum of n numbers 
# n = int(input("Enter total numbers : "))
# sum = 0
# for i in range(1,n+1):
#     sum+=i
# print(sum)

# #loop through subjects

# # subjects = ["Arghya","Sayan","Pagla"]
# # subjects = map(str,input("Enter all names one by one : ").split())
# # subjects = input("Enter all the names : ").split()
# for i in subjects:
#     print(i)

# for week in range(1, 3):
#     for day in range(1, 6):
#         print("Week", week, "Day", day)

#factorial


# n = int(input("Enter a number : "))
# fact = 1
# # while n>0:
# #     fact *= n
# #     n-=1
# for i in range(1,n):
#     fact *=n
#     n-=1
# print(fact)

#reverse string

# n = int(input("Enter the numbers: "))
# rev = 0

# while n > 0:
#     digit = n % 10
#     rev = rev * 10 + digit
#     n = n//10

# print(rev)




