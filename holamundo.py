import numpy as np
def convolution ( A, B ):
    C = np . zeros ((len ( A ) - 2 , len ( A [ 0 ]) - 2))
    n = o
    for i in range (len(C)):
        for j in range (len(C [ 0 ])):
            result = 0 
            for iaux in range (len(B)):
                for jaux in range (len(B[ 0 ])):
                    result += A [i + iaux] [i + jaux] * B [iaux] [jaux]
            C [i] [j] = result
    return C
matriz1 = [[6,9,0,3],[8,4,9,1],[4,1,3,12],[3,2,1,100]]
filtro = [[1,0,2],[5,0,9],[6,2,1]]
A = np . matrix (matriz1)
B = np . matrix (filtro)
C = np . zeros ((2,2))
x = convultion ( A, B)
print(x)

A = np . matrix (matriz1)
B = np . matrix (filtro)
C = np . zeros ((2,2))
x = convultion ( A, B)
print(x)

