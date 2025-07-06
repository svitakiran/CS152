"""
list_practice.py

Svita Kiran
Fall 2023
CS152 Lab 3

This program helps organize our Python programs and learn more details about lists.

To run this program type the following on the commandline:

python3 list_practice.py
"""

numbers = [5, 3, 6, 1, 2]
my_empty_list = []
first_number = numbers[0]
fourth_num = numbers[3]
print(first_number)
print(fourth_num)

numbers.append(7)
print(numbers)

numbers[0] = 4
numbers[2] = 8
numbers[4] = 5
print(numbers)