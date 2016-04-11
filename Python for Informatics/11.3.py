import re
total = 0
count = 0
hand = open("regex_sum.txt")
for line in hand:
    line = line.rstrip()
    lst = re.findall("([0-9]+)" , line)
    if len(lst) > 0:
        for i in range(len(lst)):
            total = total + int(lst[i])
            count = count +1
print total
print count