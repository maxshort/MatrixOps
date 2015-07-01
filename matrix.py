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
            raise ValueError("Invalid parameters for matrix: " + str(rowList))
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
        return isinstance(otherMatrix,Matrix) and self.getDim()==otherMatrix.getDim()
    def canMultWith(self,otherMatrix):
        return isinstance(otherMatrix,Matrix) and self.getColNum()==otherMatrix.getRowNum()
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
        if not self.canAddWith(otherMatrix): raise ValueError("Cannot add " + str(otherMatrix))
        newVecRows = [x+y for (x,y) in zip(self.rows,otherMatrix.rows)]
        return Matrix(newVecRows)
    def __mul__(self,otherMatrix): #TODO: Threre is a more efficeint way to multiply!
        if not self.canMultWith(otherMatrix): raise ValueError("Cannot mult with " + str(otherMatrix))
        newVecs = []
        for row in self.rows:
            newRow = []
            for cNum in range(0,otherMatrix.getColNum()):
                newRow.append(row.dot(otherMatrix.getCol(cNum)))
            newVecs.append(Vector(newRow))
        return Matrix(newVecs)

    def __eq__(self, otherMatrix):
        if not isinstance(otherMatrix, Matrix): return False
        for pair in zip(self.rows, otherMatrix.rows):
            if not pair[0] == pair[1]: return False
        return True
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
        #assuming that startWithOnes is in REF order
        for i in range(len(startWithOnes) -1, 0, -1):
            subtractor = startWithOnes[i]
            firstNonZeroLoc = subtractor.firstNonZeroLoc()
            if firstNonZeroLoc is not None:
                for j in range(i -1, -1, -1):
                    startWithOnes[j] = startWithOnes[j] - subtractor * startWithOnes[j][firstNonZeroLoc]
        return Matrix(startWithOnes)

    @staticmethod
    def identityMatrix(size):
        if size <= 0:
            raise ValueError("size must be at least 1. Was "+str(size))
        vecs = []
        for pos in range (0, size):
            vecs.append(Vector([0]*pos + [1] + [0]*(size-pos -1)))
        return Matrix(vecs)


#subTestMat = Matrix([one,two])

#print(subTestMat)
#print(subTestMat[0][0])
