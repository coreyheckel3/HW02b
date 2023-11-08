# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from triangle import classify_triangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classify_triangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testMutantA(self):
        self.assertEqual(classify_triangle(8,5,3), 'NotATriangle', 'Not a triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classify_triangle(5,3,4),'Right','5,3,4 is a Right triangle')

    def testEquilateralTriangleA(self):
        self.assertEqual(classify_triangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

    def testEquilateralTriangleB(self):
        self.assertEqual(classify_triangle(3,3,3), 'Equilateral', '3,3,3 should be equilateral')

    def testScaleneTriangleA(self):
        self.assertEqual(classify_triangle(2,3,4), 'Scalene', '2,3,4 should be scalene')

    def testScaleneTriangleB(self):
        self.assertEqual(classify_triangle(5,12,9), 'Scalene', '5,12,9 should be scalene')

    def testIsocelesTriangleA(self):
        self.assertEqual(classify_triangle(5,5,7), 'Isoceles', '5,5,7 should be isoceles')

    def testIsocelesTriangleB(self):
        self.assertEqual(classify_triangle(2,3,2), 'Isoceles', '2,3,2 should be isoceles')

    def testInvalidInputA(self):
        self.assertEqual(classify_triangle(200,200,200), 'Equilateral', '200,200,200 should be Equilateral')

    def testInvalidInputB(self):
       self.assertEqual(classify_triangle(0,0,0), 'NotATriangle', '0,0,0 should be invalid')

    def testInvalidInputC(self):
        self.assertEqual(classify_triangle(1,2,1.2), 'InvalidInput', '1,2,1.2 should be invalid')

    def testNotTriangle(self):
        self.assertEqual(classify_triangle(1,2,3), 'NotATriangle', '1,2,3 should not be a triangle')

    def testRightTriangleC(self):
        self.assertEqual(classify_triangle(3, 4, 5), 'Right', '3,4,5 is a Right triangle')

    def testMutantB(self):
        self.assertEqual(classify_triangle(1, 1, 2), 'NotATriangle', '1,1,2 is not a triangle')
    def testMutantC(self):
        self.assertEqual(classify_triangle(2,4,2), 'NotATriangle', 'not a triangle')



if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

