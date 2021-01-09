numbers = input()
total = 0
temp = 0
for char in numbers:
    if char ==" ":
        total = total +temp
        temp = 0
    else:
         temp = temp*10+int(char)
total = total + temp
print(total)    

    
