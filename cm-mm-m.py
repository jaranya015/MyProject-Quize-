'''เขียนโปรแกรมเพื่อแปลงหน่วยระหว่าง cm <=> mm <=> m โดยมีข้อกำหนดดังต่อไปนี้

รับข้อความจากผู้ใช้
จะต้องเป็นตัวเลขและ ตัวอักษร cm mm m เท่านั้น เช่น 10cm 100mm 1m 1.0cm
รับข้อความตัวเลือกว่าผู้ใช้ต้องการแปลงหน่วยเป็นอะไร จาก cm mm m
แสดงผลจากการแปลงหน่วยตามที่ผู้ใช้ต้องการ
10m → 1000cm
1cm → 10mm
1cm → 0.01m
Enter value in mm, cm, and m: 100cm
Enter unit to convert in mm, cm, m: m
Value after unit conversion is 1.0m
100cm และ m คือค่าที่ใส่ให้โปรแกรม

Enter value in mm, cm, and m: 1m
Enter unit to convert in mm, cm, m: mm
Value after unit conversion is 1000.0mm
1m และ mm คือค่าที่ใส่ให้โปรแกรม

Enter value in mm, cm, and m: -3.5cm
Enter unit to convert in mm, cm, m: mm
Value after unit conversion is -35.0mm
-3.5cm และ mm คือค่าที่ใส่ให้โปรแกรม'''


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



