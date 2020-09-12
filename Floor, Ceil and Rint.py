import numpy
A= numpy.array(input().split(),float)
numpy.set_printoptions(legacy='1.13')
print(numpy.floor(A),numpy.ceil(A),numpy.rint(A),sep='\n')



