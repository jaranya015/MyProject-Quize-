# รับข้อความจากผู้ใช้
user_input = input("กรุณาใส่ข้อความ (3 ตัวอักษร): ")

# ตรวจสอบความยาวของข้อความ
if len(user_input) != 3:
    print("Word length is mismatched")
else:
    # ขยับตัวอักษร
    shifted_text = ''.join(chr((ord(char) - ord('A') + 1) % 26 + ord('A')) for char in user_input)

    # แสดงผลทางหน้าจอเป็นอักษรพิมพ์ใหญ่ทั้งหมด
    print("ผลลัพธ์:", shifted_text.upper())
    
'''ฟังก์ชัน chr() ในภาษา Python ใช้สำหรับแปลงรหัส ASCII 
หรือ Unicode ให้กลับเป็นตัวอักษรที่เกี่ยวข้อง
print(chr(65))  # ผลลัพธ์คือ 'A'
print(chr(97))  # ผลลัพธ์คือ 'a'
print(chr(8364))  # ผลลัพธ์คือ '€' '''
    