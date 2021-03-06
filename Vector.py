from Fraction import Fraction
from Fraction import AutoReduceFraction

#IDEA:
# represent internally as tuple

#TODO:
    #Initialize from int/fraction args
    #Initialize from int/fraction tuple args

class Vector:
    def __init__(self,*args):
        """To keep this simple, right now _only_ taking a list of ints and/or fractions"""
        #initializing from a list of mixed ints and/or fractions
        if (len(args)!=1 or type(args[0])!=list):
            raise ValueError("Expecting single list argument for vector")
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

    @staticmethod
    def areLinearlyIndependent(vecs):
        for v in vecs[1:]:
            if v.getDimension() != vecs[0].getDimension():
                raise ValueError("Vectors must the the same dimension")
        ratios = set()
        for v in vecs:
            ratios.add(tuple(z//v[0] for z in v[1:]))
        print(ratios)
        return len(ratios) == len(vecs)
        
    
