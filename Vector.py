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
        
        return Vector(ans)

    def dot(self,other):
        if (not (isinstance(other,Vector) and self.getDimension()==other.getDimension())):
            otherTypeStmt = "Other is type Vector." if (isinstance(other,Vector))  else "Other is not type vector"
            raise Exception(otherTypeStmt+"Expecting 2 vectors of same dim. SelfDim = "+str(self.getDimension())+"otherDim = "+str(other.getDimension))
        mults = [x*y for x,y in zip(self.values,other.values)]
        ans = AutoReduceFraction(0)    
                                                                                                                                
        for m in mults: ans+=m
        return ans

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
print (Vector([1,1]).dot(Vector([1,1])))
