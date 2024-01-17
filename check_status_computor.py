'''โปรแกรมเพื่อตรวจสอบสถานะของคอมพิวเตอร์โดยที่ผู้ใช้จะป้อนตัวเลขจำนวนเต็มค่าหนึ่ง โปรแกรมจะนำค่านั้นมาหารไม่เอาเศษด้วย 10 แล้ว นำมา mod ด้วย 3

หากผลลัพธ์ที่ได้ เป็น 0 ให้แสดงคำว่า Complete
หากผลลัพธ์ที่ได้ เป็น 1 ให้แสดงคำว่า Waiting
หากผลลัพธ์ที่ได้ เป็น 2 ให้แสดงคำว่า Error
Enter computer status code: 60
Complete
60 คือค่าที่ผู้ใช้ป้อนให้โปรแกรม
Complete คือคำตอบของโปรแกรม
Enter computer status code: 35
Complete
35 คือค่าที่ผู้ใช้ป้อนให้โปรแกรม
Complete คือคำตอบของโปรแกรม
Enter computer status code: 20
Error'''



enter_your_number = int(input("Enter computer status code: "))
new_your_number = enter_your_number // 10
new_your_numbe2 = new_your_number % 3
if new_your_numbe2 == 0 :
    print("Complete")
elif new_your_number == 1 :
    print("Waiting")
elif new_your_numbe2 == 2 :
    print("Error")
    
'''-------------------------------------------------------------------------'''


def check_computer_status():
    enter_your_number = int(input("Enter computer status code: "))
    new_your_number = enter_your_number // 10
    new_your_numbe2 = new_your_number % 3

    if new_your_numbe2 == 0:
        print("Complete")
    elif new_your_numbe2 == 1:
        print("Waiting")
    elif new_your_numbe2 == 2:
        print("Error")
    else:
        print("Invalid input")

if __name__ == "__main__":
    check_computer_status()

    
status = int(input("Enter computer status code: "))
if (status//10)%3==0:
    print("Complete")
else :
        if (status//10)%3==1:
            print("Waiting")
        else:
            if (status//10)%3==2:
                print("Error")
