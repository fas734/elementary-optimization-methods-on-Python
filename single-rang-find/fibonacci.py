import random
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)
import functions

									# initialize
a = random.randint(0, 13) - 1100	# random start of interval
b = random.randint(0, 13) + 1000	# random end of interval

print("\n--------------------------\nSTART Fibonacci method")

n = 2	# start finding n from 2
f_n_plus_2 = abs(b-a) / functions.PRECISION
n_find = functions.fib_bine(n)
print("f_n_plus_2 ", f_n_plus_2)
print("n_find     ", n_find)
while(f_n_plus_2 > n_find):
	n += 1
	n_find = functions.fib_bine(n)
	print("%d" % n_find)
n -= 2
print("Calculation requires %d iterations" % n)
