//เขียนโปรแกรมแสดงสามเหลื่ยมตัวเลขโดยที่

โปรแกรมรับจำนวนบรรทัดของ 3 เหลี่ยมโดยมีค่าอยู่ระหว่า 0 < line < 10
หากจำนวนบรรทัดไม่อยู่ในช่วงที่กำหนด ให้แสดงข้อความ Out of Range
แสดงสามเหลี่ยมของตัวเลขตามที่กำหนด
เขียนโปรแกรมในลักษณะฟังก์ชันโดยแยกส่วนการคำนวณออกจากส่วนรับข้อมูล
ตัวอย่างโปรแกรม
Line: 2
1
121
ตัวอย่างโปรแกรม
Line: 5
1
121
12321
1234321
123454321//


def input_num_by_user():
    user_input = int(input("Line: "))
    return user_input
def triangle(num):
    for i in range(1,num+1):
        for j in range(1, i+1):
                print(j,end="")
        for j in range(i-1, 0 , -1):
            print(j,end="")
        print()
def main():
    num = input_num_by_user()
    triangle(num)

if __name__=="__main__":
    main()
    
    
