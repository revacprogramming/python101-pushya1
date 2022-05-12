# # Files

# # filename = "dataset/mbox-short.txt"

# 7.2 Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
# X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.


# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")

try:
    fhand = open(fname)
except:
    print("the file doesn't exist")
    quit()
    
count = 0
average = 0

for line in fhand:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    else:
        position = line.find(":")
        average+=float(line[position+1:])
        count+=1
average = average/count
print("Average spam confidence:",average)
    	