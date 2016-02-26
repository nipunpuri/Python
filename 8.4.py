fname = "romeo.txt"
fhand = open(fname)
big = []

for line in fhand:
	words = line.split()
	big = big + words
	
new_list =[]
for word in big:
	if any(word in s for s in new_list):
		continue
	else:
		new_list.append(word)
		
new_list.sort()
print new_list