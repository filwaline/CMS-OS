# -------------
# User Instructions
#
# Here you will be implementing a cyclic smoothing
# algorithm. This algorithm should not fix the end
# points (as you did in the unit quizzes). You  
# should use the gradient descent equations that
# you used previously.
#
# Your function should return the newpath that it
# calculates..
#
# Feel free to use the provided solution_check function
# to test your code. You can find it at the bottom.
#
# --------------
# Testing Instructions
# 
# To test your code, call the solution_check function with
# two arguments. The first argument should be the result of your
# smooth function. The second should be the corresponding answer.
# For example, calling
#
# solution_check(smooth(testpath1), answer1)
#
# should return True if your answer is correct and False if
# it is not.

from math import *
from copy import deepcopy

# Do not modify path inside your function.
path=[[0, 0], 
      [1, 0],
      [2, 0],
      [3, 0],
      [4, 0],
      [5, 0],
      [6, 0],
      [6, 1],
      [6, 2],
      [6, 3],
      [5, 3],
      [4, 3],
      [3, 3],
      [2, 3],
      [1, 3],
      [0, 3],
      [0, 2],
      [0, 1]]

############# ONLY ENTER CODE BELOW THIS LINE ##########

# ------------------------------------------------
# smooth coordinates
# If your code is timing out, make the tolerance parameter
# larger to decrease run time.
#

def smooth(path, weight_data = 0.1, weight_smooth = 0.1, tolerance = 0.00001):

    # 
    # Enter code here
    #

    # deep copy
    sp = deepcopy(path) # smoothing path
    n = len(path)
    while True:
    	grad = [[0,0] for p in path]
    	for index,point in enumerate(path):
    		for j in xrange(2):
    			grad[index][j] += weight_data * (point[j] - sp[index][j])
    			grad[index][j] += weight_smooth * (sp[(index+1)%n][j] + sp[index-1][j] - 2 * sp[index][j])
    			
    	

    	for i in xrange(n):
    		for j in xrange(2):
    			sp[i][j] += grad[i][j]

    	if sum(sum(abs(a) for a in g) for g in grad) < tolerance:
    		break

    return sp


def main():
	for p,sp in zip(path,smooth(path,weight_data=0.5,weight_smooth=0.1)):
		print '['+ ', '.join('%.3f'%x for x in p) +'] -> ['+ ', '.join('%.3f'%x for x in sp) +']'




if __name__ == '__main__':
	main()



# thank you - EnTerr - for posting this on our discussion forum

#newpath = smooth(path)
#for i in range(len(path)):
#    print '['+ ', '.join('%.3f'%x for x in path[i]) +'] -> ['+ ', '.join('%.3f'%x for x in newpath[i]) +']'


