import numpy as np 
import matplotlib.pyplot as plt 

def main():
	x = [0,0.3,1,1.7,2.1,2.5,2.9,3.5,3.9,4.3,5.0]
	y = [0.2,0.5,1.2,1.0,2.5,2.6,3.0,2.9,3.4,3.7,4.0]

	n = len(x)
	sum_xy = 0
	sum_x = 0
	sum_y = 0
	sum_x_sqr = 0
	for i in range(len(x)):
		sum_xy += x[i]*y[i]
		sum_x += x[i]
		sum_y += y[i]
		sum_x_sqr += x[i]*x[i]
	avg_x = sum_x/n
	avg_y = sum_y/n
	print("sum_xy, sum_x, sum_y, avg_x, avg_y, sum_x_sqr")
	print(sum_xy, sum_x, sum_y, avg_x, avg_y, sum_x_sqr)

	y_regression = []
	y0_regression = []
	for xx in x:
		y_regression.append(xx*0.785 + 0.33105)
		y0_regression.append(xx*0.88)
	plt.scatter(x, y, label = "scattered data")
	plt.plot(x, y_regression, label = "line regression case 1")
	plt.plot(x, y0_regression, label = "line regression case 0")
	plt.legend()
	plt.show()

if __name__ == "__main__":
	main()