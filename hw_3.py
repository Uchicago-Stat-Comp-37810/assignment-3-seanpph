# Name: Po-Hsiang Peng
# hw3.py

import math
import random

# ********** Exercise 1 ********** 

# Define is_divisible function here
def is_divisible(m,n):
    if n == 0:
        return False
    elif m%n == 0:
        return True
    else:
        return False
    

# Test cases for is_divisible
print(is_divisible(10, 5))  # This should return True
print(is_divisible(18, 7))  # This should return False
print(is_divisible(42, 0))  # What should this return? (This should return False)

# ********** Exercise 2 ********** 

# Define not_equal function here
def neq(a,b):
    if a==b:
        return False
    else:
        return True

# or simply

def neq1(a,b):
    return (not a==b)

# Test cases for not_equal
print("neq(3,5) is:", neq(3,5))
print("neq1(3,5) is:", neq1(3,5))
print("3!=5 is:", 3!=5)

print("neq(5,5) is:", neq(5,5))
print("neq1(5,5) is:", neq1(5,5))
print("5!=5 is:", 5!=5)

# ********** Exercise 3 ********** 

## multadd function
def multadd(a,b,c):
    return a * b + c

# Test Cases
angle_test = multadd(0.5, math.cos(math.pi/4), math.sin(math.pi/4))
print("sin(pi/4) + cos(pi/4)/2 is:", math.sin(math.pi/4) + math.cos(math.pi/4)/2)
print("multadd(0.5, cos(pi/4), sin(pi/4)) is:", angle_test)

ceiling_test = multadd(2, math.log(12,7), math.ceil(276/19))
print("ceiling(276/19) + 2 log_7(12) is:", math.ceil(276/19) + 2 *math.log(12,7))
print("multadd(2, log_7(12), ceiling(276/19)) is:", ceiling_test)


# ********** Exercise 4 **********

## rand_divis_3 function
def rand_divis_3():
    rnd = random.randint(0,100)
    print("random number is:", rnd)
    
    if rnd % 3 == 0:
        return True
    else:
        return False


# Test Cases
print("Is this random number divisible by 3:", rand_divis_3())
print("Is this random number divisible by 3:", rand_divis_3())
print("Is this random number divisible by 3:", rand_divis_3())
