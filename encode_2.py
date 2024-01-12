'''โปรแกรมเพื่อขยับตัวอักษรไปยังตัวอักษรลำดับถัดไปถัดไป

รับข้อความจากผู้ใช้เป็นภาษาอังกฤษ ตัวพิมพ์ใหญ่ หรือพิมพ์เล็กก็ได้ 3 ตัวอักษร
ถ้าใส่มาไม่เท่ากับ 3 ตัวอักษรให้แสดงข้อความ word length is mismatched แล้วจบการทำงาน
ขยับตัวอักษรจากข้อความไปหนึ่งตำแหน่ง
ABC → BCD
Man → NBO
can → DBO
แสดงผลออกทางหน้าจอเป็นอักษรพิมพ์ใหญ่ทั้งหมด'''



def shift_characters(input_text):
    # ตรวจสอบความยาวของข้อความ
    if len(input_text) != 3:
        print("Word length is mismatched")
    else:
        # ขยับตัวอักษร
        shifted_text = ''.join(
            chr(((ord(char) - ord('A') + 1) % 26) + ord('A')) if char.isupper() else
            chr(((ord(char) - ord('a') + 1) % 26) + ord('a')) for char in input_text
        )

        # แสดงผลทางหน้าจอ
        print(f"Ciphertext is {shifted_text}")

# รับข้อความจากผู้ใช้
user_input = input("Enter 3 characters: ")

# เรียกใช้ฟังก์ชัน
shift_characters(user_input.upper())
