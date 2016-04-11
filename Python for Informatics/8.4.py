fname = "romeo.txt"
fhand = open(fname)

for line in fhand:
	words = line.split()
	print words
	
index = range(1,len(words))

for i in index:
	print i
