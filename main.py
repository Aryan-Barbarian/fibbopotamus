import numpy as np
from matrix import Matrix
import sys
# O(2^n)
def memoize(fn):
	seen = dict()
	def to_return(*args):
		if args not in seen:
			seen[args] = fn(*args)
		return seen[args]
	return to_return;

# O(n)
def normal(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return normal(n - 1) + normal(n - 2)

# O(log(n))
def dynamic(n):
	fn = memoize(normal)
	return fn(n);

def fastest(n):
	matrix = Matrix([[0, 1],[1, 1]])
	to_mult = Matrix([[0],[1]])
	ans = (matrix**n) * to_mult;
	return ans.row(0)[0];


def main():
	arg = sys.argv[1]

	try:
		n = int(arg)
	except ValueError:
		print("Argument must be an integer! Found: {}".format(raw_n))

	if (n <= 25):
		print "Normal: {} ".format(normal(n))
	else:
		print("n too high for normal")


	if (n <= 30):
		print "Dynamic: {} ".format(dynamic(n))
	else:
		print("n too high for dynamic")


	if (n <= 1000000):
		print "Fastest: {} ".format(fastest(n))
	else:
		print("n too high for fastest")


if __name__ == "__main__":
	main()