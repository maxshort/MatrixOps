
#Test for not allowing zero in denom
#x = Fraction(1,0)

#Whole number plus zero
##f1 = Fraction(3)
##f2 = Fraction(0)
##print (f1+f2) # expecting 3/1
##
###Two Whole numbers
##f1 = Fraction(8)
##f2 = Fraction(10)
##print(f1+f2) # expecting 18/1
##
###Whole number and fraction
##f1 = Fraction(7)
##f2 = Fraction(3,2)
##print(f1+f2) #expecting 17/2
##
###Two fractions
##f1 = Fraction(3,2)
##f2 = Fraction(2,3)
##print (f1+f2) #expecting 13/6
##
###Negative and positive fraction
##f1 = Fraction(-2,3)
##f2 = Fraction(3,8)
##print(f1+f2) #expecting -7/24
##
###Subtracting whole number
##f1 = Fraction(2)
##f2 = Fraction(1)
##print (f1-f2) #expecting 1/1
##
###Subtracting fractions
##f1 = Fraction(2,3)
##f2 = Fraction(3,8)
##print(f1-f2) #expecting 7/24
##
###Multiplying whole numbers
##f1 = Fraction(3)
##f2 = Fraction(8)
##print (f1*f2) #expecting 24/1
##
###Multiplying Fractions
##f1 = Fraction(3,4)
##f2 = Fraction(7,8)
##print (f1*f2) #21/32
##
###Dividing Whole Number that divide evenly
##f1 = Fraction(12)
##f2 = Fraction(3)
##print(f1/f2)
##
###Dividing Whole number that do not divide evenly
##f1 = Fraction(15)
##f2 = Fraction(7)
##f3 = f1.divideBy(f2)
##print (f3.num)
##print (f3.denom)
##
###Testing the autoreduce fraction inheritance
##f1 = AutoReduceFraction(2)
##f2 = AutoReduceFraction(4)
##f3 = f1.add(f2)
##print (f3.num)
##print (f3.denom)
##
###Test of static method
##print (Fraction.gcd(4,8))
##
###test of whole numbers
##arf1 = AutoReduceFraction(2)
##arf2 = AutoReduceFraction(3,1)
##arf3 = arf1.add(arf2)
##print(arf3.num)
##print(arf3.denom)
##
##arf1 = AutoReduceFraction(3,2)
##arf3 = arf1.add(arf1)
##print (arf3)
##
###testing the subtraction of whole numbers
##arf1 = AutoReduceFraction(4)
##arf2 = AutoReduceFraction(2)
##print (arf1.subtract(arf2))
##
###subtraction of fraction
##arf1 = AutoReduceFraction(18,27)
##arf2 = AutoReduceFraction(9,27)
##print(arf1.subtract(arf2))
##
###other subtraction
##arf1 = AutoReduceFraction(7,2)
##arf2 = AutoReduceFraction(1,2)
##print(arf1.subtract(arf2))
##
###multiplication of whole numbers
##arf1 = AutoReduceFraction(5)
##arf2 = AutoReduceFraction(3)
##print (arf1.multiply(arf2))
##
###multiplication of a whole number and fraction
##arf1 = AutoReduceFraction(8)
##arf2 = AutoReduceFraction(1,2)
##print(arf1.multiply(arf2))
##
###divding divisible numbers
##arf1 = AutoReduceFraction(8)
##arf2 = AutoReduceFraction(4)
##print (arf1.divideBy(arf2))
###dividing non-divisible whole numbers
##arf1 = AutoReduceFraction(18)
##arf2 = AutoReduceFraction(4)
##print(arf1.divideBy(arf2))
##
###dividing fractions that result in fraction
##arf1 = AutoReduceFraction(9,2)
##arf2 = AutoReduceFraction(7,3)
##print(arf1.divideBy(arf2))

#testing signs

##arf1 = AutoReduceFraction(3,2)
##arf2 = AutoReduceFraction(7,8)
##print(arf1<arf2)
##print(arf2<arf1)
##print(arf1<=arf2)
##print(arf2<=arf1)
##print(arf1>arf2)
##print (arf2>=arf1)
##print(arf1==arf2)
##print(arf1!=arf2)

#Testing equality with equal fractions
##arf1 = AutoReduceFraction(18,4)
##arf2 = AutoReduceFraction(9,2)
##print(arf1==arf2)
##print(arf1!=arf2)

#arf1 = AutoReduceFraction(8,4)
#arf2 = AutoReduceFraction(4,2)
#print (arf1==arf2)

arf1 = AutoReduceFraction(1)
arf2 = AutoReduceFraction(2)
arf3 = AutoReduceFraction(3)
arf4 = AutoReduceFraction(4)
