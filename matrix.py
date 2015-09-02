def decompose_exponent(n):
	string = bin(n)[2:]; # something like 100110
	ans = list()
	for p in xrange(0, len(string)): # p is the power of 2 that we are dealing with
		index = len(string) - p - 1; # Index is where on the string to find that bit
		if string[index] == "1":
			ans.append(2**p);
	return ans;

class Matrix(object):
	def __init__(self, array):
		self.array = array; # Each entry is a row, so array[0] is the first row

	def shape(self):
		h = len(self.array)
		if h == 0:
			return (0, 0)
		w = len(self.array[0])
		return (w, h)

	def __pow__(self, n):
		if n == 2:
			return self.square()
		if n % 2 == 0:
			return (self**(n / 2))**2
		else:
			return self * (self**(n - 1))

	def col(self, i):
		ans = [row[i] for row in self.array]
		return ans;

	def row(self, i):
		return self.array[i];

	def __mul__(self, other):
		w1, h1 = self.shape()
		w2, h2 = other.shape()

		if (h2 != w1):
			return None
		
		w3, h3 = w2, h1 # Shape of our result matrix
		ans_array = [[0 for i in xrange(w3)] for j in xrange(h3)] # height of h3, width of w3, all zeros

		for i in xrange(h3): # i is index of row
			for j in xrange(w3): # j is index of col
				curr_row = self.row(i);
				curr_col = other.col(j);

				multiplied = [curr_col[k] * curr_row[k] for k in xrange(len(curr_col))]
				ans_array[i][j] = sum(multiplied);

		return Matrix(ans_array)

	def __str__(self):
		ans = "";
		for row in self.array:
			ans += "| "
			for val in row:
				ans += "{}, ".format(val)
			ans = ans[:-2]
			ans += " | \n"
		return ans;

	def square(self):
		return self * self;
