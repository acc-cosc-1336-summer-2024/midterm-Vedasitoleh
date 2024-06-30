#write functions here, don't add input('') statements here!
#Write a function is_prime that returns True if a number is prime False otherwise.

def is_prime(num):
    #if num = 0 or 1 return false
    if num == 0 or num == 1:
        print("It is not a Prime Number")
        return False
    factor_var = 2
    while factor_var < num:
        if num%factor_var ==0:
            print("It is not a Prime Number")
            return False
        factor_var+= 1
    print ("It is a Prime number")
    return True
    #if number divisible by factor_var and modulo = 0 return FALSE
    # else increment factor_var
      #if factor_var = num-1 return TRUE

#print(is_prime(3))