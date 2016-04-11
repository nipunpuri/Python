fname = "mbox-short.txt"
try:
	fhand = open(fname)
except:
	print "Could not find the file"
	exit()

for line in fhand:
	words = line.split()
	if len(words) > 0 and words[0] == "From":
		print "good"
	else:
		continue