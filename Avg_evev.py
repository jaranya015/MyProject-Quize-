'''เขียนโปรแกรมหาค่าเฉลี่ยของตำแหน่งคู่ในกลุ่มของข้อมูลที่เรียงลำดับแล้วและไม่ซ้ำกัน

รับข้อมูลจากผู้ใช้ 20 ค่า
กำจัดค่าที่ซ้ำกันออกแล้วเรียงลำดับให้เรียบร้อย
แสดงค่าที่เรียงลำดับเรียบร้อยแล้ว
นำค่าที่อยู่ในตำแหน่งคู่มาหาค่าเฉลี่ย
ตัวอย่างการใช้งานโปรแกรม

Enter number #1: 1
Enter number #2: 2
Enter number #3: 3
Enter number #4: 4
Enter number #5: 5
Enter number #6: 6
Enter number #7: 7
Enter number #8: 8
Enter number #9: 9
Enter number #10: 1
Enter number #11: 2
Enter number #12: 3
Enter number #13: 4
Enter number #14: 5
Enter number #15: 6
Enter number #16: 7
Enter number #17: 8
Enter number #18: 9
Enter number #19: 1
Enter number #20: 2
Unique numbers is 1 2 3 4 5 6 7 8 9 
Average number of even position in list is 5.00
Enter number #1: 1
Enter number #2: 4
Enter number #3: 7
Enter number #4: 8
Enter number #5: 54
Enter number #6: 4
Enter number #7: 4
Enter number #8: 54
Enter number #9: 4
Enter number #10: 5
Enter number #11: 54
Enter number #12: 4
Enter number #13: 4
Enter number #14: 1
Enter number #15: 5
Enter number #16: 5
Enter number #17: 12
Enter number #18: 4
Enter number #19: 5
Enter number #20: 4
Unique numbers is 1 4 5 7 8 12 54 
Average number of even position in list is 17.00'''

lst = []
lst3=[]
for i in range(20):
    numbers = int(input(f'Enter number #{i+1}: '))
    lst.append(numbers)

sets = sorted(set(lst))

for i in range(len(sets)):
    if i %2 ==0:
        lst3.append(sets[i])


avg_even = sum(lst3) / len(lst3)
unique_numbers = ' '.join(map(str, sets))

print(f'Unique numbers is {unique_numbers}')
print(f'Average number of even position in list is {avg_even:.2f}')
