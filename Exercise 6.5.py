str = 'X-DSPAM-Confidence: 0.8475'

colon = str.find(": ")
num = float(str[colon+2:len(str)])
print type(num)



