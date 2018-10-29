import time


def z(x):
	result = 70 * (x-2)**2 + 31
	return result


def f(x):
	result = 4 * (x1-5)**2 + 70 * (x2-2)**2 + 31
	return result


def time_dif(value):
	return (time.time() - value)





import random
ALPHA = .6
BETTA = .4
PRECISION = .001
TIME_LIMIT = 1


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


a = random.randint(0, 13) - 1000
b = random.randint(0, 13) + 900

print("\nSTART")
f_x = z(a)
print("a % 9.5f   f(a) % 9.5f" % (a, f_x))
f_x = z(b)
print("b % 9.5f   f(b) % 9.5f" % (b, f_x))
time_start = time.time()

iteration_number = 1

while (True):
	golden_ratio = iteration(a, b)
	a = golden_ratio["a"]
	b = golden_ratio["b"]
	delta = golden_ratio["delta"]
	time_calculation = time_dif(time_start)
	if delta < PRECISION:
		break
	if (time_calculation//60 > TIME_LIMIT):
		break
	iteration_number += 1

print("\nRESULT")
f_x = z(a)
print("a % 9.5f   f(a) % 9.5f" % (a, f_x))
f_x = z(b)
print("b % 9.5f   f(b) % 9.5f" % (b, f_x))
print("iterations ", iteration_number)
print("calculation time ", time_calculation)
