# -*- coding: utf-8 -*-
"""mahmud_omer_19660_hw1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-WJB_kf5D5rEgWFmCYpXSnOmTapkvsch
"""

# def  if_function(condition, true_result, false_result):
"""Return true_result if condition is a true value, and
    false_result otherwise.
    >>> if_function(True, 2, 3)
    2
    >>> if_function(False, 2, 3)
    3
    >>> if_function(3==2, 3+2, 3-2)
    1
    >>> if_function(3>2, 3+2, 3-2)
    5
    """
#ANS

def  if_function(condition, true_result, false_result):
    if condition:
        return true_func(true_result)
    else:
        return false_func(false_result)

def true_func(true_result):
     return true_result

def false_func(false_result):
    return false_result 

def main():
   print(if_function(3==2, 3+2, 3-2))
main()

#2.	Create a function to add odd numbers less equal than numeric input parameter together as follows
"""
            >>> sum_odd(6)		#1+3+5
            9
            >>>sum_odd(7)		#1+3+5+7
            16
"""
#ANS 
numeric_input = int(input("Enter a num: "))
def sum_odd(num):
    sum = 0
    for i in range(num + 1):
        if i % 2 == 0:
            continue
        else:
            sum += i
    return sum
print(sum_odd(numeric_input))

#3 Define a function for 4 inputs a, b, c, d, and return sum of square of two smallest number from a, b, c and d, such as
"""
>>> foo(1, 2, 3, 4)		
		>>> 5 				# 1^2+ 2^2=5
		>>> foo(-3, 1, 5, 6)	
>>> 10				# 〖(-3)〗^2+ 1^2=10
         
"""
#ANS 
def foo(a, b, c, d):
    num_list = [a, b, c, d]
    sorted_list = sorted(num_list)
    x = sorted_list[0]
    y = sorted_list[1]
    return x ** 2 + y ** 2

print(foo(1, 2, 3, 4))
print(foo(-3, 1, 5, 6))

#4.	Write a function named "df" that takes three integers x, y, and z. It returns whether subtracting one of these numbers from another gives the third.
""" >>> df(5, 3, 2) # 5 - 3 is 2
    True
    >>> df(2, 3, 5) # 5 - 3 is 2
    True
    >>> df(2, 5, 3) # 5 - 3 is 2
    True
    >>> df(-2, 3, 5) # 3 - 5 is -2
    True
    >>> df(-5, -3, -2) # -5 - -2 is -3
    True
    >>> df(-2, 3, -5) # -2 - 3 is -5
    True
    >>> df(2, 3, -5)
    False
    >>> df(10, 6, 4)
    True
    >>> df(10, 6, 3)
    False """
#ANS

def df(a, b, c):
    if (a - b) == c or (c - b) == a or (b - c) == a or (a - c) == b:
        print("True")
    else:
        print("False")
df(5, 3, 2)
df(2, 3, 5)
df(2, 5, 3)
df(-2, 3, 5) 
df(-5, -3, -2) 
df(-2, 3, -5)
df(2, 3, -5)
df(10, 6, 4)
df(10, 6, 3)

#5.	Create a function that takes an integer m greater than 1 and returns the largest integer smaller than m that evenly divides m.

#def  lrgst_factor(m):
"""Return the largest factor of n that is smaller than n.

    >>> lrgst_factor (15) 	# factors are 1, 3, 5
    5
    >>> lrgst_factor (80) 	# factors are 1, 2, 4, 5, 8, 10, 16, 20, 40
    40
"""
#ANS
def largest_integer(m):
    factorials = []
    for i in range(1, m):
        if m % i == 0:
            factorials.append(i)
    print(f"List of Factorials for {m} : {factorials}")
    print("Largest factor: " + str(factorials[-1]))

largest_integer(15)
largest_integer(80)

# 6.	Define a function which takes in a number n and determines whether the number is a perfect number. A perfect number is equal to the sum of its factors. For instance, 6 is a perfect number since 6 = 1 + 2 + 3.

