enter = input("Enter value in mm, cm, and m: ")
enter2 = input("Enter unit to covert in mm, cm, m: ")
number_value = ''.join(i for i in enter if i.isdigit())
number_value = int(number_value)
if "cm" in enter:
    num_in__m = number_value*10**-2
else :
    if "mm" in enter :
        num_in__m = number_value*10**-3
    else:
        if "m" in enter :
            num_in__m = number_value
if enter2 in enter :
    print(f"Value after unit conversion is {num_in__m}{enter2}")
else:
    if "cm" in enter2:
       print(f"Value after unit conversion is {num_in__m*10**-2}{enter2}") 
    else :
        if "mm" in enter2:
            print(f"Value after unit conversion is {num_in__m*10**-3}{enter2}")
#print(num_in__m)



