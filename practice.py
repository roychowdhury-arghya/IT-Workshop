for i in range (5):
    print (i)
name = "Arghya"
roll = 1
cgpa = 9.23
student = True

print(student,type(student))
print(name,type(name))
print(roll,type(roll))
print(cgpa,type(cgpa))

a,b,c=1,2,3
print(a,b,c)
x=y=z=11
print(x,y,z)


# x = 10
# y=5
# print(x > 5 and y < 10) # True
# print(x > 20 or y < 10) # True
# print(not(x > 5))
# # False

fruit = "apple"
print('g' in fruit)
print('g' not in fruit)

msg = "welcome to india"
print(msg)
print(msg.capitalize())
print(msg.upper())
print(msg.count("i"))
print(msg.find("to"))
print(msg.replace("india","kolkata"))
print(msg)
print(msg[-7:-1])
print(msg[-1])
print(msg[7:])
print(msg[0:10])


# list in python 
shopping_list=["milk","potato","apple","banana"]
cooking_list=["curry","fry"]
city = ["kolkata","mumbai","delhi"]
print(shopping_list)
print("apple" in shopping_list)
print("mango" in shopping_list)
print("First item :", shopping_list[0])
print("Last element :",shopping_list[-1])
print(shopping_list+cooking_list)
print(len(shopping_list))
print(city)
city[2]="pune"
print(city)
city.append("surat")
print(city)
item = city.pop()
print(city)
print("popped item : ", item )
city.remove("mumbai")
print(city)


# Fibonacci Number
n = int(input("Enter number of terms: "))
a, b =1, 2

for i in range(n):
    print(a, end="\n")
    a, b = b, a + b

person = ("Alice", 28, "Kolkata")
print(person[0])
print(person[-1])

t1 = (1, 2, 3)
t2 = (4, 5)
print(t1 + t2)
print(t2 * 2)
print(t1[1:3])