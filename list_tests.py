''' TESTING 4 COMMON OPERATIONS TO IMPLEMENT
	THE LIST DATA STRUCTURE
'''
# FOR LOOP TO CREATE LIST BY CONCATENATION
def test1():
	l = []
	for i in range(10000):
		l = l + [i]

# 783 MS PER LOOP
# ------------------------------------------
# FOR LOOP TO CREATE LIST BY USING APPEND()
def test2():
	l = []
	for i in range(10000):
		l.append(i)

# 3.86 MS PER LOOP
# ------------------------------------------
# LIST COMPREHESION
def test3():
	l = [i for i in range(10000)]

# 1.8 MS PER LOOP	
# ------------------------------------------
# RANGE FUNCTION WRAPPED BY A CALL TO THE 
# LIST CONSTRUCTOR
def test4():
	l = list(range(10000))

# 931 µs PER LOOP
# -------------------------------------------
