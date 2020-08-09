def euler36():
	s = 0
	for i in range(1,1000):
		j = int(str(i)+str(i)[::-1])
		if bin(j)[2:]==bin(j)[2:][::-1]:
			s+=j
	for i in range(0,100):
		for k in range(10):
			if i!=0: j = int(str(i)+str(k)+str(i)[::-1])
			else: j = k
			if bin(j)[2:]==bin(j)[2:][::-1]:
				s+=j
	print (s)
euler36()
