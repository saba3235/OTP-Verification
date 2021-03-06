# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 12:02:00 2020

@author: Sabarish J
"""
from __future__ import print_function
import kivy
import random
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
import time
import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 





class MyGrid1(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid1, self).__init__(**kwargs)
        self.otp=1
        self.cols = 1

        self.inside = GridLayout()
        self.inside.cols = 2

        self.inside.add_widget(Label(text="Email id: "))
        self.email = TextInput(multiline=False)
        self.inside.add_widget(self.email)


        self.inside.add_widget(Label(text="Received OTP :  "))
        self.passs = TextInput(multiline=False)
        self.inside.add_widget(self.passs)
        
      

        self.add_widget(self.inside)

        self.submit = Button(text="Send OTP", font_size=40)
        self.submit.bind(on_press=self.pressed1)
        self.inside.add_widget(self.submit)
        
        
        self.submit1 = Button(text="Verify OTP", font_size=40)
        self.submit1.bind(on_press=self.pressed2)
        self.inside.add_widget(self.submit1)
    def pressed2(self,instance):
        otp1=self.passs.text
        if(str(self.otp)==otp1):
            self.passs.text="Verification sucessfull"
        else:
            self.passs.text="Verification unsucessfull"

    def pressed1(self, instance):
        
               
        
        email = self.email.text
        self.otp=random.randint(10000,100000)
        fromaddr = "dontreplyotp@gmail.com" 
        msg = MIMEMultipart() 
        s = smtplib.SMTP('smtp.gmail.com', 587) 
        s.starttls() 
        s.login(fromaddr, "qwerty123@")
        msg = MIMEMultipart() 
        msg['From'] = fromaddr 
        msg['To'] = email
        msg['Subject'] = "OTP Verification mail"
        body = "OTP for Verificatio : "+str(self.otp)
        msg.attach(MIMEText(body, 'plain'))         
        text = msg.as_string() 
        s.sendmail(fromaddr, email, text) 

    msg=None
        
  
            
            
            
           
class OTP(App):
    def build(self):
        return MyGrid1()


if __name__ == "__main__":
    OTP().run()
