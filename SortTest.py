import numpy as np
import time

# ------------------------------------
def sortarray_builtin(A):
	'''This is built in Python sort function'''
	return sorted(np.copy(A))

# ------------------------------------
def sortarray_bubble(A):
	'''Bubble sorting algorithm -- is a simplest of sorting algorithms.
		Perfomance: O(n**2)''' 
	B = np.copy(A)
	for i in range(len(A)-1):
		for j in range(i,len(A)):
			if B[i] > B[j]:
				B[i],B[j] = B[j],B[i]
	return B

# ------------------------------------	
def sortarray_insertions(A):	
	'''Insertion sorting algorithm -- standard realisation
		Perfomance: O(n**2)'''
	B = np.copy(A)
	for i in range(1,len(B)):
		k = B[i]
		j = i - 1
		while j >= 0 and B[j] > k:
			B[j+1] = B[j]
			j -=1
		B[j+1] = k
	return B	

# ------------------------------------
def sortarray_insertions_my(A):	
	'''Insertion sorting algorithm -- my custom Python-specific realisation
		Perfomance: O(n**2)
		The best performance time among insertions algorithms in python'''
	B = []
	for i in range(len(A)):
		k = A[i]
		j = i - 1
		while j >= 0:
			if B[j] < k: break
			j -= 1
		B.insert(j+1, k)
	return B	

# -------------------------------------
def sortarray_gnome(A):
	'''Gnome sorting algorithm
		Perfomance: O(n**2)'''
	B = np.copy(A)
	i,j = 1,2
	L = len(B)
	while i < L:
		if B[i-1] < B[i]:
			i = j
			j = j + 1
		else:
			B[i-1],B[i] = B[i],B[i-1]
			i = i - 1
			if i == 0:
				i = j
				j = j + 1
	return B
	
# -------------------------------------
def sortarray_cocktail(A):
	'''Cocktail shaker sorting alogorithm -- improoved bubble sort
		Perfomance: O(n**2)
		The sample code was taken from here: https://cutt.ly/qrxDTBr'''
	B = np.copy(A)
	left  = 0
	right = len(B) - 1
	while left <= right:
		for i in range(left, right, +1):
			if B[i] > B[i + 1]:
				B[i], B[i + 1] = B[i + 1], B[i]
		right -= 1
		for i in range(right, left, -1):
			if B[i - 1] > B[i]:
				B[i], B[i - 1] = B[i - 1], B[i]
		left += 1
	return B

# -------------------------------------
def sortarray_shell(A):
	'''Shell sort algorithm -- one of the fastest
		Author: Donald Lewis Shell
		Performance: O(nlogn)'''
	B = np.copy(A)
	L = len(B)
	gap = L >> 1
	while gap > 0:
		for i in range(gap, L):
			j = i - gap
			while (j >= 0) and (B[j] > B[j+gap]):
				B[j],B[j+gap] = B[j+gap],B[j]
				j -= gap
		gap >>= 1
	return B
	
# ============= Testing functions and decorators 
def IsSorted(A):
	for i in range(len(A)-1):
		if A[i]>A[i+1]:
			return False
	return True

def Randomize(A, iterations=1):
	L = len(A)
	if L < 2:
		return
	B = np.copy(A)
	for i in range(iterations):
		i2 = i1 = np.random.randint(L)
		while i2 == i1:
			i2 = np.random.randint(L)
		B[i1],B[i2] = B[i2],B[i1]
	return B
	
def RandomizeAll(A):
	B = np.copy(A)
	L = len(B)
	for i in range(L):
		while True:
			j = np.random.randint(L)
			if i != j: break
		B[i],B[j] = B[j],B[i]
	return B

def decor_tst_cases(iters=10):
	# print(iters.__name__, flush=True)
	def decorator(func):
		def wrapper(*args, **kwargs):
			print("\t\tSorting tests : ", end='', flush=True)
			ret = True
			i = 1
			total = 0
			while i < iters+1 and ret:
				print(i, end=',', flush=True)
				# randomized = RandomizeAll(*args)
				randomized = Randomize(*args, iterations=iters)
				start = time.time()
				sorted = func(randomized, **kwargs)
				# ret &= IsSorted(func(Randomize(*args, iters),**kwargs))				
				end = time.time()
				ret &= IsSorted(sorted)
				total += (end - start)
				i += 1
			if ret:
				print(" Passed.")
			else:
				print(" Failed!!!")
			print("\t\tTime elapsed: {:.3f} seconds.".format(total))
			return ret, total,
		return wrapper
	return decorator

# ============= Test Cases

sorting_algorithmes = [
	sortarray_builtin,
	sortarray_shell,
	sortarray_bubble,
	sortarray_cocktail,
	sortarray_insertions,
	sortarray_insertions_my,
	sortarray_gnome,
]

test_iterations = 20
arraysize       = 500
rnd = np.random.randint(arraysize, size=arraysize)

mintime = test_iterations*arraysize
for i, SortFunc in enumerate(sorting_algorithmes):
	case = '\n+++ Case '
	if i < 11: case += '0'
	case += str(i+1)+':'
	print(case)
	print("\t\t"+SortFunc.__doc__)
	# decorate sorting function:
	tst_case = decor_tst_cases(test_iterations)(SortFunc)
	result, timetotal = tst_case(rnd)
	if result and timetotal < mintime:
		TheBestSortingAlgorithm = SortFunc
		mintime = timetotal
	
print("\n+++ S U M A R Y +++")
print("\t\tThe best sorting algorithm is '"+TheBestSortingAlgorithm.__name__+"()'\n\t\tWith total time={:.3f} seconds for array size={} and {} iterations.".format(mintime, arraysize, test_iterations))

