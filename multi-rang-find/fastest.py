# user can run program with parameters:
#	fastest.py	<method> <x1> <x2>
#		where <method> == 'd' if dichotomy, 'g' if golden ratio

import random
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)
import functions
import sympy


# ************************ functions finding <t> BEGIN *********************
# dichotomy BEGIN
def dichotomy():
	a = random.randint(0, 13) - 1000	# random start of interval
	b = random.randint(0, 13) + 900		# random end of interval
	delta = random.uniform(0, functions.PRECISION)

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

	return((a+b) / 2)
# dichotomy END


# golden ratio BEGIN
def golden_ratio():
	a = random.randint(0, 13) - 1000	# random start of interval
	b = random.randint(0, 13) + 900		# random end of interval

	time_start = functions.current_time()	# program started at <time_start> time
	iteration_number = 1

	while (True):
		golden_ratio = functions.golden_ratio_iteration(a, b)	# make one iteration
		
		a = golden_ratio["a"]
		b = golden_ratio["b"]
		interval_length = golden_ratio["interval_length"]
		
		time_calculation = functions.time_dif(time_start)

		if (interval_length < functions.PRECISION):			# compare with precision
			break
		if (time_calculation > functions.TIME_LIMIT):	# nobody wants to wait too much
			print("ERROR: bad limits caused long time calculation (more than ", functions.TIME_LIMIT, " seconds).")
			break
		iteration_number += 1

	return((a+b) / 2)
# golden ratio END
# ************************ finding <t> functions END ***********************


# ************************* ALGORITHM itself BEGIN *************************
# ************************* initialization BEGIN ***************************
sym_t = sympy.Symbol('t')	# symbol <t>
sym_x1 = sympy.Symbol('x1')	# symbol <x1>
sym_x2 = sympy.Symbol('x2')	# symbol <x2>

x_syms = list()	# symbols of multidimensional variable
x_syms.append(sym_x1)
x_syms.append(sym_x2)

f_syms = 4 * (sym_x1-5)**2 + 70 * (sym_x2-2)**2 + 31	# symbolic function

				# initialization of multidimensional variable
x = dict()		# access to each component is through symbolic key
for var_name in x_syms:
	x[str(var_name)] = float(random.randint(0, 22) - 13)	# random value of x components

if(len(sys.argv) > 1):			# user can set the <x1> <x2> value
	if(len(sys.argv)>=3):
		if(float(sys.argv[2])!=0):
			x['x1'] = float(sys.argv[2])
	if(len(sys.argv)>=4):
		if(float(sys.argv[3])!=0):
			x['x2'] = float(sys.argv[3])
# ************************* initialization END *****************************


# ************************* find grad BEGIN ********************************
print("\n-------------------------\nSTART Fastest method\n")

print("     X[0]")
for key in x.keys():
	print("x[%s] = % .3f" % (key, x[key]))

grad_x = dict()					# gradient contains derivatives
for key in x.keys():
	grad_x[key] = sympy.diff(f_syms, key, 1)		# derivative of f_syms by key, order 1
# ************************* find grad END *************************


# ************************* iteration BEGIN *************************
stop_iteration = False				# condition to stop: grad_x[i] < PRECISION
time_start = functions.current_time()	# program started at <time_start> time
iteration_number = 0

for key in grad_x.keys():
	if(abs(grad_x[key].subs({key: x[key]})) < functions.PRECISION):	# grad_x < PRECISION?
		stop_iteration = True
		break

while((not stop_iteration) & (iteration_number<functions.ITERATION_LIMIT)):
	iteration_number += 1

	x_sym_t = dict()		# each component contains symbol <t>
	for key in x.keys():
		x_sym_t[key] = x[key] - sym_t * grad_x[key].subs({key: x[key]})	# iteration itself

	f_sym_t = f_syms		# f_sym_t will contain only symbol <t>, not syms <x1>, <x2>
	for key in x.keys():
		f_sym_t = f_sym_t.subs({key: x_sym_t[key]})

# print("x_sym_t\n",x_sym_t,"\n",f_sym_t)


# ************************* ALGORITHM itself END ***************************
