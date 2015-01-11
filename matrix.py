import types
import collections
from Fraction import Fraction
from Fraction import AutoReduceFraction
from Vector import Vector
from queue import PriorityQueue

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
    def getCol(self,col): #cache later?
        colContents = []
        for row in self.rows:
            colContents.append(row[col])
        return Vector(colContents)
    def getRow(self,row):
        return self.rows[row]
    def __add__(self,otherMatrix):
        newVecRows = [x+y for (x,y) in zip(self.rows,otherMatrix.rows)]
        return Matrix(newVecRows)
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
    #returns a Reduced Echelon Form of this matrix
    def getREF(self):

        
        #used to make sure that each each vector in priority queue is a unique instance
        #Using a tuple to make priorities in the queue b/c there are too
        #many ways to naturally sort vectors and subclassing seemed like overkill
        #First tiebreaker is the pivot location
        #Next tiebreaker is "qId" which is basically the order it entered the queue
        
        def nextQId():
            nextQId.id = nextQId.id+1
            return nextQId.id
        nextQId.id = 0
        
        #These methods have to do with the PriorityQueue
        #The first converts the vector to a tuple so that the priority queue can sort by the pivot
        #The second converts from this tuple back to vector form
        def qForm(vec):
            if vec.firstNonZeroLoc() is not None:
                return (vec.firstNonZeroLoc(),nextQId(),vec)
            else:
                return vec.getDimension()+1,nextQId(),vec
        def vecForm(tup):
            return tup[2]

        
        
        q = PriorityQueue()
        for row in self.rows:
            q.put_nowait(qForm(row))
        finishedVecs = [] 
        while not q.empty():
            topVec = vecForm(q.get_nowait())
            if q.empty(): #top Vec was the last one 
                finishedVecs.append(topVec)
                break
            #can't use zero vector to subtract stuff out
            #Additionally, this means all remaining vectors are zero vectors
            elif topVec.firstNonZeroLoc() is None: 
                finishedVecs.append(topVec) 
            else:
                nextVec = vecForm(q.get_nowait())
                #While there are vectors w/ same pivot, subtract them 
                while nextVec is not None and nextVec.firstNonZeroLoc() == topVec.firstNonZeroLoc():
                    subNextVec = nextVec - topVec*(nextVec.firstNonZeroVal()//topVec.firstNonZeroVal())
                    q.put_nowait(qForm(subNextVec))
                    nextVec = vecForm(q.get_nowait()) #Have to put in queue to make sure we don't skip any w/ same pivot
                if nextVec is not None: #got out of loop b/c pivot position didn't math. There is probably a cleaner way to do this
                    q.put_nowait(qForm(nextVec))
                finishedVecs.append(topVec)#topVec is now the only one w/ that pivot
        return Matrix(finishedVecs)
    #Returns the reduced row echelon form of the matrix.
    def getRREF(self):
        ref = self.getREF()
        startWithOnes = []
        for row in ref.rows:
            if (row.firstNonZeroVal() is not None):
                startWithOnes.append(row//row.firstNonZeroVal())
            else:
                startWithOnes.append(row)
        #Subtract all further down the line
        #Using indicices so nested will work
        #Starting @ bottom
        #Can't subtract anything by 0
        for subtractByIdx in range(len(startWithOnes) - 1,0,-1):
            if startWithOnes[subtractByIdx].firstNonZeroVal() is None:
                continue
            #subtract all the other ones
            for toClear in range(0,subtractByIdx):
                startWithOnes[toClear] = startWithOnes[toClear] - (startWithOnes[subtractByIdx]*startWithOnes[toClear][subtractByIdx])
        return Matrix(startWithOnes)        
#just testing instantiation

v = Vector([AutoReduceFraction(1),AutoReduceFraction(2),AutoReduceFraction(3)])
#print(v)

#print(Matrix([v,v]).getDim())

#print(Matrix([v,v,v])+Matrix([v,v,v]))
one = Vector([1,2])
two = Vector([2,1])
id1 = Vector([1,0])
id2 = Vector([0,1])

#print(Matrix([one,two])*Matrix([id1,id2]))

#print (Matrix([Vector([1,2]),Vector([1,2])])*Matrix([Vector([1,3]),Vector([1,3])]))

#subTestMat = Matrix([one,two])

#print(subTestMat)
#print(subTestMat[0][0])


print(Matrix([one,two]).getRREF())

print(Matrix([Vector([3,1]),Vector([0,0])]).getRREF())

print(Matrix([Vector([1,2,3])]).getRREF())

print(Matrix([Vector([1,2,3]),Vector([4,5,6]),Vector([7,8,9])]).getRREF())

print(Matrix([Vector([0,0,0])]).getRREF())
