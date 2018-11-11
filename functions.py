import math
from time import time as current_time

ALPHA = .6			# for golden ratio method
BETTA = .4			# for golden ratio method
PRECISION = .001	# precision of calculation
TIME_LIMIT = 7		# calculation time limit in seconds


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


def fib_binet(n):	# returns fibonacci function value of <n>
	result = (((1+math.sqrt(5))/2)**n - ((1-math.sqrt(5))/2)**n) \
				/ math.sqrt(5)
	return(result)


def golden_ratio_iteration(a, b):	# one golden ratio iteration
	interval_length = abs(b-a)

	x_a = a + ALPHA*interval_length
	x_b = a + BETTA*interval_length

	f_x_a = z(x_a)
	f_x_b = z(x_b)

	if (f_x_a < f_x_b):
		a = x_b
	else:
		b = x_a

	interval_length = abs(b-a)

	return {"a":a, "b":b, "interval_length":interval_length}	# returns new interval


def dichotomy_iteration(a, b, delta):
	x_l1 = (a+b)/2 - delta
	x_l2 = (a+b)/2 + delta

	f_x_1 = z(x_l1)
	f_x_2 = z(x_l2)

	if (f_x_1 < f_x_2):
		b = x_l2
	else:
		a = x_l1

	interval_length = abs(b-a)

	return {"a":a, "b":b, "interval_length":interval_length}	# returns new interval


def fib_iteration(a, b, k, n):	# one fibonacci iteration
	interval_length = abs(b-a)

	x_a = a + (fib_binet(n-k-2)/fib_binet(n-k))*interval_length
	x_b = a + (fib_binet(n-k-1)/fib_binet(n-k))*interval_length

	f_x_a = z(x_a)
	f_x_b = z(x_b)

	if (f_x_a < f_x_b):
		b = x_b
	else:
		a = x_a

	return {"a":a, "b":b}	# returns new interval
