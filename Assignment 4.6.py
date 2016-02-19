def computepay(h , r):
    if h <= 40:
        p = h*r
    elif h > 40:
        p = (40)*r + (h-40)*r*1.5
    return p


try:
    hours = raw_input("Number of hours worked?")
    hours = float(hours)
    
    rate = raw_input("what is your rate per hour?")
    rate = float(rate)
    
except:
    quit()

pay = computepay(hours , rate)
print pay