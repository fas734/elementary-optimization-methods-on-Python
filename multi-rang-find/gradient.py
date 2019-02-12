# user can run program with parameters:
#	gradient.py		<t> <x1> <x2>

import random
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)
import functions
import sympy


# ************************* initialization BEGIN *************************
sym_x1 = sympy.Symbol('x1')	# symbol <x1>
sym_x2 = sympy.Symbol('x2')	# symbol <x2>

x_syms = list()	# symbols of multidimensional variable
x_syms.append(sym_x1)
x_syms.append(sym_x2)

f_sym = 4 * (sym_x1-5)**2 + 70 * (sym_x2-2)**2 + 31	# symbolic function

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
# ************************* initialization END *************************


# ************************* find grad_x, t BEGIN *************************
print("\n-------------------------\nSTART Gradient method\n")

print("     X[0]")
for key in x.keys():
	print("x[%s] = % .3f" % (key, x[key]))

grad_x = dict()					# gradient contains derivatives
for key in x.keys():
	grad_x[key] = sympy.diff(f_sym, key, 1)		# derivative of f_sym by key, order 1

max_grad_x_0 = abs(grad_x['x1'].subs({sym_x1: x['x1']}))		# find max value of grad to generate <t> parameter
for key in grad_x.keys():
	if(abs(grad_x[key].subs({key: x[key]})) > max_grad_x_0):
		max_grad_x_0 = abs(grad_x[key].subs({key: x[key]}))

if(len(sys.argv)>1):		# user can set the <t> value
	if(float(sys.argv[1])!=0):
		t = float(sys.argv[1])
	else:
		t = 1 / float(max_grad_x_0)
else:
	t = 1 / float(max_grad_x_0)
print("t =", t)
# ************************* find t END *************************


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
	for key in x.keys():
		x[key] = x[key] - t*grad_x[key].subs({key: x[key]})		# iteration itself
		# print('x[', key, ']', x[key], sep='')			# 'debug' line
	# print()											# 'debug' line

	for key in grad_x.keys():
		if(abs(grad_x[key].subs({key: x[key]})) < functions.PRECISION):	# grad_x < PRECISION?
			stop_iteration = True
			break

time_calculation = functions.time_dif(time_start)
# ************************* iteration END *************************


print("\n\nRESULT\n")

for key in x.keys():
	print("x[%s] = % .6f" % (key, x[key]))
print()
for key in grad_x.keys():
	print("grad_x['%s']: %15s = % 7.4f" % (key,grad_x[key], grad_x[key].subs({key: x[key]})))

print("\n%s = % 7.6f" % (f_sym, f_sym.subs({sym_x1: x['x1'], sym_x2: x['x2']})))
print("\niterations   ", iteration_number)
print("calculation time % .6f" % time_calculation)
print("--------------------------\n")
