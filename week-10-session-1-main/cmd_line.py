
# Demonstration of command line arguments
# Run the code with any number of additional arguments
# python cmd_line.py abc
# python cmd_line.py fred bob -3.1 4 a-b-c

import sys

print(f"sys.argv is a {type(sys.argv)}")   # sys.argv is a list

n = len(sys.argv)
print(f"Total arguments passed:", n)

for item in sys.argv:   # iterate through the list
    print(f"Type: {type(item)} Value: {item}")   # all items are strings
    
 # Extensions
 # 1. How do we extract useful data from command line arguments?
 # eg. what if we are entering numerical values?
 # 2. How do we "sanitise" command line arguments
 # ie. we should test any user input in the same way as we do with input()
 
