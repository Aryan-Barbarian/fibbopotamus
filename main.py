import numpy as np
import datetime
from matrix import Matrix
import sys
import csv
import pandas as pd
import matplotlib.pyplot as plt

def memoize(fn):
	seen = dict()
	def to_return(*args):
		if args not in seen:
			seen[args] = fn(*args)
		return seen[args]
	return to_return;

def normal(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return normal(n - 1) + normal(n - 2)

def dynamic(n):
	if n == 0:
		return 0

	curr = 1
	prev = 0

	while n > 1:
		prev, curr = curr, prev + curr
		n -= 1

	return curr

	

def fastest(n):
	matrix = Matrix([[0, 1],[1, 1]])
	to_mult = Matrix([[0],[1]])
	ans = (matrix**n) * to_mult;
	return ans.row(0)[0];

def time_to_execute(fn, *args):
	a = datetime.datetime.now()
	fn(*args);
	b = datetime.datetime.now()
	c = b - a
	return c.microseconds

def profile(max_n):

	df_dict = dict()
	df_dict["dynamic"] = [time_to_execute(dynamic, i) for i in xrange(2, max_n)]
	df_dict["fastest"] = [time_to_execute(fastest, i) for i in xrange(2, max_n)]
	
	df = pd.DataFrame(df_dict)
	ax = df.plot()
	fig = ax.get_figure()
	fig.savefig('profile.png')

def main():
	arg = sys.argv[1]
	if (arg == "profile"):
		raw_n = sys.argv[2]
	else:
		raw_n = arg
	try:
		n = int(raw_n)
	except ValueError:
		print("Argument must be an integer! Found: {}".format(arg))

	if (arg == "profile"):
		profile(n)
		return
	if (n <= 30):
		print "Normal: {} ".format(normal(n))
	else:
		print("n too high for normal")


	if (n <= 1000000):
		print "Dynamic: {} ".format(dynamic(n))
	else:
		print("n too high for dynamic")


	if (n <= 1000000):
		print "Fastest: {} ".format(fastest(n))
	else:
		print("n too high for fastest")


if __name__ == "__main__":
	main()