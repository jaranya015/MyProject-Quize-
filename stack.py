'''โปรแกรมสแต็กหรรษาโดยจะสุ่มตัวดำเนินการของสแต็ก 3 ตัวดำเนินการ และ close สำหรับจบการทำงานของโปรแกรม โดยทั้ง 4 ตัวเลือกมีความหมายดังนี้

push -> ใส่ตัวเลขที่ผู้ใช้ป้อนเข้า stack
pop -> เอาตัวเลขออกจาก stack
head -> แสดงค่าตัวสุดท้ายของ stack
exit -> จบการทำงานของโปรแกรม
โดยภูมิได้กำหนดการทำงานของโปรแกรทดังนี้

ผู้ใช้สามารถป้อนเลขใดก็ได้ที่เป็นจำนวนเต็ม (number)
เมื่อได้ตัวเลขจากผู้ใช้ (number) แล้วจะตรวจสอบว่าเป็นเลขคู่หรือเลขคี่แล้วกำหนดค่าให้เป็น (xnumber)
ถ้าเป็นเลขคู่ จะนำตัวเลขที่ผู้ใข้ป้อน มา xor กับ นำตัวเลขที่ผู้ใข้ป้อนชิฟบิตตัวเลข ไป 2 บิต
ถ้าเป็นเลขคี่ จะนำตัวเลขที่ผู้ใข้ป้อน มา xor กับ นำตัวเลขที่ผู้ใข้ป้อนชิฟบิตตัวเลข ไป 3 บิต
นำตัวเลขจากการ xor (xnumber) มา Mod ด้วย 13 แล้วนำตัวเลขที่ได้จากการ mod มาหาตัวดำเนินการจากตารางการสุ่มตัวดำเนินการดังตารางด้านล่าง
เมื่อได้ตัวดำเนินการแล้วให้ดำเนินการตามตัวดำเนินการนั้นกำหนด
ถ้าหากไม่ได้ตัวดำเนินการ close ให้วนรอบรับค่าจากตัวเลขใหม่
ถ้า number เป็นตัวเลขคู่

0 -> push
1 -> pop
2 -> pop
3 -> head
4 -> push
5 -> close
6 -> head
7 -> push
8 -> pop
9 -> push
10 -> pop
11 -> close
12 -> head
ถ้า number เป็นตัวเลขคี่

0 -> push
1 -> close
2 -> pop
3 -> head
4 -> pop
5 -> pop
6 -> push
7 -> push
8 -> pop
9 -> push
10 -> push
11 -> head
12 -> close
โปรแกรมจะมีตัวอย่างดังต่อไปนี้

Enter number: 1
Push: 1
Stack: [1]
Enter number: 2
Pop: 1
Stack: []
Enter number: 3
Close
Stack: []
End of program, Bye!
1 2 3 คือข้อมูลที่ผู้ใช้ป้อนให้ระบบ

Enter number: 1
Push: 1
Stack: [1]
Enter number: 2
Pop: 1
Stack: []
Enter number: 4
Push: 4
Stack: [4]
Enter number: 5
Push: 5
Stack: [4, 5]
Enter number: 6
Head: 5
Stack: [4, 5]
Enter number: 7
Head: 5
Stack: [4, 5]
Enter number: 8
Pop: 5
Stack: [4]
Enter number: 9
Push: 9
Stack: [4, 9]
Enter number: 0
Push: 0
Stack: [4, 9, 0]
Enter number: 3
Close
Stack: [4, 9, 0]
End of program, Bye!
1 2 4 5 6 7 8 9 0 3 คือตัวเลขที่ป้อนให้ระบบ'''






def generate_operator(number):
    if number % 2 == 0:
        xnumber = number ^ ((number >> 2) & 0x3)
        return {
            0: "push",
            1: "pop",
            2: "pop",
            3: "head",
            4: "push",
            5: "close",
            6: "head",
            7: "push",
            8: "pop",
            9: "push",
            10: "pop",
            11: "close",
            12: "head",
        }[xnumber % 13]
    else:
        xnumber = number ^ ((number >> 3) & 0x7)
        return {
            0: "push",
            1: "push",
            2: "pop",
            3: "close",
            4: "push",
            5: "push",
            6: "head",
            7: "push",
            8: "pop",
            9: "push",
            10: "pop",
            11: "close",
            12: "push",
        }[xnumber % 13]

def main():
    stack = []

    while True:
        number = int(input("Enter number: "))

        if number % 2 == 0:
            xnumber = number ^ ((number >> 2) & 0x3)
        else:
            xnumber = number ^ ((number >> 3) & 0x7)

        operator = generate_operator(xnumber)

        if operator == "push":
            stack.append(number)
            print(f"Push: {number}")
        elif operator == "pop":
            if len(stack) > 0:
                popped = stack.pop()
                print(f"Pop: {popped}")
        elif operator == "head":
                if len(stack) > 0:
                    print(f"Head: {stack[-1]}")
        elif operator == "close":
            print("Close")
            break

        print(f"Stack: {stack}")

    print("End of program, Bye!")

if __name__ == "__main__":
    main()
    

# def generate_operator(number):
#     xor_shift = (number >> 2) & 0x3 if number % 2 == 0 else (number >> 3) & 0x7
#     return {0: "push", 1: "pop", 2: "pop", 3: "head", 4: "push", 5: "close", 6: "head",
#             7: "push", 8: "pop", 9: "push", 10: "pop", 11: "close", 12: "head"}[xor_shift % 13]

# def main():
#     stack = []

#     while True:
#         number = int(input("Enter number: "))
#         xor_shift = ((number >> 2) & 0x3) if number % 2 == 0 else ((number >> 3) & 0x7)
#         operator = generate_operator(number ^ xor_shift)

#         if operator == "push":
#             stack.append(number)
#             print(f"Push: {number}")
#         elif operator == "pop" and stack:
#             popped = stack.pop()
#             print(f"Pop: {popped}")
#         elif operator == "head" and stack:
#             print(f"Head: {stack[-1]}")
#         elif operator == "close":
#             print("Close")
#             break

#         print(f"Stack: {stack}")

#     print("End of program, Bye!")

# if __name__ == "__main__":
#     main()
