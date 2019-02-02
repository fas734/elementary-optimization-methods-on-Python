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


def info():
	print("run program as:\npython fastest.py (g|d) [x1] [x2] ... [xn]\n \
		g - golden ratio method\n \
		d - dichotomy method\n \
		xi - value of i-th element of X\n\n \
		Golden ratio method will be used as default.\n")

# ************************ functions finding <t> BEGIN *********************
# dichotomy BEGIN
def dichotomy(f_sym_t, delta = 0):
	a = random.randint(0, 13) - 1000	# random start of interval
	b = random.randint(0, 13) + 900		# random end of interval
	if(delta == 0):
		delta = random.uniform(0, functions.PRECISION)
	
	while (True):
		x_l1 = (a+b)/2 - delta
		x_l2 = (a+b)/2 + delta

		f_a = f_sym_t.subs({sym_t: a})
		f_b = f_sym_t.subs({sym_t: b})
		f_x_1 = f_sym_t.subs({sym_t: x_l1})
		f_x_2 = f_sym_t.subs({sym_t: x_l2})

		# make sure interval is OK:
		if(((f_a > f_x_1) | (f_a > f_x_2)) & ((f_b > f_x_2) | (f_b > f_x_1))):
			break
		else:
			a -= 1000
			b += 1000

	time_start = functions.current_time()	# program started at <time_start> time
	iteration_number = 1

	while (True):
		x_l1 = (a+b)/2 - delta
		x_l2 = (a+b)/2 + delta

		f_x_1 = f_sym_t.subs({sym_t: x_l1})
		f_x_2 = f_sym_t.subs({sym_t: x_l2})

		if (f_x_1 < f_x_2):
			b = x_l2
		else:
			a = x_l1
		interval_length = abs(b-a)
		
		time_calculation = functions.time_dif(time_start)

		if (interval_length < functions.PRECISION):			# compare with precision
			break
		if (time_calculation > functions.TIME_LIMIT):	# nobody wants to wait too much
			print("WARNING: long time calculation. interval_length: %.4f" % interval_length)
			break
		iteration_number += 1

	return((a+b) / 2)
# dichotomy END


# golden ratio BEGIN
def golden_ratio(f_sym_t):
	a = random.randint(0, 13) - 1000	# random start of interval
	b = random.randint(0, 13) + 900		# random end of interval

	while (True):
		interval_length = abs(b-a)

		x_alpha = a + functions.ALPHA*interval_length
		x_betta = a + functions.BETTA*interval_length

		f_a = f_sym_t.subs({sym_t: a})
		f_b = f_sym_t.subs({sym_t: b})
		f_x_alpha = f_sym_t.subs({sym_t: x_alpha})
		f_x_betta = f_sym_t.subs({sym_t: x_betta})

		# make sure interval is OK:
		if(((f_a > f_x_alpha) | (f_a > f_x_betta)) & ((f_b > f_x_betta) | (f_b > f_x_alpha))):
			break
		else:
			a -= 1000
			b += 1000

	time_start = functions.current_time()	# program started at <time_start> time
	iteration_number = 1

	while (True):
		interval_length = abs(b-a)

		x_alpha = a + functions.ALPHA*interval_length
		x_betta = a + functions.BETTA*interval_length

		f_x_alpha = f_sym_t.subs({sym_t: x_alpha})
		f_x_betta = f_sym_t.subs({sym_t: x_betta})

		if (f_x_alpha < f_x_betta):
			a = x_betta
		else:
			b = x_alpha

		interval_length = abs(b-a)

		time_calculation = functions.time_dif(time_start)

		if (interval_length < functions.PRECISION):			# compare with precision
			break
		if (time_calculation > functions.TIME_LIMIT):	# nobody wants to wait too much
			print("WARNING: long time calculation. interval_length: %.4f" % interval_length)
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
	if not ((str(sys.argv[1])=='g') | (str(sys.argv[1])=='d')):
		info()
else:
	info()
	find_t = golden_ratio
# ************************* initialization END *****************************


# ************************* find grad BEGIN ********************************
print("\n-------------------------\nSTART Fastest method")

if(len(sys.argv) > 1):
	if((str(sys.argv[1])=='g') | (str(sys.argv[1])=='d')):
		if(str(sys.argv[1]) == 'g'):
			find_t = golden_ratio
			print(" using GOLDEN RATIO method inside\n")
		if(str(sys.argv[1]) == 'd'):
			find_t = dichotomy
			print(" using DICHOTOMY method inside\n")
	else:
		find_t = golden_ratio

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

	t = find_t(f_sym_t)
	# print("t:", t)
	# print("\nx_sym_t\n",x_sym_t,"\nf_sym_t\n",f_sym_t)
	for key in x.keys():
		x[key] = x_sym_t[key].subs({sym_t: t})
		# print(key, x[key])

	for key in grad_x.keys():
		if(abs(grad_x[key].subs({key: x[key]})) < functions.PRECISION):	# grad_x < PRECISION?
			stop_iteration = True
			break

time_calculation = functions.time_dif(time_start)
# ************************* iteration END *************************

print("\n\nRESULT\n")
for key in x.keys():
	print("x[%s] = % .3f" % (key, x[key]))
for key in grad_x.keys():
	print("grad_x['%s']: %15s = % 7.3f" % (key,grad_x[key], grad_x[key].subs({key: x[key]})))

print("\n%s = % 7.3f" % (f_syms, f_syms.subs({sym_x1: x['x1'], sym_x2: x['x2']})))
print("\niterations   ", iteration_number)
print("calculation time % .5f" % time_calculation)
print("--------------------------\n")

# ************************* ALGORITHM itself END ***************************
