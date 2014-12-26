#all operations in this class might not be reduced to their lowest possible value
#most methods return a new Fraction but _reduce alters values. _reduce is only
#for internal class use.
#Also don't use num and denom except as getters (might make these _ prefixed in
#future.
class Fraction(object):
    #creates a new fraction, denom cannot be 0
    def __init__(self,numerator, denominator=1):
        if (isinstance(numerator,Fraction)): #shortcut for making a copy...allows to take/either int or unknown and then return Frac
            self.num = numerator.num
            self.denom = numerator.denom
        else:
            self.num = numerator
            self.denom = denominator
        self.num = int(self.num)
        self.denom = int(self.denom) #explicitly converting so it will complain if they pass something weird 
    #add two fractions, return a new one
    #Not guaranteed to be lowest
    def __add__(self, other):
        other = Fraction(other)
        commonDenom = self.denom*other.denom
        newNumSelf = self.num*other.denom
        newNumOther = other.num*self.denom
        return Fraction(newNumSelf+newNumOther,commonDenom)
    #subtract two fractions by making 1 negative and then add() ing them
    def __sub__(self,other):
        return self + (Fraction(other)*-1)
    #multiply
    def __mul__(self,other):
        other = Fraction(other)
        return Fraction(self.num*other.num,self.denom*other.denom)
    def __floordiv__(self,other):
        other = Fraction(other)
        return Fraction(self.num*other.denom,other.num*self.denom)
    def __str__(self):
        return str(self.num)+"/"+str(self.denom)
    #uses euler's method to find the gcd of two numbers
    @staticmethod
    def gcd(num1, num2):
        if (num1==0):
            return num2
        if (num2==0):
            return num1
        newNum = num1%num2
        return Fraction.gcd(num2,newNum)
    def copy(self):
        return Fraction(self.num,self.denom)
    def reduce(self):
        eGcd = Fraction.gcd(self.num,self.denom)
        self.num =int(self.num/eGcd)
        self.denom = int(self.denom/eGcd)
    #comparison should have two Fraction arguments -- intended for <(_lt_) etc.
    def __compare(self,other,comparison):
        if (not isinstance(other,Fraction)):
            raise TypeError("Can only compare Fractions or subclasses")
        commonDenom = self.denom*other.denom
        newNumSelf = self.num*other.denom
        newNumOther = other.num*self.denom
        return comparison(newNumSelf,newNumOther)
    #less than
    def __lt__(self,other):
        return self.__compare(other,lambda num1,num2:num1<num2)
    def __le__(self,other):
        return self.__compare(other,lambda num1,num2:num1<=num2)
    def __eq__(self,other):
        return self.__compare(other,lambda num1,num2:num1==num2)
    def __ne__(self,other):
        return self.__compare(other,lambda num1,num2:num1!=num2)
    def __gt__(self,other):
        return self.__compare(other,lambda num1,num2:num1>num2)
    def __ge__(self,other):
        return self.__compare(other,lambda num1,num2:num1>=num2)
    __ZERO = None
    @staticmethod
    def ZERO():
        if (Fraction.__ZERO is None):
            Fraction.__ZERO = Fraction(0)
        return Fraction.__ZERO

#returns the most reduced fraction from all operations
#Add/subtract/mult/div are weird b/c they trying to make immutable.
    #might change that.
class AutoReduceFraction(Fraction):
    def __init__(self,numerator,denominator=1):
        super().__init__(numerator,denominator)
        self.reduce()
    def __add__(self,other):
        answer = super().__add__(other)
        a = AutoReduceFraction(answer.num,answer.denom)
        return a
    def __sub__(self,other):
        answer = super().__sub__(other)
        a = AutoReduceFraction(answer.num,answer.denom)
        return a
    def __mul__(self,other):
        answer = super().__mul__(other)
        a = AutoReduceFraction(answer.num,answer.denom)
        return a
    def __floordiv__(self,other):
        answer = super().__floordiv__(other)
        a = AutoReduceFraction(answer.num,answer.denom)
        return a
    def copy(self):
        return AutoReduceFraction(self.num,self.denom)


print(AutoReduceFraction(3,4)//AutoReduceFraction(1,2))
