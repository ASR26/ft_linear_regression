from estimate import estimate_price
import matplotlib.pyplot as plt

""" Reads the values from data.csv file and returns it into a list"""

def read_data(file):
		try:
			data = open(file, 'r')
			data = data.read().split('\n')
			del data[0]
			del data[-1]
			data = [line.split(',') for line in data]
			data = [[float(element) for element in line] for line in data]
		except:
			print('Error during data reading')
			exit()

		return data

""" Displays the data as dots and the estimation as a line, receiving an object as argument"""

def final_state(lr):
	plt.figure("Data and estimation")
	plt.xlabel('Mileage')
	plt.ylabel('Price')
	plt.scatter(lr.raw_mileages, lr.raw_prices, color='blue')
	plt.plot(
		[min(lr.raw_mileages), max(lr.raw_mileages)],
		[estimate_price(lr.theta0, lr.theta1, min(lr.raw_mileages)), estimate_price(lr.theta0, lr.theta1, max(lr.raw_mileages))],
		'r'
	)

""" Displays the evolution of the loss over time, receiving an object as argument"""

def loss_progression(lr):
	plt.figure("Loss progression")
	plt.xlabel('Epoch')
	plt.ylabel('Loss')
	plt.plot([i for i in range(len(lr.loss_acc))], lr.loss_acc, 'r')