def count(str , x , case):
	num = 0
	if case == 0:
		for i in str:
			if i == x or i == x.upper():
				num = num + 1
		print num
	elif case == 1:
		for i in str:
			if i == x:
				num = num + 1
		print num
	
		
count("Nipun" , "n" , 0)