import types
import collections
from Fraction import Fraction
from Fraction import AutoReduceFraction
from Vector import Vector


#This assumes a 2d matrix
#should change to a tuple??
class Matrix:
    def __init__(self, rowList):
        if (not Matrix.couldFormMatrix(rowList)):
            raise Exception("Invalid parameters for matrix: "+rowList)
        self.rows = rowList
        
    def isSquare(self):
        return len(self.rows)==len(self.rows[0]) #only testing 1st row b/c all rows have to have same len

    #look @ replibr?
    def __str__(self):
        ret = "START of matrix\n"
        for row in self.rows:
            ret += str(row)+"\n"
        return ret + "END OF MATRIX"
    @staticmethod 
    def couldFormMatrix(vectorList):
        """If not a list of Vectors that are all the same dimension, it will return false""" 
        return all(x.getDimension() == vectorList[0].getDimension() for x in vectorList) # Right now, only check is if they have the same dimensino
    def canAddWith(self,otherMatrix):
        return isinstance(otherMatrix,Matrix) and self.getDim()==other.getDim()
    def canMultWith(self,otherMatrix):
        return isinstance(otherMatrix,Matrix) and self.getColNum()==other.getRowNum()
    def getRowNum(self):
        return len(self.rows)
    def getColNum(self):
        return self.rows[0].getDimension()
    def getDim(self):
        return (self.getRowNum(),self.getColNum())
    def getCol(self,col):
        columns = []
        for row in self.rows:
            columns.append(row[col])
        return Vector(columns)
    def getRow(self,row):
        return self.rows[row]
    def __add__(self,otherMatrix):
        newVecRows = [x+y for (x,y) in zip(self.rows,otherMatrix.rows)]
        return Matrix(newVecRows)
        #USE THE ZIP??? LOOK @ Vector??
    def __mul__(self,otherMatrix):
        newVecs = []
        for row in self.rows:
            newRow = []
            for cNum in range(0,otherMatrix.getColNum()):
                newRow.append(row.dot(otherMatrix.getCol(cNum)))
            newVecs.append(Vector(newRow))
        return Matrix(newVecs)
    def __getitem__(self,key):
        return self.getRow(key)
        
#just testing instantiation

v = Vector([AutoReduceFraction(1),AutoReduceFraction(2),AutoReduceFraction(3)])
print(v)

#print(Matrix([v,v]).getDim())

#print(Matrix([v,v,v])+Matrix([v,v,v]))
one = Vector([1,2])
two = Vector([2,1])
id1 = Vector([1,0])
id2 = Vector([0,1])

print(Matrix([one,two])*Matrix([id1,id2]))

print (Matrix([Vector([1,2]),Vector([1,2])])*Matrix([Vector([1,3]),Vector([1,3])]))

subTestMat = Matrix([one,two])

print(subTestMat)
print(subTestMat[0][0])
