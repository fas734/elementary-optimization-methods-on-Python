import time

ALPHA = .6
BETTA = .4
PRECISION = .001
TIME_LIMIT = 1


def z(x):
	result = 70 * (x-2)**2 + 31
	return result


def f(x):
	x1 = x["x1"]
	x2 = x["x2"]
	result = 4 * (x1-5)**2 + 70 * (x2-2)**2 + 31
	return result


def time_dif(value):
	return (time.time() - value)


def iteration(a, b):
	delta = abs(b-a)

	x_a = a + ALPHA*delta
	x_b = a + BETTA*delta

	f_x_a = z(x_a)
	f_x_b = z(x_b)

	if (f_x_a < f_x_b):
		a = x_b
	else:
		b = x_a
	return {"a":a, "b":b, "delta":delta}
