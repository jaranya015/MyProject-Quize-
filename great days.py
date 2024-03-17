//เนื่องจากมีนักศึกษาสายมูคนนึงต้องการหาวันไปเที่ยวทะเล โดยมีวิธีหาวันมงคลดังต่อไปนี้

หากวันนี้เป็นวันที่ 12 ให้นำตัวเลขมากับด้าน แล้วนำไปลบกับวันที่ 12 - 21 = - 9
นำผลที่ได้มา หารด้วยเลขมงคล หาก หารแล้วไม่เหลือเศษจะถือว่าเป็นวันมงคล
เขียนโปรแกรมเพื่อช่วยเพื่อนนักศึกษาสายมูหาวันมงคลที่จะไปเที่ยวทะเล

โปรแกรมจะรับวันเริ่มต้นและวันสิ้นสุดที่จะคำนวณ
โปรแกรมจะรับเลขมงคลจากนักศึกษาสายมู
โปรแกรมจะแสดงจำนวนวันที่เป็นวันมงคล
เขียนโปรแกรมในลักษณะฟังก์ชันโดยแยกส่วนการคำนวณออกจากส่วนรับข้อมูล
ตัวอย่างโปรแกรม
Date: 11 15
Great Number: 3
Great Days : 5 
ตัวอย่างโปรแกรม
Date: 20 23
Great Number: 6
Great Days: 2//

def input_by_user():
    user = input("Date: ")
    return user
def calculation(user,gate):
    user1 = [int(i) for i in user.split()]
    count = 0
    for i in range(user1[0],user1[1]+1) :
        change = int(str(i)[::-1])
        if (i - change) % gate == 0 :
            count += 1
    return count
def main():
    user = input_by_user()
    gate = int(input("Great Number: "))
    cal = calculation(user,gate)
    print("Great Days : ",cal)
if __name__ == "__main__":
    main()
