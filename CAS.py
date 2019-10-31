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

def get_midpoint_values_average(func,min,max,sub):
	length = (max-min)/sub 
	bounds = [Bounds(min,min+length)]
	for i in range(1,sub):
		bounds.append(Bounds(bounds[i-1].second,min+((i+1)*length)))

	midpoint_values = []
	for i in range(len(bounds)):
		midpoint = bounds[i].first + (length/2)

		midpoint_values.append(func(midpoint))
	return get_average(midpoint_values)


def get_average(midpoints):
	sum = 0
	for i in range(len(midpoints)):
		sum += midpoints[i]
	return sum/len(midpoints)


def mathFunciton(x):
	return math.sin(x)

class Bounds():
	def __init__(self,first,second):
		self.first = first 
		self.second = second

	def __repr__(self):
		return "first = {} second = {}".format(self.first,self.second)

print("n = 100 -> {}".format(get_midpoint_values_average(mathFunciton,0,math.pi,100)))
print("n = 200 -> {}".format(get_midpoint_values_average(mathFunciton,0,math.pi,200)))
print("n = 1000 -> {}".format(get_midpoint_values_average(mathFunciton,0,math.pi,1000)))

print(math.asin(get_midpoint_values_average(mathFunciton,0,math.pi,1000)))





