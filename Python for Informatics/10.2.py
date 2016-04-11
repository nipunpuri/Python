fname = "mbox-short.txt"
fhand = open(fname)

emails = dict()
for line in fhand():
    if line.startswith('From:'):
        print line





emails = dict()
for line in fhand:
    if line.startswith("From"):
        words = line.split()
        email = words[1]
        emails[email] = emails.get(email , 0) + 1
        
lst = list()
for email in emails:
    lst.append((emails[email] , email))
    
lst.sort(reverse = True)
print( lst[1][1], emails[lst[1][1]])