'''เขียนโปรแกรมเข้ารหัสหรือถอดรหัส ROT-13

สามารถเลือกได้ว่าจะเข้ารหัส หรือ ถอดรหัส
รับข้อความจากผู้ใช้เป็นภาษาอังกฤษ ตัวพิมพ์ใหญ่ พิมพ์เล็ก หรือตัวเลขก็ได้
การเข้ารหัสจะขยับตัวอักษรทุกๆ ตัวจากข้อความไปข้างหน้า 13 ตำแหน่งเฉพาะตัวอักษร หากเลยตัว Z หรือ z ให้วนกลับไป A หรือ a
Hello, World! 1234 → Uryyb, Jbeyq! 1234
Python 101 → Clguba 101
การถอดรหัสจะขยับตัวอักษรทุกๆ ตัวจากข้อความถอยหลัง 13 ตำแหน่งเฉพาะตัวอักษร หากเลยตัว A หรือ a ให้วนกลับไป Z หรือ z
Uryyb, Jbeyq! 1234 Hello, → World! 1234
Clguba 101 → Python 101
แสดงผลออกทางหน้าจอ
Select 2 options
 - 1 encrypt with ROT 13
 - 2 decrypt with ROT 13

Choose option: 1
Enter text: Hello, World! 1234
Ciphertext is "Uryyb, Jbeyq! 1234"
1 และ Hello, World! 1234 คือข้อมูลที่ใส่ให้โปรแกม

Select 2 options
 - 1 encrypt with ROT 13
 - 2 decrypt with ROT 13

Choose option: 2
Enter text: Uryyb, Jbeyq! 1234
Plaintext is "Hello, World! 1234"
2 และ Uryyb, Jbeyq! 1234 คือข้อมูลที่ใส่ให้โปรแกม

Select 2 options
 - 1 encrypt with ROT 13
 - 2 decrypt with ROT 13

Choose option: 1
Enter text: Shift cipher Caesar's code
Ciphertext is "Fuvsg pvcure Pnrfne'f pbqr"
1 และ Shift cipher Caesar's code คือข้อมูลที่ใส่ให้โปรแกม

Select 2 options
 - 1 encrypt with ROT 13
 - 2 decrypt with ROT 13

Choose option: 2
Enter text: Fuvsg pvcure Pnrfne'f pbqr
Plaintext is "Shift cipher Caesar's code"'''


def encrypt(word):
    result = ""
    for char in word :
        if char.isalpha():
            if char.islower():
                result += chr((ord(char) - ord('a') + 13)%26 + ord('a'))
            elif char.isupper():
                result += chr((ord(char) - ord('A') + 13)%26 + ord('A'))
        else :
            result += char
    return result
def decrypt(word):
    result = ""
    for char in word :
        if char.isalpha():
            if char.islower():
                result += chr((ord(char) - ord('a') - 13)%26 + ord('a'))
            elif char.isupper():
                result += chr((ord(char) -ord('A') - 13)%26 + ord('A'))
        else :
            result += char
    return result
def main():
    print(f"Select 2 options\n - 1 encrypt with ROT 13\n - 2 decrypt with ROT 13\n")
    input_choice = input("Choose option: ")
    input_text = input("Enter text: ")
    if input_choice == '1' :
        print(f'Ciphertext is "{encrypt(input_text)}"')
    elif input_choice == '2' :
        print(f'Plaintext is "{decrypt(input_text)}"')
        
if __name__ == "__main__":
    main()
               
