'''เขียนโปรแกรมนับจำนวนคำตามลำดับโดยมีเงื่อนไขดังนี้

โปรแกรมรับจำนวนคำที่ต้องการนับ
รับคำเพื่อนับจำนวนตามลำดับ
โปรแกรมแสดง จำนวนคำที่แตกต่างกัน
โปรแกรมแสดงความถี่ของคำแต่ละคำที่นับได้ตามลำดับ
เขียนโปรแกรมในลักษณะฟังก์ชันโดยแยกส่วนการคำนวณออกจากส่วนรับข้อมูล
ตัวอย่างโปรแกรม
Word = 4
>>> Hello
>>> world
>>> Hello
>>> CoE
Ans =>
3
2 1 1
ตัวอย่างโปรแกรม
Word = 6
>>> hello
>>> world
>>> and
>>> good
>>> bye
>>> world
Ans =>
5
1 2 1 1 1'''

    #### แต่การทำแบบ dictionary จะมีบาง case รันไม่ผ่าน
'''วิธีนี้ไม่ work'''
input_word = int(input("Word = "))
frequency_word = {}
for i in range(input_word):
    enter = input(">>> ").lower()
    frequency_word[enter] = frequency_word.get(enter, 0) + 1
print(f"Ans =>\n{len(frequency_word)}\n{' '.join(map(str,frequency_word.values()))}")
#print(frequency_word)


"-------------------------------------------------------------------------------------------"

input_word2 = int(input("Word = "))
word = []
frequency_word2 = []
for i in range(input_word2):
    next_word = input(">>> ").lower()
    if next_word in word :
        index = word.index(next_word)
        frequency_word2[index] += 1
    else :
        word.append(next_word)
        frequency_word2.append(1)  
print(f"Ans =>\n{len(frequency_word2)}\n{' '.join(map(str,frequency_word2))}")

