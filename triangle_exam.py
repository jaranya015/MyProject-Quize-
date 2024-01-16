'''โปแกรมแสดงสามเหลี่ยมตัวเลขโดยรับจำนวนบรรทัดจากผู้ใช้ หากตัวเลขที่ที่ได้เกิน 9 ให้แสดงข้อความ "Out of Range"

ตัวอย่างโปรแกรม
Base: 3
1
22
333
ตัวอย่างโปรแกรม
Base: 5
1
22
333
4444
55555
ตัวอย่างโปรแกรม
Base: 10
Out of Range'''


user_input = int(input("Base: ")) # รับ input จากผู้ใช้งานเป็นตัวเลขจำนวนเต็ม
if user_input >=0 and user_input <= 9: # กำหนดให้ตัวเลขอย่ระหว่าง 0-9 (0,1,2,3,4,5,6,7,8,9)
    for num in range(1, user_input+1): 
        print(str(num) * num)  
else:
    print("Out of Range") # หากนอกเหนือจากเงื่อนไขใน if ข้างต้น โปรแกรมจะแสดงผล Out of Range