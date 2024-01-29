'''หำค่ำ BMI (Body Mass Index)
ฟังก์ชัน read_height_weight() ข้างล่างนี้ อ่านความสูง (หน่วยเป็นเซ็นติเมตร) และน าหนัก (หน่วยเป็นกิโลกรัม) มา
สร้าง numpy array แบบ 2 มิติ ดังตัวอย่างในตารางข้างล่างนี้ (บรรทัดแรกคือจ านวนข้อมูล บรรทัดที่ตามมาคือ ความสูงกับ
น้ าหนัก)
อินพุต ผลที่ได้จำก read_height_weight()
4
160 60
155 62
170 54
180 55
array([[160, 60],
[155, 62],
[170, 54],
[180, 55]])
เอกสารประกอบรายวิชา 241-152 BAISD
14
จงสร้างฟังก์ชัน cm_to_m(x) และ cal_bmi(hw) ในโปรแกรมข้างล่างนี้ ที่มีข้อก าหนดของพารามิเตอร์ และผลลัพธ์ที่
ได้ตามตารางนี้
Function Input Parameter Return value
cm_to_m(x) อำเรย์ 1 มิติ เก็บควำมสูง หน่วยเป็นเซ็นติเมตร
เช่น array([160, 155, 170, 180])
อำเรย์1 มิติ เก็บควำมสูง หน่วยเป็นเมตร
เช่น array([1.6,1.55,1.7,1.8])
cal_bmi(hw) อำเรย์ 2 มิติ ขนำด n แถว 2 คอลัมน์ แต่ละแถว
แทนข้อมูล 1 คู่
คอลัมน์ 0 เก็บควำมสูง (เซ็นติเมตร)
คอลัมน์ 1 เก็บน้ ำหนัก (กิโลกรัม) เช่น
array([[160, 60],
 [155, 62],
 [170, 54],
 [180, 55]])
อำเรย์ 1 มิติ เก็บ bmi ที่ค ำนวณจำกควำม
สูงและน้ ำหนักใน Input Parameter ที่
ได้รับ เช่น
array([23.4375,
25.80645161,
18.68512111, 16.97530864])
และเขียนค าสั่ง
 หาค่าเฉลี่ยของ bmi ทั้งหมดที่ค านวณได้ เก็บใส่ตัวแปร avg_bmi และ
 นับจ านวน bmi ที่ค านวณได้ที่มีค่าน้อยกว่า 18.5
โปรแกรมเริ่มต้น
import numpy as np
def read_height_weight():
list_hw = []
for k in range(int(input())) :
h,w = input().split()
list_hw.append((int(h),int(w)))
return np.array(list_hw)
def cm_to_m(x):
# ???
def cal_bmi(hw):
# ???
def main():
hw = read_height_weight()
bmi = cal_bmi(hw)
avg_bmi = ______________________________________
count_underweight = ____________________________
print('average bmi =', avg_bmi)
print('#bmi < 18.5 =', count_underweight)
exec(input().strip())
เอกสารประกอบรายวิชา 241-152 BAISD
15
ข้อมูลน าเข้า
ค าสั่งในการทดสอบฟังก์ชันที่เขียน
ข้อมูลส่งออก
ผลที่ได้จากค าสั่งที่ป้อนเป็นข้อมูลน าเข้า
ตัวอย่าง
อินพุตจำกแป้นพิมพ์ เอำต์พุตทำงจอภำพ
x=np.array([160,150,140])
print(cm_to_m(x))
print(x)
[ 1.6 1.5 1.4]
[160 150 140]
d=np.array([[100,30],[120,36]]) print(cal_bmi(d)) [ 30. 25.]
main()
4
160 60
155 62
170 54
180 55
average bmi = 21.2260953405
#bmi < 18.5 = 1
'''

import numpy as np
def read_height_weight():
    list_hw = []
    for k in range(int(input())):
        h,w = input().split()
        list_hw.append((int(h),int(w)))
    return np.array(list_hw)

def cm_to_m(x):
    return x /100
    
def cal_bmi(hw):
   heights = cm_to_m(hw[:, 0])
   weights = hw[:, 1] 
   return weights / heights**2
def main():
    hw = read_height_weight()
    bmi = cal_bmi(hw)
    avg_bmi = np.mean(bmi)
    count_underweight = np.count_nonzero(bmi < 18.5)
    print('average bmi =', avg_bmi)
    print('#bmi < 18.5 =', count_underweight)
main()
