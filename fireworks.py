'''บาสกับนายนัดกันไปดูพลุที่จุดในวันขึ้นปีใหม่ แต่บาสอยากรู้ว่ามีพลุสีอะไรบ้างจะถูกจุดในวันสิ้นปี บาสต้องการเขียนโปรแกรมเพื่อช่วยกันนับพลุกับนาย แต่ยังคิดไม่ออกว่าจะบันทึกข้อมูลอย่างไรให้ง่ายและสามารถทำได้อย่างต่อเนื่องและรวดเร็ว นายจึงเสนอวิธีบันทึกข้อมูลเป็นโค้ดสีแล้วตามด้วยตัวเลข โดยที่ถ้าพลุมี 2 สี ไม่ว่าจะบันทึกสีใดขึ้นก่อนก็จะถือเป็นสีเดียวกัน ดังนี้

R12 => สีแดง 12 ลูก
YR5 => สีแดง-เหลือง 5 ลูก
RY10 => สีแดง-เหลือง 10 ลูก
โดยนายกำหนดสีพลุดังต่อไปนี้

R -> สีแดง
G -> สีเขียว
B -> สีฟ้า
W -> สีขาว
Y -> สีเหลือง
P -> สีชมพู
C -> สีฟ้า
O -> สีส้ม
M -> ม่วง
U -> แยกสีไม่ได้
เพื่อให้ง่ายต่อการสรุปผล บาสได้กำหนดวิธีแสดงผลตาลำดับตัวอักษรในพจนานุกรมโดยมีตัวอย่างดังนี้

Fireworks Counter
Enter color code: R10
R     ->         10
Enter color code: G10  
G     ->         10
Enter color code: B10
B     ->         10
Enter color code: END

Fireworks Statistic
B     ->         10
G     ->         10
R     ->         10
R10 G10 B10 END เป็นค่าที่ผู้ใช้ป้อน'''





print("Fireworks Counter")
def frireworke():
    dict_frirework = {}
    while True :
        input_frire_worke = input("Enter color code: ").lower()
        color = ''.join(char for char in input_frire_worke if char.isalpha())
        count = ''.join(char for char in input_frire_worke if char.isdigit())
        if input_frire_worke == "END" or input_frire_worke == "end" :
            break
        
        if color and count:  
            count = int(count) 
            dict_frirework[color] = dict_frirework.get(color, 0) + (count)
    
        print(f"{color}\t->\t{count}")
                
    print("Fireworks Statistic") 
    for key, value in dict_frirework.items():
        print(f"{key}\t->\t{value}")
        
frireworke()
    
                
