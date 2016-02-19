# Use the file name mbox-short.txt as the file name
fname = "mbox.txt"
try:
	fhand = open(fname)
except:
	print "Could not find the file"
	exit()

num = 0
for line in fhand:
	if line.startswith("X-DSPAM-Confidence"):
		a = line.find(": ")
		num = num + float(line[a + 2:len(line)])
print "The sum is" , num


