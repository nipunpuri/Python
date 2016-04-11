fhand = open("regex_sum.txt")
for line in fhand:
    


import re
lst = []
for line in fhand:
    line = line.rstrip()
    item = re.findall( reg, line) ##re.findall returns a list
    if len(item) > 0:
        lst.append(item)
        print len(lst)