from Fraction import Fraction
from Fraction import AutoReduceFraction

#IDEA:
# represent internally as tuple
# mostly provide ways of multiplying/adding and then making new immutables
# Matrices would _not_ be made up of these...mostly would just use them to perform row ops

#TODO:
    #Initialize from int/fraction args
    #Initialize from int/fraction tuple args
    #Initialize from int/fraction list args

    #support adding/subtracting like vectors _DONE
    #support multiplying by scalar numbers/fractions -DONE
    #
    #support dot product - DONE

class Vector:
    def __init__(self,*args):
        """To keep this simple, right now _only_ taking a list of ints and/or fractions"""
        #initializing from a list of mixed ints and/or fractions
        if (len(args)!=1 or type(args[0])!=list):
            raise Exception("Expecting single list argument for vector")
        cleanList = [AutoReduceFraction(x) for x in args[0]]
        self.values = tuple(cleanList)

    def getDimension(self):
        return len(self.values)
    def __len__(self):
        return len(self.values)
    def __eq__(self,other):
        return self.values == other.values
    def __ne__(self,other):
        return self.values != other.values

    def isSameDimension(self,other):
        return other.getDimension()==self.getDimension()
    #might need to make this output more readable stuff
    def __str__(self):
        ret = "<"
        prefix = ""
        for val in self.values:
            ret+=prefix+str(val)
            prefix = ","
        return ret+">"

    def __add__(self,other):
        """Expecting other to be another vector of the same dimension"""
        if (not self.isSameDimension(other)):
            raise Exception("Can't add two vectors of different dimensions")
        sumList = [a+b for a,b in zip(self.values,other.values)]
        return Vector(sumList)
    def __sub__(self,other):
        return self+(other*-1)

    def __mul__(self,other):
        """For scalar multiplication only. Dot product has its own thing to avoid confusion"""
        if (not (isinstance(other,int) or isinstance(other,float) or isinstance(other, Fraction))):
            raise Exception("Expecting only an int, float or Fraction")
        ans = [x*other for x in self.values]
        print("INTERPRETING OTHER AS " + str(other))
        return Vector(ans)

    def __floordiv__(self,other):
        """Divide by a scalar"""
        return self.__mul__(AutoReduceFraction(1)//AutoReduceFraction(other))

    def dot(self,other):
        if (not (isinstance(other,Vector) and self.getDimension()==other.getDimension())):
            otherTypeStmt = "Other is type Vector." if (isinstance(other,Vector))  else "Other is not type vector"
            raise Exception(otherTypeStmt+"Expecting 2 vectors of same dim. SelfDim = "+str(self.getDimension())+"otherDim = "+str(other.getDimension))
        mults = [x*y for x,y in zip(self.values,other.values)]
        ans = AutoReduceFraction(0)    
                                                                                                                                
        for m in mults: ans+=m
        return ans
    def __getitem__(self,key):
        #index error will be naturally raised by tuple anyway
        return self.values[key]
    #IF THERE IS NO NON-ZERO IT WILL RETURN None
    def firstNonZeroLoc(self):
        try: #This try catch is basically a way of caching the val so its only calced once
            return self.__firstNonZeroLoc
        except AttributeError:            
            for i in range(0,self.getDimension()):
                if (not (self.values[i] == Fraction.ZERO())):
                    self.__firstNonZeroLoc = i
                    return i
            self.__firstNonZeroLoc = None
            return None
    #IF THERE IS NO NON-ZERO IT WILL RETURN None
    def firstNonZeroVal(self):
        if (self.firstNonZeroLoc() is None):
            return None
        return self.values[self.firstNonZeroLoc()]
    
#Just a basic test
##v = Vector([1,2,3])
##print (v.getDimension())
##print(v)

#Adding test
##v = Vector([2,1])
##v1 = Vector([3,4])
##v2 = v+v1
##print(v2)

#Some mult tests
##v = Vector([2,1])
##v2 = v*AutoReduceFraction(1,2)
##print (v2)
                                                                                                                                   
##v3 = v*4
##print(v3)

#Subtract test
#print (Vector([5,4])-Vector([1,1]))

#Dot product test
#print (Vector([1,1]))
#print (Vector([1,1]).dot(Vector([1,1])))

#print (Vector([1,2,3])[1])

print(Vector([1,2,3]).firstNonZeroLoc())

print(Vector([1,2,3]).firstNonZeroVal())

print(Vector([0,0,1,2]).firstNonZeroLoc())

print(Vector([0,0,0]).firstNonZeroLoc())

#print(Vector([1,1])==Vector([1,1]))

#print(Vector([1,0])!=Vector([0,1]))

#print(Vector([1,0,0])==Vector([1,0]))

print("ANS" + str(Vector([2,2,2])//4))
