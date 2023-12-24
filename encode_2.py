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