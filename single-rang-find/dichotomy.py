# user can run program with parameters:
#	dichotomy.py		<a> <b> <delta>
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
delta = random.uniform(0, functions.PRECISION/2)

if(len(sys.argv) > 1):			# user can set the <a> <b> <t> value
	if(len(sys.argv)>=2):
		if(float(sys.argv[1])!=0):
			a = float(sys.argv[1])
	if(len(sys.argv)>=3):
		if(float(sys.argv[2])!=0):
			b = float(sys.argv[2])
	if(len(sys.argv)>=4):
		if(float(sys.argv[3])!=0):
			delta = float(sys.argv[3])

print("\n--------------------------\nSTART Dichotomy method")

f_x = functions.z(a)			# value of function at <a> point after initialization
print("a % 9.5f   f(a) % 9.5f" % (a, f_x))
f_x = functions.z(b)			# value of function at <b> point after initialization
print("b % 9.5f   f(b) % 9.5f" % (b, f_x))
print("delta %.5f" % delta)

time_start = functions.current_time()	# program started at <time_start> time

iteration_number = 1

while (True):
	dichotomy = functions.dichotomy_iteration(a, b, delta)	# make one iteration
	
	a = dichotomy["a"]
	b = dichotomy["b"]
	interval_length = dichotomy["interval_length"]
	
	time_calculation = functions.time_dif(time_start)

	if (interval_length < functions.PRECISION):			# compare with precision
		break
	if (time_calculation > functions.TIME_LIMIT):	# nobody wants to wait too much
		print("WARNING: long time calculation caused by very big value of delta (too close to PRECISION)")
		break
	iteration_number += 1

print("\nRESULT")
f_x = functions.z(a)
print("a % 9.5f   f(a) % 9.5f" % (a, f_x))
f_x = functions.z(b)
print("b % 9.5f   f(b) % 9.5f" % (b, f_x))
print("interval_length ", interval_length)
print("\niterations   ", iteration_number)
print("calculation time % .5f\n--------------------------\n" % time_calculation)
