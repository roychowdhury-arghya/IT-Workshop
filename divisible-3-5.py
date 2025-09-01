count = 0
for i in range (1,101):
    if i%3==0 and i%5 == 0:
        count+=1
print("Count of numbers divisible by 3 and 5 :",count)