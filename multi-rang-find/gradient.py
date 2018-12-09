import random
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)
import functions
import sympy


x1 = sympy.Symbol('x1')	# symbol <x1>
x2 = sympy.Symbol('x2')	# symbol <x2>

x_sym = list()	# symbols of multidimensional variable
x_sym.append(x1)
x_sym.append(x2)

				# initialization of multidimensional variable
x = dict()		# access to each component is through symbolic key
for var_name in x_sym:
	x[str(var_name)] = random.randint(0, 22) - 13	# random value of x components

f_sym = 4 * (x1-5)**2 + 70 * (x2-2)**2 + 31	# symbolic function

if(len(sys.argv) > 1):				# user can set the <t> value, otherwise random [0.01, 0.99]
	t = float(sys.argv[1])
	if(len(sys.argv) >= 3):
		x['x1'] = float(sys.argv[2])
	if(len(sys.argv) == 4):
		x['x2'] = float(sys.argv[3])
else:
	t = random.randint(1,100) / 100

print("\n-------------------------\nSTART Gradient method")

print("X[0]")
for item in x.items():
	print(item)

print("t =", t)

grad_x = dict()
for key in x.keys():
	grad_x[key] = sympy.diff(f_sym, key, 1)

stop_iteration = False		# condition to stop: grad_x < PRECISION

time_start = functions.current_time()	# program started at <time_start> time

iteration_number = 0

for key in grad_x.keys():
	if(abs(grad_x[key].subs({key: x[key]})) < functions.PRECISION):	# grad_x < PRECISION?
		stop_iteration = True
		break

while((not stop_iteration) & (iteration_number<functions.ITERATION_LIMIT)):
	iteration_number += 1
	for key in x.keys():
		print('x[', key, ']', x[key], sep='')
		x[key] = x[key] - t*grad_x[key].subs({key: x[key]})
		print('x[', key, ']', x[key], sep='')

	for key in grad_x.keys():
		if(abs(grad_x[key].subs({key: x[key]})) < functions.PRECISION):	# grad_x < PRECISION?
			stop_iteration = True

time_calculation = functions.time_dif(time_start)

for key in grad_x.keys():
	print("grad_x['", key, "'] := ", grad_x[key], " = ", grad_x[key].subs({key:x[key]}), sep='')

print("\nRESULT")
print("\niterations   ", iteration_number)
print("calculation time % .5f" % time_calculation)
print("--------------------------\n")

########################## PYTHON HISTORY: .python_history #######################
