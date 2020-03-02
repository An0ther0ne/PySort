# PySort
Testing perfomance of classic sorting algorithms in Python.
# Synopsis
    python [-O] SortTest.py [[-v]|[-vv]]
Where:
* -O   : turn DEBUG flag to off
* -v   : verbose level 1
* --vv : verbose level 2
# Explanation
This program designed for purpose of testing performance and accuracy of various sorting algorithms. 
We wraps with decorator each of those algorithm. And decorator runs for us the specified number of tests for each sorting algorithm, notice result (passed or not) of it and calcuate total elapsed time for all amount of tests in this case.
The testing procedure is to check all array elements are sorted in ascending order. Each time after this check an array is randomized again.
If at least one of test is fail – wrapper skip all following and return the failed state.
For total time calculation purpose only effective runtime of each successfully completed sorting function counts.
At the end of all tests, name of the fastest algorithm is determined and displayed.
For comparison, also shown a total time for built into Python sorting algorithm, but which is not considered in the summary championship result, because it is not implemented by the Python language itself.     
    
# Files:
* [SortTest.py](SortTest.py)
* [pylint.config](pylint.config) - my PyLint custom configuration file for this project.

# Requirements
* Python 3.x
* NumPy
# Output
+++ Case 01:

		This is built in Python sort function
		Sorting tests : 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20, Passed.
		Time elapsed: 0.003 seconds.

+++ Case 02:

		Shell sort algorithm -- one of the fastest
		Author: Donald Lewis Shell
		Performance: O(NlogN)
		Sorting tests : 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20, Passed.
		Time elapsed: 0.089 seconds.

+++ Case 03:

		Quick sort algorithm -- the fastest, but deep level of recursion needed
		Performance: O(NlogN), recursion level ~ N
		Sorting tests : 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20, Passed.
		Time elapsed: 0.052 seconds.

+++ Case 04:

		Bubble sorting algorithm -- is a simplest of sorting algorithms. Classic variant.
		Perfomance: O(N**2)
		Sorting tests : 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20, Passed.
		Time elapsed: 1.321 seconds.

+++ Case 05:

		Bubble sorting algorithm -- is a simplest of sorting algorithms. Variant with enumerate() usage.
		Perfomance: O(N**2)
		Sorting tests : 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20, Passed.
		Time elapsed: 1.810 seconds.

+++ Case 06:

		Cocktail shaker sorting alogorithm -- improoved bubble sort
		Perfomance: O(N**2)
		The sample code was taken from here: https://cutt.ly/qrxDTBr
		Sorting tests : 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20, Passed.
		Time elapsed: 1.594 seconds.

+++ Case 07:

		Insertion sorting algorithm -- standard realisation
		Perfomance: O(N**2)
		Sorting tests : 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20, Passed.
		Time elapsed: 0.608 seconds.

+++ Case 08:

		Insertion sorting algorithm -- my custom Python-specific realisation
		Perfomance: O(N**2)
		The best performance time among insertions algorithms in python
		Sorting tests : 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20, Passed.
		Time elapsed: 0.127 seconds.

+++ Case 09:

		Gnome sorting algorithm
		Perfomance: O(N**2)
		Sorting tests : 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20, Passed.
		Time elapsed: 1.284 seconds.

+++ S U M M A R Y +++

		The best sorting algorithm is 'sortarray_quick()'
		With total time=0.052 seconds for array size=500 and 20 iterations.
		
# LINKS
1. [DONALD E. KNUTH "The Art Of Computer Programming, Volume 3: Sorting and Searching."](https://linuxnasm.be/media/pdf/donald-knuth/taocp/volume-3/taocp-vol3-sorting-searching.pdf)
2. [WIKI Sorting algorithm](https://en.wikipedia.org/wiki/Sorting_algorithm)
3. [WIKI explanation for Cocktail shaker sorting](https://ru.wikipedia.org/wiki/%D0%A1%D0%BE%D1%80%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%BA%D0%B0_%D0%BF%D0%B5%D1%80%D0%B5%D0%BC%D0%B5%D1%88%D0%B8%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5%D0%BC)

# AUTHOR
   An0ther0ne
