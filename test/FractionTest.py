import unittest
import sys
sys.path.append("..")
from Fraction import Fraction
from Fraction import AutoReduceFraction

class FractionTest(unittest.TestCase):
    def test_zeroNotAllowedInDenom(self):
        with self.assertRaises(ValueError):
            x = Fraction(1, 0)
    
    def test_wholeNumPlusZeroShouldBeWholeNum(self):
        three = Fraction(3)
        zero = Fraction(0)
        self.assertEqual(three+zero, Fraction(3))

    def test_twoWholeNumsShouldBeCorrectSum(self):
        eight = Fraction(8)
        ten = Fraction(10)
        self.assertEqual(eight+10, Fraction(18))

    def test_wholeNumPlusFractionShouldBeCorrectSum(self):
        seven = Fraction(7)
        threeHalves = Fraction(3,2)
        self.assertEqual(seven+threeHalves, Fraction(17,2))

    def test_twoFractionsAddedTogetherShouldGiveCorrectAnswer(self):
        threeHalves = Fraction(3,2)
        twoThirds = Fraction(2,3)
        self.assertEqual(threeHalves + twoThirds, Fraction(13, 6))

    def test_negativeAndPositiveFractionShouldGiveCorrectAnswer(self):
        negTwoThirds = Fraction(-2, 3)
        threeEights = Fraction(3,8)
        self.assertEqual(negTwoThirds + threeEights, Fraction(-7, 24))

    def test_subtractingWholeNumbersShouldWork(self):
        one = Fraction(1)
        two = Fraction(2)
        self.assertEqual(two-one, Fraction(1))

    def test_subtractingTwoFractionsShouldWork(self):
        twoThirds = Fraction(2,3)
        threeEights = Fraction(3,8)
        self.assertEqual(twoThirds - threeEights, Fraction(7,24))

    def test_multiplyingTwoWholeNumbersShouldWork(self):
        three = Fraction(3)
        eight = Fraction(8)
        self.assertEqual(three*eight, Fraction(24))

    def test_multiplyingFractionsShouldWork(self):
        threeFourths = Fraction(3,4)
        sevenEights = Fraction(7,8)
        self.assertEqual(threeFourths*sevenEights, Fraction(21, 32))

    def test_divisionWithNoRemainderWholeNumbersShouldWork(self):
        twelve = Fraction(12)
        three = Fraction(3)
        self.assertEqual(twelve//three, Fraction(4))

    def test_divWithRemainderShouldResultInFraction(self):
        fifteen = Fraction(15)
        seven = Fraction(7)
        self.assertEqual(fifteen//seven, Fraction(15,7))

    def test_gcdMethodWorks(self):
        self.assertEqual(Fraction.gcd(4,8), 4)

    def test_autoReduceReducesAfterAdd(self):
        threeHalves = AutoReduceFraction(3, 2)
        three = threeHalves + threeHalves
        self.assertEqual(three.num, 3)
        self.assertEqual(three.denom, 1)

    def test_autoReduceReducesAfterSubtract(self):
        sevenHalves = AutoReduceFraction(7, 2)
        threeHalves = AutoReduceFraction(3, 2)
        two = sevenHalves - threeHalves
        self.assertEqual(two.num, 2)
        self.assertEqual(two.denom, 1)

    def test_autoReduceReducesAfterMult(self):
        eight = AutoReduceFraction(8)
        oneHalf = AutoReduceFraction(1, 2)
        answer = eight * oneHalf
        self.assertEqual(answer.num, 4)
        self.assertEqual(answer.denom, 1)

    def test_autoReduceReducesAfterDiv(self):
        eight = AutoReduceFraction(8)
        four = AutoReduceFraction(4)
        answer = eight//4
        self.assertEqual(answer.num, 2)
        self.assertEqual(answer.denom, 1)

    def test_autoReducesReducesAfterRemainderDiv(self):
        eighteen = AutoReduceFraction(18)
        four = AutoReduceFraction(4)
        answer = eighteen//4
        self.assertEqual(answer.num, 9)
        self.assertEqual(answer.denom, 2)

    def test_autoReduceReducesAfterDividingFractions(self):
        nineHalves = AutoReduceFraction(9, 2)
        sevenThirds = AutoReduceFraction(7, 3)
        answer = nineHalves//sevenThirds
        self.assertEqual(answer.num, 27)
        self.assertEqual(answer.denom, 14)

    def test_comparisionOperatorsShouldWorkInAutoReduce(self):
        threeHalves = AutoReduceFraction(3, 2)
        sevenEights = AutoReduceFraction(7, 8)
        self.assertFalse(threeHalves<sevenEights)
        self.assertTrue(threeHalves > sevenEights)
        self.assertFalse(threeHalves <= sevenEights)
        self.assertTrue(threeHalves >= sevenEights)
        self.assertFalse(threeHalves == sevenEights)
        self.assertTrue(threeHalves != sevenEights)
        
    def test_initiallyNonReducedAutoReducedFractionsEqual(self):
        eighteenFourths = AutoReduceFraction(18,4)
        nineHalves = AutoReduceFraction(9,2)
        self.assertTrue(eighteenFourths == nineHalves)
        self.assertFalse(eighteenFourths != nineHalves)
