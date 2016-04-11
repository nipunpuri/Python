fname = "words.txt"
fhand = open(fname)

for line in fhand:
    words = line.split()
    print words
    
dic = dict()

dic_num = range(0 , len(words))
i = 0
for word in words:
    dic[word] = dic_num[i]
    i = i+1