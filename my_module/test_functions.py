#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Erica Carrillo
"""

from my_module.functions import *

def testGCD():
    assert gcd(10,5) == 5
    assert gcd(100,10) == 10
    assert gcd(9,15) == 3
    

def testRelativePrimePicker():
    assert relativePrimePicker(35) == 2
    assert relativePrimePicker(10) == 3
    assert relativePrimePicker(18) == 5
    
    
def testInverseModulo():
    assert inverseMod(3,2) == 1
    assert inverseMod(4,5) == 4
    assert inverseMod(6,7) == 6
    
def runTests():
    testGCD()    
    testRelativePrimePicker()
    testInverseModulo()
    
runTests()    
    
    

