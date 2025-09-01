# Using nested if-else
marks = int(input("Enter your marks (0-100) : "))
if 0<=marks<=100 :
    if marks >=90 :
        print("Grade = A")
    else :
        if marks >= 80 :
            print("Grade = B")
        else:
            if marks >= 70 :
                print("Grade = C")
            else:
                print("Grade = Fail")
else:
    print("Invalid Marks !")