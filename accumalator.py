''' SIMPLE ACCUMALATOR PROGRAMS
'''
# LETS TIME SOME FUNCTIONS

# USING ACCUMALATOR VARIABLE, COMPUTE THE SUM 
# OF THE FIRST 'N' INTEGERS
def sumOfN(n):

	theSum = 0
	for i in range(1,n+1):
		theSum = theSum + i

	return theSum
# AVERAGE RUNTIME WAS 0.00038 SECONDS FOR 
#N = 100,000 - THAT'S 37000000 ns
#============================================#
def sumOfN2(n):
	return (n * (n+1)) / 2
# AVERAGE RUNTIME WAS 0.000000980 SECONDS FOR 
#N = 100,000 - THAT'S 980 ns



if __name__ == '__main__':
	app.run()
