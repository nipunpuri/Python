max = None
min = None
while True:
    try:
        
        num = raw_input("Enter a number ")
        if num == "done":
            print "Maximum is" , max
            print "Minimum is" , min
            break
        else:
            num = int(num)
        if max is None or num > max:
            max = num
        if min is None or num < min:
            min = num
            
            
    except:
        print("Invalid input") #the input's i is small in the auto-grader
        continue