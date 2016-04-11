import re
hand = open("mbox-short.txt")
for line in hand:
    line = line.rstrip()
    lst = re.findall("[a-z0-9A-Z]\S*@\S*[a-z0-9A-Z]" , line)  ##This is [These things]followed by zero or
                                                              ##more 
    if len(lst) >0:
        print lst
        
hand = open("mbox-short.txt")
for line in hand:
    line = line.rstrip()
    lst = re.findall("^X-\S+: ([0][.][0-9]+)" , line)  ##This is [These things]followed by zero or
                                                              ##more 
    if len(lst) >0:
        print lst