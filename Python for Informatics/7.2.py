# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
try:
	fhand = open(fname)
except:
	print "Could not find the file"
	exit()
	
count = 0
total = 0
for line in fhand:
	if line.startswith("X-DSPAM-Confidence:"):
		count = count + 1

		total = float(total) + float(line[len("X-DSPAM-Confidence:") + 1: 30])
avg = float(total/count)
print "Average spam confidence:" , avg

