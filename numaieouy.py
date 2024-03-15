//เขียนโปรแกรมเพื่อหาคะแนนจากข้อความ โดยที่

โปรแกรมจะรับข้อมูลเป็นตัวอักษรพิมพ์ใหญ่หรือเล็กก็ได้
พิจารณาอักษร a, e, i, o, u และ y ที่มีเสียงเป็นสระในแต่ละคำ
หากผลรวมของตัวอักษรเสียงสระ เป็นเลขคู่ จะคะแนนเป็น 2
หากผลรวมของตัวอักษรเสียงสระ เป็นเลขคี่ จะคะแนนเป็น 1
แสดงผลรวมของคะแนนในแต่ละคำ
เขียนโปรแกรมในลักษณะฟังก์ชันโดยแยกส่วนการคำนวณออกจากส่วนรับข้อมูล
ตัวอย่างโปรแกรม
Enter Text: PSU
Ans => 1
ตัวอย่างโปรแกรม
Enter Text: Department of Computer Engineering, Prince of Songkla University
Ans => 10
ตัวอย่างโปรแกรม
Enter Text: Hello world
Ans => 3//


def input_by_user():
    user_input = input("Enter Text: ")
    return user_input
def suma_e_i_o_u(user_input):
    vowels = "aeiouy"
    count = 0 ; sum = 0
    for char in user_input :
        for vowel in vowels :
            if char == vowel :
                count += 1
                if count % 2 == 0 :
                    sum += 0
                else :
                    sum += 1
            if char == " ":
                break
    return sum 
def main():
    userinput = input_by_user()
    result = suma_e_i_o_u(userinput)
    print("Total sum:", result)
if __name__ == "__main__":
    main()
                
