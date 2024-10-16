# num1=10
# num2=5
# print(num1&num2,"& operator")

# print(num1|num2,"| or opeerator")

# print(~num1)

# print(num1 <<3)
# print(num2>>2)

def evenodd(n):
    if(n^1==n+1):
        return True
    else:
        return False
    
number=int(input("Enter a number: "))
if evenodd(number):
    print("is even")
else:
    print("is odd")