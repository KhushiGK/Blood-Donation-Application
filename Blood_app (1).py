# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 23:05:36 2021

@author: Dhanisht
"""
# class blood_app:
    
def admin():
    global address_bb
    global address_bc
    global bg_A
    global bg_B
    global bg_AB
    global bg_O
    global request
    global contact_detail
    
    choice=int(input("enter your choice:"))
    bg_A=int(input("entre the quqntity of bg_A:"))# enter how much amount of blood A available in blood bank
    bg_B=int(input("entre the quqntity of bg_B:"))
    bg_AB=int(input("entre the quqntity of bg_AB:"))
    bg_O=int(input("entre the quqntity of bg_O:"))
    contact_detail=input("enter the contact detail of admin")
    if (choice==1):
        blood_bank=input("entre the name of nearest blood bank:")
        address_bb=input("enter the area and address of blood bank:")
        print(blood_bank)
        print(address_bb)
    elif (choice==2):
        blood_bank=input("entre the nearest blood camp:")
        address_bc=input("enter the area and address of blood camp:")
        print(blood_bank)
        print(address_bc)
        # admin(blood_bank, blood_camp, area)
        
    if (bg_A < 2):# minimaum amout of blood available in blood A bank
        request=1
    elif (bg_B < 2):
        request=2
    elif (bg_AB < 2):
        request=3
    elif (bg_O < 2):
        request=4
admin()
def recepient():
    name=input("entre the name of recepient:")
    address=input("entre the address of recepient:")
    age=input("entre the age of recepient:")
    gender=input("entre the gender of recepient:")
    blood_need=input("entre the grp of blood which is need:")
    print(name, address, age, gender, blood_need,)
    option=int(input("entre the option of  blood place:"))
     
    if (option==1):
        print("address is",address_bb)
    elif (option==2):
        print("address is",address_bc)
    print("cntct admin at this cntct detail",contact_detail)
recepient()  
def donar():
    name=input("entre the name of donar:")
    address=input("entre the address of donar:")
    age=input("entre the age of donar:")
    gender=input("entre the gender of donar:")
    blood_grp=input("entre the blood grp of donar:")
    print(name, address, age, gender, blood_grp,)
    # return request
    if (request==1 and blood_grp==bg_A):#admin send request to donar to donate the blood grp A(bg_A)
        print("sm bld grp,cntct admin to this cnt det. if want to donate",contact_detail)
    elif (request==2 and blood_grp==bg_B):
        print("sm bld grp,cntct admin to this cnt det. if want to donate",contact_detail)
    elif (request==3 and blood_grp==bg_AB):
        print("sm bld grp,cntct admin to this cnt det. if want to donate",contact_detail)
    elif (request==4 and blood_grp==bg_O):
        print("sm bld grp,cntct admin to this cnt det. if want to donate",contact_detail)
donar()
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    