'''รับค่าตัวอักษรภาษาอังกฤษจากผู้ใช้มา 5 ตัวอักษร ได้ทั้งพิมพ์ใหญ่ และพิมพ์เล็ก
แปลงตัวอักษรให้เป็นตัวอักษรในตําแหน่งเดียวกันเมื่อกลับด้าน
ผลลัพธ์จะเป็นตัวเล็กทั้งหมด
ABCDE แปลงเป็น zyxwv
Gentle แปลงเป็น tvmgov
ฝึก ใช้ความรู้ที่มี ห้ามใช้ความรู้เรื่องอื่นนะครับ :D
Enter 5 characters: abcde
Encryption is zyxwv
abcde คืออักขระที่ป้อนให้โปรแกรม

Enter 5 characters: zyxwv
Encryption is abcde
zyxwv คืออักขระที่ป้อนให้โปรแกรม

Enter 5 characters: House
Encryption is slfhv
house คืออักขระที่ป้อนให้โปรแกรม'''

def encryption(characters):
    dict_characters = {'a':'z', 'b':'y', 'c':'x', 'd':'w', 'e':'v', 'f':'u', 'g':'t', 'h':'s', 'i':'r', 'j':'q', 'k':'p', 'l':'o', 'm':'n', 'z':'a', 'y':'b', 'x':'c', 'w':'d', 'v':'e', 'u':'f', 't':'g', 's':'h', 'r':'i', 'q':'j', 'p':'k', 'o':'l', 'n':'m'}
    encrypted_text = ''.join([dict_characters.get(char, char) for char in characters])
    return encrypted_text
    # encrypted_text = ''.join([dict_characters.get(char) for char in characters])
    # return encrypted_text()

enter = input("Enter 5 characters: ")
enter.lower()
print(f"Encryption is {encryption(enter)}")




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
