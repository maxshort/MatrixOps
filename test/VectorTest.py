import unittest
import sys
sys.path.append("..")
from Vector import Vector
from Fraction import AutoReduceFraction

class VectorTest(unittest.TestCase):
    
    def test_onlySingleListAllowed(self):
        try:
            v = Vector(3,4,5)
            self.fail("allowed non-list")
        except(ValueError):
            pass
        try:
            v = Vector()
            self.fail("allowed empty vector")
        except:
            pass
    def test_givesCorrectDimension(self):
        v=Vector([1,2])
        self.assertEqual(2, v.getDimension())
        v1=Vector([2,4,7])
        self.assertEqual(3,v1.getDimension())

    def test_vectorsAddCorrectly(self):
        v1 = Vector([2, 1])
        v2 = Vector([3, 4])
        self.assertEqual(Vector([5, 5]), v1 + v2)

    def test_multScalarsCorrectly(self):
        v = Vector([2, 1])
        self.assertEqual(Vector([1, AutoReduceFraction(1,2)]), v*AutoReduceFraction(1, 2))
        self.assertEqual(Vector([8,4]), v*4)

    def test_vectorsSubtractCorrectly(self):
        v1 = Vector([5, 4])
        v2 = Vector([1, 1])
        self.assertEqual(Vector([4,3]), v1 - v2)

    def test_dotProductWorks(self):
        v1 = Vector([1, 1])
        self.assertEqual(AutoReduceFraction(2), v1.dot(v1))

    def test_firstNonZeroWithNoZeroCorrect(self):
        v1 = Vector([1, 2, 3])
        self.assertEqual(0, v1.firstNonZeroLoc())
        self.assertEqual(AutoReduceFraction(1), v1.firstNonZeroVal())

    def test_firstNonZeroWithZero(self):
        v1 = Vector([0, 0, 1, 2])
        self.assertEqual(2, v1.firstNonZeroLoc())
        self.assertEqual(AutoReduceFraction(1), v1.firstNonZeroVal())

    def test_equalsWorks(self):
        self.assertTrue(Vector([1,1]) == Vector([1, 1]))
        self.assertFalse(Vector([1, 0, 0]) == Vector([1, 0]))
        self.assertFalse(Vector([1,0]) == Vector([0,1]))

    def test_notEqualsWorks(self):
        self.assertFalse(Vector([1,1]) != Vector([1, 1]))
        self.assertTrue(Vector([1, 0, 0]) != Vector([1, 0]))
        self.assertTrue(Vector([1,0]) != Vector([0,1]))

    def test_scalarDivWorks(self):
        v = Vector([2, 2, 2])
        self.assertEqual(Vector([AutoReduceFraction(1, 2), AutoReduceFraction(1, 2), AutoReduceFraction(1, 2)]), v//4)
    
    
