import random
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)
import functions
import sympy


# ************************* initialization begin *************************
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
# ************************* initialization end *************************
