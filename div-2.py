#Number divisible by 2 and 3 any one
number = int(input("Enter a Number : "))
if(number%2==0):
    print(number," is divisible by 2")
elif(number%3==0):
    print(number," is divisible by 3")
else:
    print(number, "is not divisible by 2 and 3")
