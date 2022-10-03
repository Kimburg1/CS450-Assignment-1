# uestion1

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

#2.	

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

def foo(a, b, c, d):
    num_list = [a, b, c, d]
    sorted_list = sorted(num_list)
    x = sorted_list[0]
    y = sorted_list[1]
    return x ** 2 + y ** 2

print(foo(1, 2, 3, 4))
print(foo(-3, 1, 5, 6))

#4.	

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

#5.	
def largest_integer(m):
    factorials = []
    for i in range(1, m):
        if m % i == 0:
            factorials.append(i)
    print(f"List of Factorials for {m} : {factorials}")
    print("Largest factor: " + str(factorials[-1]))

largest_integer(15)
largest_integer(80)

# 6.	
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

# 7.	
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

#8.	
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

#9.	
def uniq_digits(x):
    number = str(x)
    unique = sorted([int(x) for x in set(number)])

    print(f"Unique digits: {unique}")
    print("Total Num of unique digits: " + str(len(unique)))
    
uniq_digits(8675309)
uniq_digits(1313131)
uniq_digits(10000)
uniq_digits(10)

# 10.	
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
