import numpy as np


def printSeparator(title):
	print('~~~~~~~~~ ' + title + ' ~~~~~~~~~~~~~~~~')
	pass


"""
NumPy’s main object is the homogeneous multidimensional array. It is a table of elements (usually numbers), 
all of the same type, indexed by a tuple of positive integers. In NumPy dimensions are called axes.


ndarray.ndim - the number of axes (dimensions) of the array.
ndarray.shape - the dimensions of the array. This is a tuple of integers indicating the size of the array in each dimension.
ndarray.size - the total number of elements of the array.
ndarray.dtype - an object describing the type of the elements in the array.
ndarray.itemsize - the size in bytes of each element of the array. 
ndarray.data - the buffer containing the actual elements of the array. Normally, we won’t need to use this attribute because we will access the elements in an array using indexing facilities.

np.arange(start, end, step)
np.ones(number of ones)
np.zeros(number of zeros)


Array Creation
arange, array, copy, empty, empty_like, eye, fromfile, fromfunction, identity, linspace, logspace, mgrid, ogrid, ones, ones_like, r, zeros, zeros_like

Conversions
ndarray.astype, atleast_1d, atleast_2d, atleast_3d, mat

Manipulations
array_split, column_stack, concatenate, diagonal, dsplit, dstack, hsplit, hstack, ndarray.item, newaxis, ravel, repeat, reshape, resize, squeeze, swapaxes, take, transpose, vsplit, vstack

Questions
all, any, nonzero, where

Ordering
argmax, argmin, argsort, max, min, ptp, searchsorted, sort

Operations
choose, compress, cumprod, cumsum, inner, ndarray.fill, imag, prod, put, putmask, real, sum

Basic Statistics
cov, mean, std, var

Basic Linear Algebra
cross, dot, outer, linalg.svd, vdot

"""

#Array Creation
printSeparator('Array Creation')

array1 = np.array([1,2,3,4,5,6,7,8,9,0])

print(array1)
print(array1.size)
print(array1.shape)
print(array1.dtype)


printSeparator('Array Creation - 2D')
array2 = np.array([(1,2,3), (8,9,0.1)])
print(array2)
print(array2.size)
print(array2.shape)
print(array2.dtype)


printSeparator('Array Creation - with DataType')
array3 = np.array([(1,2,3), (8,9,0)], dtype = complex)
print(array3)
print(array3.size)
print(array3.shape)
print(array3.dtype)


printSeparator('Array Creation - Zeroes')
zeroArray = np.zeros(9)
zeroArray_2D = np.zeros((3,4))
print(zeroArray)
print(zeroArray_2D)

printSeparator('Array Creation - Ones')
onesArray = np.ones(3)
print(onesArray)


printSeparator('Array Creation - Sequences')
countUpArray = np.arange(10)   
AP_Array = np.arange(10,20,1.2) # np.arange(first num, last num (excluded; less than), step)
countUpArray_2D = np.arange(20).reshape((4,5))
print(countUpArray)
print(AP_Array)
print(countUpArray_2D)


#Array indexing and Slicing 
printSeparator('Array indexing and Slicing - 1D')
aryX = np.array([1,2,3,4,5])
print(aryX)
print(aryX[1])
print(aryX[1:5])
print(aryX[::-1])

printSeparator('Array indexing and Slicing - 2D')
matX = np.array([(1,2,3),(11,22,33),(111,222,333)])
print(matX)
print(matX[1,2])   #matX[row,col]
print(matX[:,0])   #Get first column
print(np.diag(matX))

