'''โปรแกรมเพื่อลดจำนวนของตัวเลขโดยมีคุณลักษณะดังต่อไปนี้

โปรแกรมรับตัวเลขโดยไม่กำหนดจำนวน
โปรแกรมแสดง ความถี่ของตัวตัวเลขที่เหมือนกัน อยู่ตำแหน่งติดกันในรูปแบบ (จำนวน, ตัวเลข)
เขียนโปรแกรมในลักษณะฟังก์ชันโดยแยกส่วนการคำนวณออกจากส่วนรับข้อมูล
ตัวอย่างโปรแกรม
Enter String: 1222311
(1, 1) (3, 2) (1, 3) (2, 1)
ตัวอย่างโปรแกรม
Enter String: 1122336985478569
(2, 1) (2, 2) (2, 3) (1, 6) (1, 9) (1, 8) (1, 5) (1, 4) (1, 7) (1, 8) (1, 5) (1, 6) (1, 9)'''

user_input = input("Enter String: ")
count = 1 ; result = []
for i in range(1, len(user_input)):
    if user_input[i] == user_input[i - 1]:
        count += 1
    else :
        result.append((count, int(user_input[i - 1])))
        count = 1
result.append((count, int(user_input[-1])))
for pair in result:
    print(f'({pair[0]}, {pair[1]})', end=' ')
