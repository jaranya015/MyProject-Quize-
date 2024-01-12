'''รับข้อความจากผู้ใช้
รับคำที่ไม่ต้องการให้แสดงออกมา
เปลี่ยนข้อความที่ไม่ต้องการให้แสดงเป็น * ตามจำนวนตัวอักษรของคำที่ไม่ต้องการให้แสดง
Hello, World! ไม่อยากให้แสดง Hell → ****o, World!
Love, Song ไม่อยากให้แสดง Love → ****, Song
แสดงข้อความออกทางหน้าจอ
ตัวอย่างโปรแกรม

Enter text: Hello, World!
Enter filter word: Hell
Text after filter is "****o, World!"
Hello, World! และ Hell คือข้อความที่ใส่ให้โปรแกรม

enter = input("Enter text: ")
enter2 = input("Enter filter word: ")
encode_text = enter.replace(enter2 , '*'*len(enter2))
print(f'Text after filter is "{encode_text}"')'''
    
    
    
