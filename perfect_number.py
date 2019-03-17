def sovrshen_broj(num):
    psum = 0
    
    for x in range(1, num):
        if num % x == 0:
            psum += x

        

    if psum == num:
        return "Brojot {} e sovrshen".format(num)
    else:
        return "Brojot {} ne e sovrshen".format(num)


print(sovrshen_broj(15))        