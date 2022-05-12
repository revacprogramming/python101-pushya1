# Lists

# filename = "dataset/romeo.txt"

fname = input("Enter file name: ")

try:
    fhand = open(fname)
except:
    print("the file not exist")
    quit()
fh = fhand.read()
words_sp=fh.split()

lst = []

for word in words_sp:
    if word not in lst:
        lst.append(word)
    else:
        continue

lst.sort()
print(lst)
