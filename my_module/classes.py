#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Erica Carrillo
"""

import smtplib

#from functions import *
###############################################################################
class Email():
    def __init__(self, sender, receiver, password, msg):
        """ 
        Initialize sender email, receiver email, sender password, and email      
        """  
        self.msg = msg
        self.sender = sender
        self.receiver = receiver
        self.password = password
        
        
    
    def sendEmail(self):
        """ 
        Send email using the technique mentioned in this article : https://realpython.com/python-send-email/
        Code was copied directly since I don't understand it
        
        Parameters:
               None
        Returns: 
               None       
        """    
          
        try:
            server = smtplib.SMTP("smtp.gmail.com",587)
            server.starttls()
            server.login(self.sender, self.password)
            server.sendmail(self.sender, self.receiver, self.msg)
            print('Sent!')
        except Exception as e:
            print(e)
        finally:
            server.quit()           
            
            
###############################################################################      