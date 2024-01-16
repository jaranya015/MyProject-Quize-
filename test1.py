'''โปรแกรมเพื่อรับข้อความจากผู้ใช้แล้วเปลี่ยนเปลี่ยนตัวอักษรแรกของคำเป็นตัวพิมใหญ่ เช่น

hello world => Hello World
department of computer engineering => Department Of Computer Engineering
55year of Faculty of Engineering => 55year Of Faculty Of Engineering
ping   pong => Ping Pong
ตัวอย่างการใช้งานโปรแกรม
Text: hello world
=> Hello World
ตัวอย่างการใช้งานโปรแกรม
Text: 55year of Faculty of Engineering
=> 55year Of Faculty Of Engineering
ตัวอย่างการใช้งานโปรแกรม
Text: ping   pong
=> Ping Pong'''





# user_input = input("Text: ")
# formatted_text = user_input.title()
# print(f'=> {formatted_text}')

def capitalize_text(text): # สร้าง funtion capitalize_text() ที่มี input string text
    '''                                โดยวิธ๊การทำงานดังนี้        '''
    
    words = text.split() # word แทนด้วยการแยก input string ออกเป็นคำโดยใช้ funtion split()
    
    for i in range(len(words)): # ลูป for ที่วนซ้ำตั้งแต่ตำแหน่ง 0 ถึง ตำแหน่ง len(words)
        
        if words[i].isdigit(): # เป็นเงื่อไขตรวจสอบว่า words ตำแหน่ง i เป็นตัวเลขมั้ย
            
            words[i] = words[i] # หากเป็นตัวเลขให้words ตำแหน่ง i เป็นค่าเดิม
            
        else:                   # หาก if funtion เป็นเท็จ else funtion จะทำงาน
            
            words[i] = words[i].capitalize() # เป็นคำสั่งที่เปลี่ยนตัวอักษรตัวแรกให้เป็นตัวใหญ่ในตำแหน่งที่ i
            
    return ' '.join(words) # คืนค่า string ของ words ที่แก้ไขแล้ว

user_input = input("Text: ") # รับ input Text จากผู้ใช้งาน

formatted_text = capitalize_text(user_input) # formatted_text แทนด้วยการเรียกใช้งาน funtion ของ capitalize_text()

print(f'=> {formatted_text}') # แสดงผล formatted_text ผ่านทางหน้าโดยใช้ format string ช่วยในการจัดตำแหน่งของข้อความ




'''------------------------------------------------------------------------------------------------------------'''



user_input = input("Text :").split()
new_word = ""
for word in range(len(user_input)) :
    if user_input[word].isdigit():
        user_input[word] = user_input[word]
    else :
        user_input[word] = user_input[word].capitalize()
    new_word += user_input[word] + " "
    
print(f'=> {new_word}')
