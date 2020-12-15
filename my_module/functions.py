#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Erica Carrillo
"""
import random as rand
from my_module.classes import Email
        
################################## Globals ####################################
alpha = 'aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ .,?!'
###############################################################################

def twoDigPrimeGenerator():
    """ 
    Generates all prime numbers between 10-100. 
    
    Parameters:
           None
    Returns: 
           primes: A list containes all prime numbers between 10-100.  
    """
    # list all numbers from 2 to 100
    nums = [i for i in range(2,100)]
    primes = []
    
    # Iterate over the nums list and append any number that is not divisible by 2,3,5,7
    # primes should contain all primes between 10-100 at the end of the loop
    for number in nums:
        if  (number != 2 and number % 2 != 0) and (number != 3 and number % 3 != 0) and (number != 5 and number % 5 != 0) and (number != 7 and number % 7 != 0):
            primes.append(number)
    return primes

###############################################################################
    
def randomPrimePicker():
    """ 
    Randomly picks two prime numbers between 10-100 
    
    Parameters:
           None
    Returns: 
           firstPrime (int): the first prime number
           secondPrime (int): the second prime number
    """
    # Generate a list of primes between 2-100
    primes = twoDigPrimeGenerator()
    
    # pick the first prime randomly
    firstPrime = rand.choice(primes)
    
    # pick the second prime randomly
    secPrime = rand.choice(primes)
    return firstPrime,secPrime

###############################################################################
    
def relativePrimePicker(a):
    """ 
    Finds the smallest number 'e' 'that doesn't share any common factor with a
    such a number is called relatively prime to a
    
    Parameters:
           a (int): the first number
    Returns: 
           e (int): the smallest number that is relatively prime to a       
    """
    # Iterate over all the numbers between 2 and a
    # gcd(a,b) = 1 means a and b don't share any common factors
    # Check if a number has no common factor with a
    # Once you find it, save it and exit the loop
    # return that number
    
    for i in range(2, a):
        if gcd(i, a) == 1:
            e = i
            break
    return e    

###############################################################################
    
def inverseMod(e, a):
    """ 
    Finds an inverse of e modulo (a)  
    
    Parameters:
           a (int): the number
           e (int): a number relatively prime to a
    Returns: 
           d (int): an inverse of e modulo (a)        
    """
    # Iterate over all the numbers between 1 and a
    # Check if a number has a remainder of 1 when multipled by e then divided by a
    # Once you find it, save it and exit the loop
    # return that number
    
    d = 'error'
    for i in range(1, a):
        if (i*e)%(a) == 1:
            d = i
            break
    return d    

###############################################################################
    
def gcd(x, y):
    """ 
    Finds the greatest common factor (gcd) of two integers x, y  
    
    Parameters:
           x (int): the first integer
           y (int): the second integer
    Returns: 
           gcd (int): the greatest common factor (gcd) of two integers x, y       
    """
    # Check which number is the smaller and save it in a variable 'min'
    if x > y: 
        min = y 
    else: 
        min = x
        
    # Iterate over all the numbers between 1 and the smaller number
    # Check if a number divides both numbers. If so, save it in 'gcd'
    # return gcd
        
    for i in range(1, min+1): 
        if((x % i == 0) and (y % i == 0)): 
            gcd = i 
              
    return gcd 

###############################################################################
    
def AlphaToNums():
    """ 
    Builds a dictionary that associate every letter to a unique number : a->0, A->1, b->2, etc  
    
    Parameters:
           None
    Returns: 
           alphaDic (dictionary): a dictionary that associate every letter to a unique number       
    """
    
    alphaDic = {}
    
    # Fill in the dictionary alphaDic such that each letter gets associated with a unique number
    # a->0, A->1, b->2, B->3, ...
    # Return the dictionary
    
    for i in range(len(alpha)):
        alphaDic[alpha[i]] = i
        
    return alphaDic    

###############################################################################
    
def NumsToAlpha(index):
    """ 
    Returns the letter associated with a given index in the alphabetic string   
    
    Parameters:
           index (int): the index of the letter in the alphabetic string 
    Returns: 
           (str): the letter associated with the index in the alphabetic string       
    """
    
    # Return the letter associated with index
    return alpha[index]

###############################################################################
        
def encrypt(text):
    """ 
    Encrypts a text using RSA algorithm 
    
    Parameters:
           text (string): the original text to be encrypted  
    Returns: 
           encryptedMsg (str): the encryption of the message
           pin (str): the pin code needed to decrypt the message later
    """
    
    # The implementation of RSA encryption scheme
    # Pick two random prime numbers then multiply them
    p, q = randomPrimePicker()
    n = p*q
    # Find a number that is shares no common factors with (p-1)*(q-1)
    e = relativePrimePicker((p - 1)*(q - 1))
    
    # Loads the dictionary that maps alphabet to numbers
    dic = AlphaToNums()
    numerEncoding = []
    encryptedMsg = ''
    
    # Iterate over every letter in the original message
    # Fetch the number associated with that letter
    # Raise that number to the exponent 'e' then calculate the remainder when divided by n
    # Store the remiander in variable 'C'
    # Append C to the list numerEncoding
    for char in text:
        M = dic[char]
        C = (M**e)%n
        numerEncoding.append(C)
    
    # Make sure every letter encoding has length 4 by padding it with 0s on the left
    fixedLenEncoding = fourDigitEncoding(numerEncoding)  
    
    # Iterate over the encoding of those letters and concatenate them in a single string
    # That string is the final encoding of the original message
    for num in fixedLenEncoding:
        encryptedMsg += num
    
    # Concatenate p with q with to be your PIN code    
    pin = str(p)+str(q)+str(e)
    
    # Return the encrypted msg and the pin code needed to decrypt it
    return encryptedMsg, pin      

###############################################################################
    
def fourDigitEncoding(encryptionList):
    """ 
    Padds the encryption of each letter with extra 0s to make all encryption have same length 
    
    Parameters:
           encryptionList (list[int]): list of the encoding of each letter in the original message  
    Returns: 
           fixedLenList (list[str]): list of the encoding of each letter after padding them with extra 0s
    """
    
    fixedLenList = []
    
    # Iterate over every letter encoding and check if its length is less than 4
    # If so, padd it with as many zeros as need to reach length 4
    # Then append it to the list fixedLenList
    # Return the list
    
    for num in encryptionList:
        lenDiff = 4 - len(str(num))
        fixedLenList.append('0'*lenDiff+str(num))
        
    return fixedLenList    

###############################################################################
    
def chopMsg(encryption, fixedLen = 4):
    """ 
    Splits the encrypted message into chucks of 4 digits each.  
    
    Parameters:
           encryption (str): the encryption of the original message  
    Returns: 
           choppedText (list[int]): list of the padded encoding of each letter
    """
    
    choppedText = []
    
    # Slice the encrypted msg into strings of length 4
    # Convert each string to its numerical value
    # Append each numerical value to the list choppedText
    
    for i in range(0, len(encryption), fixedLen):
        choppedText.append(int(encryption[i:i+fixedLen]))
        
    return choppedText    

###############################################################################
    
def decrypt(encryptedMsg):
    """ 
    Decrypts the encrypted message 
    
    Parameters:
           encryptedMsg (str): the encryption of the original message  
    Returns: 
           msg (str): the original message after decryption
    """
    ## The implementation of RSA decryption scheme
    # Read PIN from user then slice it to p, q and e
    pin = input('Please enter your PIN: ')
    p, q , e = int(pin[0:2]), int(pin[2:4]), int(pin[4:]) 
    
    # Calculate the inverse modulo needed for decryption
    d = inverseMod(e, (p-1)*(q-1))
    decryption = []
    msg = ''
    
    # Fetch the list of letters encoding after they are padded
    numerEncoding = chopMsg(encryptedMsg)
    
    # Iterate over each encoding and perfom the decryption opertion 
    for C in numerEncoding:
        decryption.append((C**d)%(p*q))
    
    # Iterate over each number and convert it back to its alphabetic value
    for num in decryption:
        msg += NumsToAlpha(num)
       
    # Return the decrypted message    
    return msg

###############################################################################
    
def run():
    print('Menu :')
    print('Enter 1 to encrypt a message')
    print('Enter 2 to decrypt a message')
    print('Enter 3 to send an encrypted Email')
    try:
        choice = int(input())
    except Exception as e:
        print('Wrong choice. Re-run program')
        return
    
    if choice == 1:
        msg = input('Enter your message : ')
        encryptedMsg, pin = encrypt(msg)
        print('Encrypted Message : '+encryptedMsg)
        print('Your pin code is : '+pin)
        
    elif choice == 2:
        encryptedMsg = input('Enter your encrypted message')
        decryptedMsg = decrypt(encryptedMsg)
        print('The original Message : '+decryptedMsg)
        
    elif choice == 3:
        sender = input('Enter your gmail address: ')
        password = input('Enter your gmail password : ')
        receiver = input('Enter receiver email : ')
        msg = input('Type email : ')
        encryptedMsg, pin = encrypt(msg)
        print('Your PIN = '+pin)
        e = Email(sender,receiver, password, encryptedMsg)
        e.sendEmail()
        
    else:
        print('Invalid choice. Try again!')
        
        