a = [1,2,3,4,5,6]
print "The original list"
print a 

def chop(t): #In this function we have modified the argument and returned None. i.e. I am changing the value of the original argument and not creating a new one 
	del t[len(t)-1]
	del t[0]
	return None 
	
t1 = chop(a)
print "The chopped list"
print t1

def middle(t):#In this function, I am changing creating a new variable by modifying the original and I am also returning it
	t2 = t[1:len(t)-1]
	return t2
	
t2 = middle(a)  
print "The middle list"
print t2