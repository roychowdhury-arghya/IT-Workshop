rows = int (input("Enter number of Rows : "))
for i in range (1,rows+1):
    for j in range(1,i+1):
        print("*" ,end = " ")
    print()
# print() - moves to next line after each rows