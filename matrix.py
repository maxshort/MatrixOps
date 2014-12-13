import types
import collections
from Fraction import Fraction
from Fraction import AutoReduceFraction

        #LEFT OFF HERE...
class RowOperations:
    def multiplyBy(rowList,value):
        ret = []
        for col in rowList:
            ret.append(col*value)
    def is1dList(row):
        if not type(row) is list: 
                return False
        for col in row:
            if type(col) is list:
                return False
        return True

#This assumes a 2d matrix
#should change to a tuple??
class Matrix:
    def __init__(self, matrixList):
        if not (Matrix.isMatrix2d(matrixList)):
            raise ValueError("The matrix is not 2d");
        self.matrix = matrixList
    def printMatrix(self):
        print (self.matrix)
    def getRREF(self): 
        for row in self.matrix:
            originalOneVal = row[0]
            for col in row:
                print ("HI!")       
        print ("NOT IMPLEMENTED")
    def isMatrix2d(matrixList):
        if not type(matrixList) is list:
                return False
        for row in matrixList:
            if (not RowOperations.is1dList(row) and not row is int and not row is Fraction):
                return False
        return True
        
#Test for accepting 1d matrix
##x = Matrix([1,2,3])
##x.printMatrix()
##
###Test for accepting 3d matrix
##x = Matrix([[[1,2,3],[1,2,3]],[[1,2,3],[1,2,3]]])
##x.printMatrix()

#Test for creating generic matrix
#x = Matrix([[1,2,3],[1,2,3]])
#x.printMatrix()

#mat = Matrix([arf1,arf2,arf3,arf4])

arf = AutoReduceFraction(3,4)

weirdFrac = Fraction(Fraction(3,4))
print ("HERE:!")
print (weirdFrac)

#print (3*arf)
#print (arf*3)

For vectors:

            vec = (1,2,3)
            Can do vec * 3
            vec + vec (CHECK BOUNNDS)
            vec 
