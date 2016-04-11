fname = "mbox-short.txt"
fhand = open(fname)
names = []
numLines = 0

for line in fhand:
	line = line.strip()
	words = line.split()
	
	if len(words) > 0 and words[0] == "From":
		names.append(words[1])
		numLines = numLines + 1
		
for name in names:
	print name

out = "There were %d lines in the file with From as the first word" %(numLines)
print out