colors = [['red', 'green', 'green', 'red' , 'red'],
          ['red', 'red', 'green', 'red', 'red'],
          ['red', 'red', 'green', 'green', 'red'],
          ['red', 'red', 'red', 'red', 'red']]

measurements = ['green', 'green', 'green', 'green', 'green']


motions = [[0, 0], [0, 1], [1, 0], [1, 0], [0, 1]]

sensor_right = 0.7

p_move = 0.8

def show(p):
    for i in range(len(p)):
        print p[i]


def calculate():

    #DO NOT USE IMPORT
    #ENTER CODE BELOW HERE
    #ANY CODE ABOVE WILL CAUSE
    #HOMEWORK TO BE GRADED
    #INCORRECT
    x,y = len(colors),len(colors[0])  
    pinit = 1.0 / (x * y) 
    p = [[pinit for cell in row] for row in colors]
    

    for i in range(len(motions)):
    	p = move(p,motions[i],p_move,x,y)
    	p = sense(p,measurements[i],sensor_right,colors,x,y)

    #Your probability array must be printed 
    #with the following code.

    show(p)
    return p


def move(prob,movement,p_move,x,y):
	if movement == [0,0]:
		return prob
	else:
		prob_stay = [[(1-p_move)*cell for cell in row] for row in prob]
		prob_move = [[0 for cell in row] for row in prob]
		for i in range(x):
			for j in range(y):
				prob_move[(i+movement[0])%x][(j+movement[1])%y] += prob[i][j] * p_move

		for i in range(x):
			for j in range(y):
				prob[i][j] = prob_move[i][j] + prob_stay[i][j]

	return prob


def sense(prob,Z,sensor_right,colors,x,y):
	for i in range(x):
		for j in range(y):
			if Z == colors[i][j]:
				prob[i][j] *= sensor_right
			else:
				prob[i][j] *= 1 - sensor_right

	normalizer = sum(sum(row) for row in prob)
	prob = [[cell / normalizer for cell in row] for row in prob]
	return prob


if __name__ == '__main__':
	print calculate()
