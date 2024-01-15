'''โปรแกรมเพื่อนับเลขมงคลโดยรับตัวเลขจากผู้ใช้ 2 ตัวเลข แทน 2 หลัก (i,j) ที่มีค่าตั้งแต่ 0 - 9

ตัวเลขแต่ละหลัก สามารถมีเลขที่เป็นไปได้ตั้งแต่ 0 ถึงตัวเลขนั้น
ตัวเลขแต่ละหลักสามารถประกอบกันกลับหลักอื่นจนกว่าจะครบทุกความเป็นไปได้
รับค่าตัวเลขมงคลจากผู้ใช้
นับตัวเลขเฉพาะชุดที่ หาร ด้วยเลขมงคลลงตัว
ตัวอย่างการสร้างชุดตัวเลข - i = 2 - j = 3 เลขที่เป็นไปได้คือ 00 01 02 03 10 11 12 13 20 21 22 23

Enter number i: 2
Enter number j: 2
Enter magic number: 2
Found 6 magic numbers
2 2 2 คือตัวเลขที่ป้อนให้กลับโปรแกรม

Enter number i: 3
Enter number j: 5
Enter magic number: 5
Found 8 magic numbers
3 5 5 คือตัวเลขที่ป้อนให้กลับโปรแกรม

Enter number i: 3
Enter number j: 2
Enter magic number: 5
Found 4 magic numbers
3 2 5 คือตัวเลขที่ป้อนให้กลับโปรแกรม'''





def find_magic_numbers(num_i, num_j, magic):
    count = 0
    for i in range(num_i + 1):
        for j in range(num_j + 1):
            num = str(i) + str(j)
            if int(num) % magic == 0:
                count += 1
    return count

num_i = int(input("Enter number i: "))
num_j = int(input("Enter number j: "))
magic = int(input("Enter magic number: "))
count = find_magic_numbers(num_i, num_j, magic)
print(f"Found {count} magic numbers")


'''-----------------------------------------------'''





num_i = int(input("Enter number i: "))
num_j = int(input("Enter number j: "))
magic = int(input("Enter magic number: "))

numbers = [str(i) + str(j) for i in range(num_i + 1) for j in range(num_j + 1)]

count = sum(1 for num in numbers if int(num) % magic == 0)

print(f"Found {count} magic numbers")
