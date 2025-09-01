num = int (input("Enter the number : "))
sum = 0
while num >0 :
    digit = num % 10
    sum +=digit
    num = num//10
# print(f"Sum of digits :{sum}")
print("Sum of digits :",(sum))

# // used for intiger division and / used for normal division or float