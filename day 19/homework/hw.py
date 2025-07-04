 #1:
#სია:

#numbers = [10, 20, 30, 40, 50, 60, 70]
#აიღე ამ სიიდან პირველი 3 ელემენტი slicing-ის გამოყენებით.

numbers = [10, 20, 30, 40, 50, 60, 70]
first_three = numbers[:3]
print(first_three)  # [10, 20, 30]


#letters = ['a', 'b', 'c', 'd', 'e', 'f']
#დაპრინტე სიიდან ელემენტები 'c', 'd', 'e' slicing-ით.

letters = ['a', 'b', 'c', 'd', 'e', 'f']
middle_part = letters[2:5]
print(middle_part)  # ['c', 'd', 'e']

#words = ['apple', 'banana', 'cherry', 'date', 'fig', 'grape']
#აიღე სიის ბოლო 2 ელემენტი slicing-ის მეშვეობით.

words = ['apple', 'banana', 'cherry', 'date', 'fig', 'grape']
last_two = words[-2:]
print(last_two)  # ['fig', 'grape']

#colors = ['red', 'green', 'blue', 'yellow', 'purple']
#დაპრინტე სია შუიდან დაწყებული ბოლომდე (სადღაც 'blue'-დან ბოლომდე) slicing-ით.

colors = ['red', 'green', 'blue', 'yellow', 'purple']
from_middle = colors[2:]
print(from_middle)  # ['blue', 'yellow', 'purple']

#text = "programming"
#დაპრინტე მხოლოდ პირველი 5 სიმბოლო slicing-ის მეშვეობით.

text = "programming"
first_five = text[:5]
print(first_five)  # 'progamming'