#Array Operations
#Arithmetic operators on arrays apply elementwise. A new array is created and filled with the result.
#elementwise
printSeparator('Array Operations')
seqX = np.array([1,20,3,5])
print(seqX + 2)
print(seqX * 5)
print(seqX // 2)
print(seqX >= 2)


printSeparator('Array Multiplication')
matrix1 = np.array([(1,3,7),(0,1,1),(9,6,9)])
matrix2 = np.array([(0,1,8),(1,5,1),(2,2,2)])

print(matrix1.ravel(), '\n\ns') # Flattern an array

matrix_elementWiseProduct = matrix2 * matrix1
matrix_multiplication = matrix1 @ matrix2 #dot Product
matrix_dotProduct = matrix1.dot(matrix2)


print(matrix_elementWiseProduct,'\n\n')
print(matrix_multiplication,'\n\n')
print(matrix_dotProduct,'\n\n')


#iteration
printSeparator('Numpy Array iteration')

for x in array1:
	print(x)

for x in matrix1:
	print(x)

pass

#Random
printSeparator('Random')
print(np.random.random((2,3)), '\n\n')
print(np.linspace(6,10), '\n\n')

#Stacking Arrays
printSeparator('Stacking Arrays')
matA = np.array([(1,2,3),(4,5,6)])
matB = np.array([(0,0,0),(0,0,0)])

print(np.vstack((matA, matB)), '\n\n')
print(np.hstack((matA,matB)), '\n\n')


"""
~~~~~~~~~ Array Creation ~~~~~~~~~~~~~~~~
[1 2 3 4 5 6 7 8 9 0]
10
(10,)
int32
~~~~~~~~~ Array Creation - 2D ~~~~~~~~~~~~~~~~
[[1.  2.  3. ]
 [8.  9.  0.1]]
6
(2, 3)
float64
~~~~~~~~~ Array Creation - with DataType ~~~~~~~~~~~~~~~~
[[1.+0.j 2.+0.j 3.+0.j]
 [8.+0.j 9.+0.j 0.+0.j]]
6
(2, 3)
complex128
~~~~~~~~~ Array Creation - Zeroes ~~~~~~~~~~~~~~~~
[0. 0. 0. 0. 0. 0. 0. 0. 0.]
[[0. 0. 0. 0.]
 [0. 0. 0. 0.]
 [0. 0. 0. 0.]]
~~~~~~~~~ Array Creation - Ones ~~~~~~~~~~~~~~~~
[1. 1. 1.]
~~~~~~~~~ Array Creation - Sequences ~~~~~~~~~~~~~~~~
[0 1 2 3 4 5 6 7 8 9]
[10.  11.2 12.4 13.6 14.8 16.  17.2 18.4 19.6]
[[ 0  1  2  3  4]
 [ 5  6  7  8  9]
 [10 11 12 13 14]
 [15 16 17 18 19]]
~~~~~~~~~ Array indexing and Slicing - 1D ~~~~~~~~~~~~~~~~
[1 2 3 4 5]
2
[2 3 4 5]
[5 4 3 2 1]
~~~~~~~~~ Array indexing and Slicing - 2D ~~~~~~~~~~~~~~~~
[[  1   2   3]
 [ 11  22  33]
 [111 222 333]]
33
[  1  11 111]
[  1  22 333]
~~~~~~~~~ Array Operations ~~~~~~~~~~~~~~~~
[ 3 22  5  7]
[  5 100  15  25]
[ 0 10  1  2]
[False  True  True  True]
~~~~~~~~~ Array Multiplication ~~~~~~~~~~~~~~~~
[1 3 7 0 1 1 9 6 9] 

s
[[ 0  3 56]
 [ 0  5  1]
 [18 12 18]] 


[[17 30 25]
 [ 3  7  3]
 [24 57 96]] 


[[17 30 25]
 [ 3  7  3]
 [24 57 96]] 


~~~~~~~~~ Numpy Array iteration ~~~~~~~~~~~~~~~~
1
2
3
4
5
6
7
8
9
0
[1 3 7]
[0 1 1]
[9 6 9]
~~~~~~~~~ Random ~~~~~~~~~~~~~~~~
[[0.35113211 0.24969512 0.70665035]
 [0.40362263 0.88822591 0.48457603]]
[Finished in 0.3s]

"""