
def prime_number(num):
    if num >1:
        for i in range(2,num):
            if num%i==0:
                result = "Not Prime"
                break
        else:
            result = "Prime"
    print(result)


num = int(input("enter the number"))
prime_number(num)