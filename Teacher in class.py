//เขียนโปรแกรมช่วยอาจารย์มหาลัยท่านหนึ่งตัดสินใจว่าจะสอนหรือเลิกชั้นเรียนหากจำนวนนักศึกษาน้อยกว่าค่าที่ต้องการโดยที่

โปรแกรมจะรับจำนวนนักศึกษาที่ใช้เป็นค่าตัดสินใจ
อาจารย์จะใส่เวลาที่นักศึกษาเข้าชั้นเรียน
0 นักศึกษามาตรงเวลา
มากกว่า 0 ถ้านักศึกษามาสาย
น้อยกว่า 0 ถ้านักศึกษามาก่อนเวลา
ถ้าหากจำนวนนักศึกษามาตรงเวลา และมาก่อนเวลารวมกัน มากกว่าหรือเท่ากับค่าตัดสินใจ
YES ถ้าหากยกเลิกชั้นเรียน
NO ถ้าหากไม่ยกเลิกชั้นเรียน
เขียนโปรแกรมในลักษณะฟังก์ชันโดยแยกส่วนการคำนวณออกจากส่วนรับข้อมูล
ตัวอย่างโปรแกรม
Threshhold Number: 3
Time: -1 -3 4 2
Decision: YES
Threshhold Number: 2
Time: 0 -1 2 1
Decision: No//


//---------------------------------------------------------------------------//
def input_by_user():
    user_input = int(input("Threshhold Number: "))
    return user_input
def calculate():
    user_input = input_by_user()
    user_input_2 = [int(x) for x in input("Time: ").split(" ")]
    count = 0
    for i in user_input_2 :
        if i < 0 :
            count += i
    count = abs(count)
    if count > user_input :
        print("YES")
    else :
        print("NO")
 
    
calculate()    

//-----------------------------------------------------------------------//

# ส่วนการรับข้อมูล
def get_threshold():
    threshold = int(input("Enter the threshold number: "))
    return threshold

def get_times():
    times = [int(x) for x in input("Enter space-separated times: ").split()]
    return times

# ส่วนการคำนวณ
def calculate_threshold_exceed(threshold, times):
    negative_sum = sum([time for time in times if time < 0])
    absolute_sum = abs(negative_sum)
    if absolute_sum > threshold:
        return "YES"
    else:
        return "NO"

# ฟังก์ชันหลัก
def main():
    threshold = get_threshold()
    times = get_times()
    result = calculate_threshold_exceed(threshold, times)
    print("Does the negative sum exceed the threshold?", result)

if __name__ == "__main__":
    main()


