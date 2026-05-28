import unittest

from src.compound_interest import CompoundInterest

class CompoundInterestTest(unittest.TestCase):

    # Tests

    # Should return 732.81 given 100 principal, 10 percent, 20 years
    def test_final_amount_when_principal_100_rate_10_term_20(self):
        compound_interest = CompoundInterest(100, 10, 20)
        self.assertEqual(732.81, CompoundInterest.calculate_final_amount(compound_interest))

    # Should return 181.94 given 100 principal, 6 percent, 10 years
    def test_final_amount_when_principal_100_rate_6_term_10(self):
        compound_interest = CompoundInterest(100, 6, 10)
        self.assertEqual(181.94, CompoundInterest.calculate_final_amount(compound_interest))


    # Should return 149,058.55 given 100000 principal, 5 percent, 8 years
    def test_final_amount_when_principal_10000_rate_5_term_8(self):
        compound_interest = CompoundInterest(100000, 5, 8)
        self.assertEqual(149058.55, CompoundInterest.calculate_final_amount(compound_interest))

    def test_final_amount_when_principal_0_rate_10_term_1(self):
        compound_interest = CompoundInterest(0, 10, 1)
        self.assertEqual(0, CompoundInterest.calculate_final_amount(compound_interest))

    # Should return 0.00 given 0 principal, 10 percent, 1 year

    def test_final_amount_when_principal_100_rate_0_term_10(self):
        compound_interest = CompoundInterest(100, 0, 10)
        self.assertEqual(100, CompoundInterest.calculate_final_amount(compound_interest))

    # Extention tests

    # Should return 118,380.16 given 100 principal, 5 percent, 8 years, 1000 per month
    def test_final_amount_when_principal_100_rate_5_term_8_contributions_1000(self):
        compound_interest = CompoundInterest(100, 5, 8)
        self.assertEqual(118380.16, CompoundInterest.calculate_final_amount_with_contributions(compound_interest, 1000))

    # Should return 156,093.99 given 100 principal, 5 percent, 10 years, 1000 per month
    def test_final_amount_when_principal_100_rate_5_term_10_contributions_1000(self):
        compound_interest = CompoundInterest(100, 5, 10)
        self.assertEqual(156093.99, CompoundInterest.calculate_final_amount_with_contributions(compound_interest, 1000))

    # Should return 475,442.59 given 116028.86, 7.5 percent, 8 years, 2006 per month
    def test_final_amount_when_principal_116028_rate_7_term_8_contributions_2006(self):
        compound_interest = CompoundInterest(116028.86, 7.5, 8)
        self.assertEqual(475442.59, CompoundInterest.calculate_final_amount_with_contributions(compound_interest, 2006))

    # Should return 718,335.96 given 116028.86 principal, 9 percent, 12 years, 1456 per month
    def test_final_amount_when_principal_116028_rate_9_term_12_contributions_1456(self):
        compound_interest = CompoundInterest(116028.86, 9, 12)
        self.assertEqual(718335.97, CompoundInterest.calculate_final_amount_with_contributions(compound_interest, 1456))

