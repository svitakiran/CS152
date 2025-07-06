"""
com.py

Svita Kiran
Fall 2023
9/27/23
CS152 Lab 3

python3 com.py

"""

import sys

print(sys.argv)

print("Running program", sys.argv[0])
print("I'm going to open the file", sys.argv[1])
print("I'm going to extract column", int(sys.argv[2]))