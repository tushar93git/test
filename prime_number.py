
def prime_number(num):
    if num >1:
        for i in range(2,num):
            if num%i == 0:
                result = "Not Prime Number"
                break
        else:
            result = "Prime Number"
    return result


num = int(input("enter the number"))
r = prime_number(num)
print(r)