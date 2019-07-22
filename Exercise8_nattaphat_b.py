#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#นาย ณัฐภัทร บุญรอด 362515241004 EE36241N
Username=input("Username :")
Password=input("Password :")
if Username=="ntp" and Password=="0918":
    print("Welcome to mennybar Shop.")
    print("-------------------Menu-------------------")
    print("Welcome to mennybar Shop")
    print("1. beer    75  THB")
    print("2. vodka 100 THB")
    print("3. wine   200 THB")
    print("4. soda   20   THB")
    print("5. ice      10  THB")

    B=75
    V=100
    W=200
    S=20
    I=10
    cocktail=int(input("What do you want?(1-5) : "))
    number=int(input("How many do you want? : "))
    if   cocktail==1:
               print("You order ",number," of beer ",B*number," THB")
    elif  cocktail==2:
               print("You order ",number," of vodka ",V*number, " THB")
    elif  cocktail==3:
               print("You order ",number," of wine ",W*number, " THB")
    elif  cocktail==4:
               print("You order ",number," of soda ",S*number, " THB")
    elif  cocktail==5:
               print("You order ",number," of ice ",I*number, " THB")
        
else :
    print("Error ,please try again.")


# In[ ]:




