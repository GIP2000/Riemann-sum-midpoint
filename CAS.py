import math

def calculateArea(func,min,max,sub):
	length = (max-min)/sub 
	bounds = [Bounds(min,min+length)]
	area = 0
	for i in range(1,sub):
		bounds.append(Bounds(bounds[i-1].second,min+((i+1)*length)))


	for i in range(len(bounds)):
		midpoint = bounds[i].first + (length/2)
		# print(midpoint)
		area += func(midpoint)*length
	return area


def mathFunciton(x):
	return math.sin(x)

class Bounds():
	def __init__(self,first,second):
		self.first = first 
		self.second = second

	def __repr__(self):
		return "first = {} second = {}".format(self.first,self.second)
	
answer = calculateArea(mathFunciton,math.pi,2*math.pi,1000)
print(answer)
