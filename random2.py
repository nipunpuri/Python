fname = "mbox-short.txt"
fhand = open(fname)
names = []

for line in fhand:
	line = line.strip()
	if line.startswith("From"):
		words = line.split()
		if any(words[1] in i for i in names): continue
		names.append(words[1])
		
print names