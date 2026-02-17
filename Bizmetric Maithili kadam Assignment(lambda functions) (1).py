
#  #LAMBDA FUNCTIONS


#1.	Write a lambda to add two numbers. 
a , b = 4,7
add = lambda a, b: a + b
print (add(a,b))

#2.	Create a lambda to check if a number is even. 
x = 19
is_even = lambda x: x % 2 == 0
print (is_even(x))

#3.	Write a lambda to get the last character of a string. 
s = "PYTHON"
char1 = lambda s: s[-1]
print (char1(s))

#4.	Use lambda with map() to square every number in a list.
num = [11, 20, 32, 44]
squares = list(map(lambda x: x**2, num))
print (squares)
 
# #5.	Use lambda with filter() to get only odd numbers from a list.
num = [11, 32, 39, 40, 55]
odd = list(filter(lambda x: x % 2 != 0, num))
print (odd)
 
#6.	Use sorted() + lambda to sort a list of tuples by second value.
data = [(1, 3), (4, 1), (2, 5), (8,2)]
data1 = sorted(data, key=lambda x: x[1])
print (data1)
 
#7.	Create a lambda to check if a string is a palindrome.
s = "MALAYALAM"
palindrome = lambda s: s == s[::-1]
print (palindrome(s))
 
#8.	Use lambda to find maximum of three numbers.
a , b, c = 34,78,98
maximum = lambda a, b, c: max(a, b, c)
print (maximum (a,b,c))
 
#9.	Write a lambda to reverse a string.
s = "PYTHON"
reverse = lambda s: s[::-1]
print (reverse(s))
 
#10.	Use lambda with map() to convert a list of strings to integers.
lst = ["10", "20", "30"]
num = list(map(lambda x: int(x), lst))
print (num)

#11.	Use lambda with filter() to remove empty strings from a list. 
lst = ["Shyam", "", "Rajat", "", "Siya"]
result = list(filter(lambda x: x != "", lst))
print (result)

# #12. Use lambda to compute factorial using reduce().
from functools import reduce
fact = lambda n: reduce(lambda x, y: x*y, range(1, n+1), 1)
print (fact(9))

# #13. Write a lambda that returns the larger of two numbers.
a , b = 98 , 34
large = lambda a, b: a if a > b else b 
print (large(a,b))

#14. Use lambda to check if number is divisible by 5. 
remainder = lambda x: x % 5 == 0
print (remainder (555))

#15. Use lambda + map() to add 10 to each element of a list.
num = [5, 10, 15]
result = list(map(lambda x: x + 10, num)) 
print (result)

#16. Use lambda to sort a list of dictionaries by a key (like "age"). 
people = [ {"name": "Rajat", "age": 35}, {"name": "Siya", "age": 30}]
people1 = sorted(people, key=lambda x: x["age"])
print (people1)

#17. Write a lambda that returns True if a character is a vowel. 
ch = 'oui'   # you
vowel = lambda ch: ch.lower() in "aeiou"
print (vowel(ch))

#18. Use lambda + filter to extract words of length > 5 from a list. 
word = ["Python", "Training", "Bizmetric", "Mysql"]
word1 = list(filter(lambda x: len(x) > 5, word))
print (word1)

#19. Use lambda to calculate the area of a circle (πr²). 
import math
area = lambda r: math.pi * r * r
print (area(5))

#20. Write a lambda to remove duplicates from a list using filter + set. 
lst = [1, 2, 2, 3, 4, 4]
unique = list(set(lst))
print (unique)

#21.	Use lambda with reduce() to find the product of all numbers in a list.
from functools import reduce
num = [1, 20, 33, 2]
product = reduce(lambda x, y: x*y, num ) 
print (product)

#22.	Write a lambda that returns absolute value of a number. 
absolute = lambda x: abs(x)
print (absolute (-67))

# #23.	Use lambda to sort a list of strings by their length. 
words = ["bye", "hi", "python", "training"]
sort1 = sorted(words, key=lambda x: len(x))
print (sort1)

#24.	Use lambda to get only uppercase characters from a string. 
text = "PyThOn CoDe"
upper = list(filter(lambda x: x.isupper(), text))
print (upper)


#25.	Write a lambda that returns the square if number is even, cube if odd. 
x = 34     #35 
calc = lambda x: x**2 if x % 2 == 0 else x**3
print (calc(x))

#26.	Use lambda with map to convert Celsius to Fahrenheit.
celsius = [10, 80, 17]
fahrenheit = list(map(lambda c: (c*9/5)+32, celsius)) 
print (fahrenheit)

#27.	Write a lambda to check if two strings are anagrams. 
a = "listen"
b = "silent"
is_anagram = lambda a, b: sorted(a) == sorted(b)
print (is_anagram(a,b))

#28.	Use lambda to extract only numeric values from a mixed list. 
lst = [10, "cat", 33.5, "80", 79]
num = list(filter(lambda x: isinstance(x, (int, float)), lst))
print (num)

#29.	Use lambda inside any() to check if any list element is negative. 
num = [2,6,-9,1]
negative = any(map(lambda x: x < 0, num))
print (negative)

# #30.	Use lambda to generate a function that multiplies any number by n
multi = lambda n: lambda x: x * n
num = multi(3)
print(num(5))   
