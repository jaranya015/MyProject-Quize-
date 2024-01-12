'''เขียนโปรแกรมนับตัวอักษรจากข้อความที่ผู้ใช้ป้อนให้จนกว่าจะได้รับข้อความว่า 'end'

รับข้อมูลจากผู้ใช้จนกว่าจะป้อนเฉพาะคำว่า end
แปลงข้อความที่ผู้ใช้ป้อนให้เป็นตัวพิมพ์เล็กแล้วนับตัวอักษร
นับเฉพาะตัวอักษรไม่นับเครื่องหมายอื่น
แสดงข้อมูลเฉพาะตัวอักษรที่ที่ปรากฎในข้อความที่ผู้ใช้ป้อนโดยเรียงตามตัวอักษร
ตัวอย่างการใช้งาน

Enter string: Hello, World!
Enter string: Hello -> Python \o/                              
Enter string: end
******************************
*     Alphabet Counting      *
******************************
d 1
e 2
h 3
l 5
n 1
o 5
p 1
r 1
t 1
w 1
y 1
******************************
Enter string: Even though I know I am so in love with you
Enter string: I’m not really sure that you feel the same way too
Enter string: Ready for that moment, when my hearts broken again
Enter string: Yeahh! Yeahh! Yeahh!
Enter string: end
******************************
*     Alphabet Counting      *
******************************
a 13
b 1
d 1
e 17
f 2
g 2
h 14
i 6
k 2
l 4
m 6
n 8
o 12
r 6
s 4
t 11
u 4
v 2
w 4
y 9
******************************'''

letter_count = {}
while True:
    enter = input("Enter string: ")
    if enter == "end" :
        break
    for char in enter :
        if char.isalpha():
            char_lower = char.lower()
            letter_count[char_lower] = letter_count.get(char_lower,0) + 1
            
print("******************************")
print("*     Alphabet Counting      *")
print("******************************")
for char, count in sorted(letter_count.items()):
    print(f"{char} {count}")
print("******************************")
    
        
