def is_prime(num):
    if num<=1:
        return False
    for i in range (2,int (num**0.5)+1):
        if num % i==0:
            return False
    return True
n= int(input("enter a number to check if it's prime"))
if is_prime(n):
    print(f"{n} is a prime number")
else:
    print(f"{n} is not a prime number")




