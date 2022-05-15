# Tuples

filename = "dataset/mbox-short.txt"


name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
hours = list()
for line in handle:
    line = line.rstrip()
    if line.startswith('From '):
        word = line.split(":")
        hours.append(word[0][-2:])
hours.sort()

di = dict()

for hour in hours:
    di[hour] = di.get(hour,0)+1
    
for k,v in di.items():
    print(k,v)

        
