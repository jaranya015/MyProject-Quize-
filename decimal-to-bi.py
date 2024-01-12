'''รับเลขฐาน 10 จำนวนเต็มบวกจากผู้ใช้
แปลงเลขฐาน 10 เป็นเลขฐาน 2
Enter number: 2
2 is 10 in base 2.
2 คือค่าที่ป้อนให้โปรแกรม'''


def decimal_to_binary(decimal):
    binary = ""
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal = decimal // 2
    return binary

decimal = int(input("Enter number: "))
binary = decimal_to_binary(decimal)
print(f"{decimal} is {binary} in base 2.")
