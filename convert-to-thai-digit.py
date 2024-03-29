'''รับเลขอารบิกเป็นจํานวนเต็มจากผู้ใช้ 5 ตัวอักษร
แปลงเลขอารบิกเป็นเลขไทย
รับค่า 12345
แสดงค่า ๑๒๓๔๕
ใช้ความรู้เรื่อง สตริง
Enter only 5 Arabic number: 12345
Thai number is ๑๒๓๔๕
12345 คือค่าที่ป้อนให้โปรแกรม'''

# option 1

def convert_to_thai(digit):
    dict_thai = {'1':'๑', '2':'๒', '3':'๓', '4':'๔', '5':'๕', '6':'๖', '7':'๗', '8':'๘', '9':'๙', '0':'๐'}
    thai_number = ''.join([dict_thai[str(d)] for d in digit])
    return thai_number
    
    
enter_number = [int(x) for x in input("Enter only 5 Arabic number: ")]
print(f'Thai number is {convert_to_thai(enter_number)}')

# option 2

alphabet = "abcdefghijklmnopqrstuvwxyz"
input_enter = input("Enter 5 characters: ").lower()
encryption = []

for char_in_input_enter in input_enter:
    if char_in_input_enter in alphabet:
        encrypted_char = alphabet[-(alphabet.index(char_in_input_enter) + 1)]
        encryption.append(encrypted_char)

result = ''.join(encryption)
print('Encryption is', result)

