'''รับจำนวนแถวและสัญลักษณ์ จากนั้นวาดต้นไม้ยอดชี้ลง

Enter the number of rows: 6
Enter print symbol: *
***********
 *********
  *******
   *****
    ***
     *
6 และ * คือข้อมูลที่ป้อนให้โปรแกรม'''

enter = int(input("Enter the number of rows: "))
enter2 = input("Enter print symbol: ")
for i in range(enter, 0, -1):
    spaces = " " * (enter - i)
    symbols = enter2 * (2 * i - 1)
    print(f'{spaces}{symbols}')
