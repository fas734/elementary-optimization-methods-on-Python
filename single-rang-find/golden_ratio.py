import random
import functions


a = random.randint(0, 13) - 1000
b = random.randint(0, 13) + 900

print("\nSTART Golden ratio method")
f_x = functions.z(a)
print("a % 9.5f   f(a) % 9.5f" % (a, f_x))
f_x = functions.z(b)
print("b % 9.5f   f(b) % 9.5f" % (b, f_x))
time_start = functions.time.time()

iteration_number = 1

while (True):
	golden_ratio = functions.iteration(a, b)
	
	a = golden_ratio["a"]
	b = golden_ratio["b"]
	delta = golden_ratio["delta"]
	
	time_calculation = functions.time_dif(time_start)

	if delta < functions.PRECISION:
		break
	if (time_calculation//60 > functions.TIME_LIMIT):
		print("ERROR: bad limits caused long time calculation (more than ", functions.TIME_LIMIT, " seconds.")
		break
	iteration_number += 1

print("\nRESULT")
f_x = functions.z(a)
print("a % 9.5f   f(a) % 9.5f" % (a, f_x))
f_x = functions.z(b)
print("b % 9.5f   f(b) % 9.5f" % (b, f_x))
print("iterations ", iteration_number)
print("calculation time ", time_calculation)
