'''โปรแกรมสำหรับตู้กดนน้ำอัตโนมัติ โดยที่โปรแกรมจะแสดงสินค้าและราคาออกมาให้ผู้ใช้ดูว่ามีสินค้าอะไรบ้างและมีราคาเท่าใด โดยที่สินค้าและราคาจะมีรายการดังต่อไปนี้

1. Khanom Jak            7 Baht
2. Khanom Kruy      13 Baht
3. Khanom Keemod   9 Baht
4. Khanom Co             3 Baht
5. Khanom Dokdon 22 Baht
เมื่อผู้ใช้เลือกขนมแลัวป้อนจำนวนแล้ว ระบบจะแสดงราคาให้แก่ผู้ใช้ แล้วรอรับจำนวนเงินจากลูกค้า

หากผู้ใช้ป้อนจำนวนเงินไม่พอ ระบบจะแจ้งผู้ใช้ให้ป้อนเงินเพิ่ม
หากผู้ใช้ป้อนเงินครบตามจำนวน ระบบจำแสดงข้อความขอบคุณ
หากผู้ใช้ป้อนเงินเกินกว่าจำนวนเงินค่าขนม ตู้กดขนมจะทอนเงินออกมาเป็นเหรียญ 1 2 5 10 บาทเท่านั้น โดยตู้กดขนมจะแสดงจำนวนเงินทอนและจำนวนเหรีญของแต่ละเหรียญ แล้วระบบจะแสดงข้อความขอบคุณ
Kanom Machine
  1. Khanom Jak             7 Baht
  2. Khanom Kruy           13 Baht
  3. Khanom Keemod          9 Baht
  4. Khanom Co              3 Baht
  5. Khanom Dokdon         22 Baht
Enter your order: 1
Enter quantity: 2
Total: 14 baht
Enter your money: 14
Thank you
1 2 14 คือค่าที่ผู้ใช้ป้อน

Kanom Machine
  1. Khanom Jak             7 Baht
  2. Khanom Kruy           13 Baht
  3. Khanom Keemod          9 Baht
  4. Khanom Co              3 Baht
  5. Khanom Dokdon         22 Baht
Enter your order: 2
Enter quantity: 3
Total: 39 baht
Enter your money: 43
Change: 4 Baht
   2: 2 coins
Thank you
2 3 43 คือจำนวนที่ผู้ใช้ป้อนให้ระบบ

Kanom Machine
  1. Khanom Jak             7 Baht
  2. Khanom Kruy           13 Baht
  3. Khanom Keemod          9 Baht
  4. Khanom Co              3 Baht
  5. Khanom Dokdon         22 Baht
Enter your order: 5
Enter quantity: 4
Total: 88 baht
Enter your money: 100
Change: 12 Baht
   10: 1 coin
   2: 1 coin
Thank you
5 4 100 คือจำนวนที่ผู้ใช้ป้อนให้ระบบ'''



print("Kanom Machine")
print(f"  1. Khanom Jak             7 Baht\n  2. Khanom Kruy           13 Baht\n  3. Khanom Keemod          9 Baht\n  4. Khanom Co              3 Baht\n  5. Khanom Dokdon         22 Baht")
kanom_dict = {"1":7,
              "2":13,
              "3":9,
              "4":3,
              "5":22
              }
enter_order = input("Enter your order: ")
enter_quantity = int(input("Enter quantity: "))
if enter_order in kanom_dict :
    price = kanom_dict[enter_order]
    total = price*enter_quantity
    print("Total:",total,"Bath")
    enter_your_money = int(input("Enter your money: "))
    if total != enter_your_money :
        change = enter_your_money - total
        if change > 0:
            for coin_value in [10, 5, 2, 1]:
                coins = change // coin_value
                if coins > 0:
                    print(f"{coin_value}: {coins} coins")
                    change -= coins * coin_value
        print("Thank you")
                
'''BY AI'''

# print("Kanom Machine")
# print(f"  1. Khanom Jak             7 Baht\n  2. Khanom Kruy           13 Baht\n  3. Khanom Keemod          9 Baht\n  4. Khanom Co              3 Baht\n  5. Khanom Dokdon         22 Baht")

# kanom_dict = {"1": 7, "2": 13, "3": 9, "4": 3, "5": 22}

# while True:  # Loop to allow multiple orders
#     enter_order = input("Enter your order+: ")
#     if enter_order.lower() == 'q':
#         break  # Exit the loop if user enters 'q'

#     try:
#         enter_quantity = int(input("Enter quantity: "))
#     except ValueError:
#         print("Invalid quantity. Please enter a number.")
#         continue  # Skip to the next iteration of the loop

#     if enter_order in kanom_dict:
#         price = kanom_dict[enter_order]
#         total = price * enter_quantity
#         print("Total:", total, "Baht")

#         while True:  # Loop to ensure correct payment
#             try:
#                 enter_your_money = int(input("Enter your money: "))
#             except ValueError:
#                 print("Invalid input. Please enter a number.")
#                 continue

#             if enter_your_money >= total:
#                 change = enter_your_money - total
#                 if change > 0:
#                     print("Change:")
#                     for coin_value in [10, 5, 2, 1]:
#                         coins = change // coin_value
#                         if coins > 0:
#                             print(f"{coin_value}: {coins} coins")
#                             change -= coins * coin_value
#                 print("Thank you!")
#                 break  # Exit the payment loop
#             else:
#                 print("Not enough money. Please enter the correct amount.")
#     else:
#         print("Invalid order. Please try again.")

    