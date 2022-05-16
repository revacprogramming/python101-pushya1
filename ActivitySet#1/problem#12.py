# Regular Expressions
# https://www.py4e.com/lessons/regex

fhand = open("actual-file")
import re
nums_list = list()
for line in fhand:
    line = line.rstrip()
    num_list=re.findall('[0-9]+',line)
    if len(num_list)==0:
        continue
    nums_list+=num_list
total = 0
for num in nums_list:
    total+=int(num)
print("sum of the numbers in sample text is ",total)
    
    