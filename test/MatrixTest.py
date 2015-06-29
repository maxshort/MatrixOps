import unittest
import sys
sys.path.append("..")
from Fraction import AutoReduceFraction
from Vector import Vector
from matrix import Matrix

class MatrixTest(unittest.TestCase):

    def test_noJaggedMatricesAllowed(self):
        two = Vector([1,2])
        three = Vector([1, 2, 3])
        #Test to make sure the couldFormMatrix checks correctlty
        self.assertFalse(Matrix.couldFormMatrix([two, three]))
        #Test to make sure that constructor is testing this
        try:
            Matrix([two, three])
            self.fail("expected to fail when passing jagged matrix")
        except(ValueError):
            pass #test passes, exception was thrown for invalid matrix


    def test_equalWorks(self):
        v1 = Vector([1, 2, 3])
        v2 = Vector([4, 5, 6])
        self.assertTrue(Matrix([v1, v2]) == Matrix([v1, v2]))
        self.assertFalse(Matrix([v2, v1]) == Matrix([v1, v2]))
    
    def test_JudgesSquaresCorrectly(self):
        one = Vector([1])
        two = Vector([1,2])
        self.assertTrue(Matrix([one]).isSquare())
        self.assertFalse(Matrix([one,one]).isSquare())
        self.assertTrue(Matrix([two, two]).isSquare())

    def test_dimensionsShouldBeCorrect(self):
        one = Vector([1])
        two = Vector([1,2])
        self.assertEqual((3,2), Matrix([two]*3).getDim())
        self.assertEqual((5,1), Matrix([one]*5).getDim())

    def test_canAddWithOnlyWorksForSameDim(self):
        one = Vector([1])
        two = Vector([1,2])
        self.assertFalse(Matrix([one]).canAddWith(Matrix([two])))
        self.assertTrue(Matrix([one]*2).canAddWith(Matrix([one]*2)))

    def test_canMultWorks(self):
        one = Vector([1])
        two = Vector([1,2])
        self.assertTrue(Matrix([two]).canMultWith(Matrix([one, one])))
        self.assertTrue(Matrix([one, one, one]).canMultWith(Matrix([two])))
        self.assertFalse(Matrix([two,two]).canMultWith(Matrix([one])))

    def test_addChecksBounds(self):
        one = Vector([1])
        two = Vector([1,2])
        try:
            Matrix([one])+Matrix([two])
            fail("Should have thrown ValueError for adding of 2 matrices of different dimensions")
        except(ValueError):
            pass #caught unequal dim adding

    def test_mulChecksBounds(self):
        one = Vector([1])
        two = Vector([1,2])
        try:
            Matrix([two, two])*(Matrix([one]))
            fail("Should have thrown value error for multiplication where first matrix had different column number than second matrix's row number")
        except(ValueError):
            pass #caught unequal

    def test_matrixMultWorks(self):
        m1_v1= Vector([1, 2, 3])
        m1_v2 = Vector([4, 5, 6])
        m2_v1 = Vector([3])
        m2_v2 = Vector([2])
        m2_v3 = Vector([4])
        self.assertEqual(Matrix([Vector([19]), Vector([46])]),Matrix([m1_v1, m1_v2])*Matrix([m2_v1, m2_v2, m2_v3]))

        m3_v = Vector([1, 2])
        m4_v = Vector([1, 3])
        m5_v = Vector([3, 9])
        self.assertEqual(Matrix([m5_v, m5_v]), Matrix([m3_v, m3_v])*Matrix([m4_v,m4_v]))
        
    def test_REFWorks(self):
        one0 = Vector([1, 0])
        zero1 = Vector([0, 1])
        identity2 = Matrix([one0, zero1])
        self.assertEqual(identity2, identity2.getREF())
        
        four_3_7_5 = Vector([4, 3, 7, 5])
        four_3_7_9 = Vector([4, 3, 7, 9])
        four_3_7_0 = Vector([4, 3, 7, 5])

        zero_0_0_4 = Vector([0, 0, 0, 4])
        zero_0_0_0 = Vector([0, 0, 0, 0])

        m = Matrix([four_3_7_5, four_3_7_9, four_3_7_0])
        mREF = Matrix([four_3_7_5, zero_0_0_4,zero_0_0_0])
        print (m.getREF())
        self.assertEqual(mREF, m.getREF())

##    def test_RREFWorks(self):
##        one0 = Vector([1, 0])
##        zero1 = Vector([0, 1])
##        identity2 = Matrix([one0, zero1])
##        self.assertEqual(identity2, identity2.getRREF())
##
##        four_3_7_5 = Vector([4, 3, 7, 5])
##        four_3_7_9 = Vector([4, 3, 7, 9])
##        four_3_7_0 = Vector([4, 3, 7, 5])
##
##        m = Matrix([four_3_7_5, four_3_7_9, four_3_7_0])
##
##        mRREF_v1 = Vector([1, AutoReduceFraction(3, 4), AutoReduceFraction(7,4), AutoReduceFraction(5,4)])
##        mRREF_v2 = Vector([0, 0, 0, AutoReduceFraction(9, 4)])
##        mRREF_v3 = Vector([0, 0, 0, 0])
##
##        mRREF = Matrix([mRREF_v1, mRREF_v2, mRREF_v3])
##        print(m.getRREF())
##        self.assertEqual(mRREF, m.getRREF())
