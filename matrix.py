import types
import collections

#all operations in this class might not be reduced to their lowest possible value
class Fraction(object):
    #creates a new fraction, denom cannot be 0
    def __init__(self,numerator, denominator=1):
        self.num=numerator
        if (denominator == 0):
            raise ValueError("Attempting to place 0 in the denominator")
        self.denom = denominator
    #add two fractions, return a new one
    #Not guaranteed to be lowest
    def add(self, other):
        commonDenom = self.denom*other.denom
        newNumSelf = self.num*other.denom
        newNumOther = other.num*self.denom
        return Fraction(newNumSelf+newNumOther,commonDenom)
    #subtract two fractions by making 1 negative and then add() ing them
    def subtract(self,other):
        return self.add(Fraction(other.num*-1,other.denom))
    #multiply
    def multiply(self,other):
        return Fraction(self.num*other.num,self.denom*other.denom)
    def divideBy(self,other):
        return Fraction(self.num*other.denom,other.num*self.denom)
#returns the most reduced fraction from all operations
class AutoReduceFraction(Fraction):
    def __init__(self,numerator,denominator=1):
        super().__init__(numerator)
        self.reduce()
    def add(self,other):
        answer = super().add(other)
        a = AutoReduceFraction(answer.num,answer.denom)
        a.reduce()
        return a
    #uses euler's method to find the gcd of two numbers
    @staticmethod
    def gcd(num1, num2):
        if (num1==0):
            return num2
        if (num2==0):
            return num1
        newNum = num1%num2
        return AutoReduceFraction.gcd(num2,newNum)
    def reduce(self):
        eGcd = AutoReduceFraction.gcd(self.num,self.denom)
        self.num /=eGcd
        self.denom /=eGcd
        #########################LEFT OFF HERE...
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
            if (not RowOperations.is1dList(row)):
                return False
        return True
        
#Test for accepting 1d matrix
##x = Matrix([1,2,3])
##x.printMatrix()

#Test for accepting 3d matrix
##x = Matrix([[[1,2,3],[1,2,3]],[[1,2,3],[1,2,3]]])
##x.printMatrix()

#Test for creating generic matrix
#x = Matrix([[1,2,3],[1,2,3]])
#x.printMatrix()

#Test for not allowing zero in denom
#x = Fraction(1,0)

#Whole number plus zero
##f1 = Fraction(3)
##f2 = Fraction(0)
##f3 = f1.add(f2)
##print(f3.num)
##print(f3.denom)

#Two Whole numbers
##f1 = Fraction(8)
##f2 = Fraction(10)
##f3 = f2.add(f1)
##print (f3.num)
##print(f3.denom)

#Whole number and fraction
##f1 = Fraction(7)
##f2 = Fraction(3,2)
##f3 = f2.add(f1)
##print(f3.num)
##print(f3.denom)

#Two fractions
##f1 = Fraction(3,2)
##f2 = Fraction(2,3)
##f3 = f2.add(f1)
##print (f3.num)
##print (f3.denom)

#Negative and positive fraction
##f1 = Fraction(-2,3)
##f2 = Fraction(3,8)
##f3 = f1.add(f2)
##print(f3.num)
##print(f3.denom)

#Subtracting whole number
##f1 = Fraction(2)
##f2 = Fraction(1)
##f3 = f1.subtract(f2)
##print(f3.num)
##print (f3.denom)

#Subtracting fractions
##f1 = Fraction(2,3)
##f2 = Fraction(3,8)
##f3 = f1.subtract(f2)
##print(f3.num)
##print (f3.denom)

#Multiplying whole numbers
##f1 = Fraction(3)
##f2 = Fraction(8)
##f3 = f1.multiply(f2)
##print(f3.num)
##print (f3.denom)

#Multiplying Fractions
##f1 = Fraction(3,4)
##f2 = Fraction(7,8)
##f3 = f1.multiply(f2)
##print(f3.num)
##print (f3.denom)

#Dividing Whole Number that divide evenly
##f1 = Fraction(12)
##f2 = Fraction(3)
##f3 = f1.divideBy(f2)
##print (f3.num)
##print(f3.denom)

#Dividing Whole number that do not divide evenly
##f1 = Fraction(15)
##f2 = Fraction(7)
##f3 = f1.divideBy(f2)
##print (f3.num)
##print (f3.denom)

#Testing the autoreduce fraction inheritance
##f1 = AutoReduceFraction(2)
##f2 = AutoReduceFraction(4)
##f3 = f1.add(f2)
##print (f3.num)
##print (f3.denom)

#Test of static method
##print (AutoReduceFraction.gcd(8,4))

#test of whole numbers
##arf1 = AutoReduceFraction(2)
##arf2 = AutoReduceFraction(3,1)
##arf3 = arf1.add(arf2)
##print(arf3.num)
##print(arf3.denom)

arf1 = AutoReduceFraction(3,2)
arf3 = arf1.add(arf1)
print (arf3.num)
print (arf3.denom)

