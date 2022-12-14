# -*- coding: utf-8 -*-
"""Muneeb_PIAIC175939.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DD8TbY5h5N9RVTq2CiRjdw_RIONkvw4X
"""

def electricity(units):
    if units >= 1 and units <= 100:
        charges = units * 9.43
    
    elif units > 100 and units <= 200:
        charges = units * 10.29
    
    elif units > 200 and units <= 300:
        charges = units * 12.55
    
    elif units > 300 and units <= 400:
        charges = units * 17.38
    
    elif units > 400 and units <= 500:
        charges = units * 18.84
    
    elif units > 500 and units <= 600:
        charges = units * 19.76
    
    elif units > 600 and units <= 700:
        charges = units * 20.40

    elif units > 700:
        charges = units * 23.87
    
    else:
        charges = -1
    
    return charges

def uniform(units):
    if units >= 1 and units <= 100:
        charges = units * 3.95
    
    elif units > 100 and units <= 200:
        charges = units * 7.67
        
    else:
        print("No Uniform Changes applied")
        charges = 0
        
    return charges

def fuel(monthly_units):
    charges = units * 6.88
    
    return charges

def sales_tax(units):
    charges = 865.43
    return charges

def tv_fees():
    charges = 335.71
    return charges

def advance_tax():
    charges = 940.66
    return charges

def bill_main(monthly_units):
    electric_charges = electricity(monthly_units)
    print("Your electric charges for", monthly_units, "units =", electric_charges)
    
    uniform_charges = uniform(monthly_units)
    print("Uniform charges for", monthly_units, "units =", uniform_charges)
    
    fuel_charges = fuel(monthly_units)
    print("Fuel adjustment charges for", monthly_units, "units =", fuel_charges)
    
    sale_tax = sales_tax(monthly_units)
    print("Sale tax for", monthly_units, "units =", sale_tax)
    
    advanceTax = advance_tax()
    print("Advance and Government TAX = ", advanceTax)
    
    tv_fee = tv_fees()
    print("TV license fees for", monthly_units, "=", tv_fee)
    
    total = electric_charges + uniform_charges + fuel_charges + sale_tax + advanceTax + tv_fee
    print("------------------------------------------------------------------------")
    print("Your total Electricity bill for", monthly_units, "units =", total)

units = int(input("Please enter your units here: "))
print("********************************************************************")

bill_main(units)

