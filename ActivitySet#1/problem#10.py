# Dictionaries

# filename = "dataset/mbox-short.txt"

name = input("Enter file:")

try:
    fhand = open(name)
except:
    print("file not found!")
    quit()
    
di = dict()
li = list()

for line in fhand:
    line = line.rstrip()
    if line.startswith('From:'):
        words = line.split()
        li.append(words[1])   
for w in li:
    di[w] = di.get(w,0)+1
    
largest_count = -1
largest_name = None
for k,v in di.items():
    if largest_count<v:
        largest_count=v
        largest_name = k
print(largest_name,largest_count)
    
