from time import time as current_time

ALPHA = .6			# for golden ratio method
BETTA = .4			# for golden ratio method
PRECISION = .001	# precision of calculation
TIME_LIMIT = 1		# calculation time limit in minutes


def z(x):
	result = 70 * (x-2)**2 + 31
	return result


def f(x):
	x1 = x["x1"]
	x2 = x["x2"]
	result = 4 * (x1-5)**2 + 70 * (x2-2)**2 + 31
	return result


def time_dif(value):		# time difference between now and <value> moments
	return (current_time() - value)


def golden_ratio_iteration(a, b):	# one golden ratio iteration
	delta = abs(b-a)

	x_a = a + ALPHA*delta
	x_b = a + BETTA*delta

	f_x_a = z(x_a)
	f_x_b = z(x_b)

	if (f_x_a < f_x_b):
		a = x_b
	else:
		b = x_a
	return {"a":a, "b":b, "delta":delta}	# returns new interval
