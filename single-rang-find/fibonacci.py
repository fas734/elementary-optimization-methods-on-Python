# user can run program with parameters:
#	fibonacci.py		<a> <b>
#		where <a> <b> is interval

import random
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)
import functions

									# initialize
a = random.randint(0, 13) - 1000	# random start of interval
b = random.randint(0, 13) + 900		# random end of interval

if(len(sys.argv) > 1):			# user can set the <a> <b> value
	if(len(sys.argv)>=2):
		if(float(sys.argv[1])!=0):
			a = float(sys.argv[1])
	if(len(sys.argv)>=3):
		if(float(sys.argv[2])!=0):
			b = float(sys.argv[2])

print("\n-------------------------\nSTART Fibonacci method")

f_x = functions.z(a)			# value of function at <a> point after initialization
print("a % 9.5f   f(a) % 9.5f" % (a, f_x))
f_x = functions.z(b)			# value of function at <b> point after initialization
print("b % 9.5f   f(b) % 9.5f" % (b, f_x))

n = 3				# start finding n from 3
f_n = abs(b-a) / functions.PRECISION	# value of fibonacci function should be at least <f_n>
f_n_find = functions.fib_binet(n)
print("f_n should be >= %d" % f_n)
while(f_n > f_n_find):
	n += 1
	f_n_find = functions.fib_binet(n)
print("fibonacci(%d) == %d" % (n, f_n_find))
print("Calculation requires %d iterations" % n)

time_start = functions.current_time()	# program started at <time_start> time

iteration_number = 1

while(iteration_number < n):
	fibonacci = functions.fib_iteration(a,b,iteration_number,n)

	a = fibonacci["a"]
	b = fibonacci["b"]
	interval_length = fibonacci["interval_length"]

	time_calculation = functions.time_dif(time_start)
	if (time_calculation > functions.TIME_LIMIT):	# nobody wants to wait too much
		print("WARNING: long time calculation")
		break
	iteration_number += 1

print("\nRESULT")
f_x = functions.z(a)
print("a % 9.5f   f(a) % 9.5f" % (a, f_x))
f_x = functions.z(b)
print("b % 9.5f   f(b) % 9.5f" % (b, f_x))
print("interval_length ", interval_length)
print("\niterations   ", iteration_number)
print("calculation time % .5f\n-------------------------\n" % time_calculation)
