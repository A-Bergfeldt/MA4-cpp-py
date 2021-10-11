#!/usr/bin/env python3

from integer import Integer
from time import perf_counter as pc
import matplotlib as plt

def fib_py(n):
	if n <= 1:
		return n
	else:
		return(fib_py(n-1) + fib_py(n-2)) 

def main():
	start_fib = 10
	end_fib = 20
	py_time = []
	cpp_time = []
	fib_vals = list(range(start_fib, end_fib))

	for val in fib_vals:

		# python
		start = pc()
		print(f"Calculating fib {val} with py")
		temp = fib_py(val)		
		end = pc()
		print(f"Finished calculating fib {val} with py")
		time = end - start
		py_time.append(time)

		#c++
		start = pc()
		f = Integer(val)
		print(f"Calculating fib {val} with c++")
		temp = f.fib()
		end = pc()
		print(f"Finished calculating fib {val} with c++")
		time = end - start
		cpp_time.append(time)

	plt.xlim([start_fib, end_fib])
	plt.xlabel('Fib nr calculated')
	plt.ylabel('TTime to calculate')
	plt.plot(fib_vals, py_time, c = 'b', label ='Fib time - py')
	plt.plot(fib_vals, cpp_time, c ='r', label = 'Fib time - c++')
	plt.show()
	


if __name__ == '__main__':
	main()