fname = "words.txt"
fhand = open(fname)

for line in fhand:
    words = line.split()
    print words
    
dic = dict()

dic_num = range(0 , len(words))
i = 0
for word in words:
    print word
    print dic_num[i]
    dic[word] = dic_num[i]
    i = i+1