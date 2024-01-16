'''โปรแกรมรับข้อความที่มีความยาวไม่จำกัด และจำนวนข้อความย่อยที่ต้องการแบ่ง

ตัวอย่างของโปรแกรม
Text: 1234567890
Width: 3
123
456
789
0
ข้อความ 1234567890 เป็นข้อความที่ป้อนให้กับโปรแกรม
3 ความยาวของข้อความย่อย
ตัวอย่าง Output
123
456
789
0
ตัวอย่างของโปรแกรม
Text: Prince of Songkla University
Width: 4
Prin
ce o
f So
ngkl
a Un
iver
sity'''




user_input = input("Text: ") # รับ input text จากผู้ใช้งาน
user_input2 = int(input('Width: ')) # รับ input width จากผู้ใช้งาน

for i in range(0, len(user_input), user_input2): # ใช้วนซ้ำตั้งแต่ตำแหน่งเริ่มต้น 0 
                                                # จนถึงตำแหน่งสิ้นสุด len(user_input) และเพิ่มค่า user_input2 ในแต่ละรอบ

    substring = user_input[i:i + user_input2] # ตัวแปร substring แทนด้วย user_input ตำแหน่งที่ i ที่ได้มาจากการ for loop
                                              # และหยุดตำแหน่งที่ i + user_input2 (เป็นตัวเลข int)
    
    print(substring) # แสดงผลที่ได้จาก substring ผ่านหน้าจอ
                     # โดยจะทำงานทุกครั้งที่มีการวนลูปของ for i
                     # จะหยุดการทำงานกต่อเมื่อลูปหยุดการทำงาน