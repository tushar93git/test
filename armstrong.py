def armstrong(num):
    new = num
    p = len(str(num))
    result = 0
    while num>0:
        digit = num%10
        result = result + digit**p
        num = num//10
    if result == new:
<<<<<<< HEAD
        print("Armstrong")
    else:
        print("Not Armstrong")
    
    
num = 153
armstrong(num)
=======
        return "Armstrong"
    else:
        return "Not Armstrong"
    
    
num = 153
a = armstrong(num)
print(a)
>>>>>>> thirsty