#def pfct_num(m):
"""
    Returns True or False indicating whether "n" is a perfect 
    number. A number is a perfect number when the sum of all its 
    factors equal the number itself.

    >>> pfct_num (6)
    True
    >>> pfct_num (8)
    False
    >>> pfct_num (28)
True
"""
#ANS
def pfct_num(m):
    factorials = []
    for i in range(1, m):
        if m % i == 0:
            factorials.append(i)
    print(f"List of Factorials for {m} are {factorials}")
    sum = 0
    for j in factorials:
        sum += j
    if sum == m:
        print(f"True!, {m} is a perfect number.")
    else:
        print(f"True!, {m} is not a perfect number.")

pfct_num(6)
pfct_num(8)
pfct_num(28)

# 7.	Implement a function to check if the number of bits from two positive input parameters is the same or not.
#def    same_ord(a, b):
"""Return whether positive integers a and b have the same number of digits.

    >>> same_ord(50, 70)			# 2 bits of a and b
    True
    >>> same_ord(50, 100)			# a is 2 bits; b is 3 bits
    False
    >>> same_ord(1000, 100000)		# a is 4 bits; b is 6 bits
    False
"""
#ANS
def same_ord(a, b):
    len_of_a = len(str(a))
    len_of_b = len(str(b))
    print(f"Digits of first number is {len_of_a} and digits of second number is {len_of_b}.")
    if len_of_a == len_of_b:
        print("True")
    else:
        print("False")

same_ord(50, 100)
same_ord(50, 70)
same_ord(1000, 100000)

#8.	Write a function that takes in a number and determines if the digits contain two adjacent 5s.

#def 	double_5(n):
"""Return true if n has two fives in a row.

    >>> double_5 (5)
    False
    >>> double_5 (55)
    True
    >>> double_5 (550055)
    True
    >>> double_5 (12345)
    False
    >>> double_5 (50505050)
    False
"""
#ANS
def double_5(num):
    number = str(num)
    contains_55 = "55"
    if contains_55 in number:
        print(f"True! 55 is in {number}")
    else:
        print("False!")
        
double_5(5)
double_5(550055)
double_5(50505050)

#9.	Design a function that returns the number of unique digits in a positive integer.
#def uniq_digits(x):
"""Return the number of unique digits in positive integer n

    >>> uniq_digits (8675309) 	# All are unique
    7
    >>> uniq_digits (1313131) 	# 1 and 3
    2
    >>> uniq_digits (13173131) 	# 1, 3, and 7
    3
    >>> uniq_digits (10000) 		# 0 and 1
    2
    >>> uniq_digits (101) 		# 0 and 1
    2
    >>> uniq_digits (10) 		# 0 and 1
    2
"""

# ANS
def uniq_digits(x):
    number = str(x)
    unique = sorted([int(x) for x in set(number)])

    print(f"Unique digits: {unique}")
    print("Total Num of unique digits: " + str(len(unique)))
    
uniq_digits(8675309)
uniq_digits(1313131)
uniq_digits(10000)
uniq_digits(10)

# 10.	Write a def function "amc" with a positive integer "n" input parameter. It returns the smallest amicable number greater than "n". Two different numbers are both amicable if the sum of the proper divisors of each is equal to the other. Any number that's part of such a pair is an amicable number.

#*Hint: You may want to create a separate function to sum proper divisors.

#def  amc(n):
"""
  Return the smallest amicable number greater than positive integer n.

      Every amicable number x has a buddy y different from x, such that
      the sum of the proper divisors of x equals y, and
      the sum of the proper divisors of y equals x.

      For example, 220 and 284 are both amicable because
      1 + 2 + 4 + 5 + 10 + 11 + 20 + 22 + 44 + 55 + 110 is 284, and
      1 + 2 + 4 + 71 + 142 is 220

      >>> amc(5)
      220
      >>> amc(220)
      284
      >>> amc(284)
      1184
      >>> r = amc(5000)
      >>> r
      5020
"""
# ANS
def sum_of_division(x):
    sum = 1
    for i in range(2, x):
        if x % i == 0:
            sum += i
    return sum

def is_amicable(a, b):
    if sum_of_division(a) == b and sum_of_division(b) == a:
        return True
    else:
        return False

def amc(n):
    i = n + 1
    while i < 10000:
        j = 0
        while j < 10000:
            if is_amicable(i, j):
                return i
            j += 1
        i += 1
print(amc(220))
r = amc(5000)
print(r)