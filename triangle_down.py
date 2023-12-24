enter = int(input("Enter the number of rows: "))
enter2 = input("Enter print symbol: ")
for i in range(enter, 0, -1):
    spaces = " " * (enter - i)
    symbols = enter2 * (2 * i - 1)
    print(f'{spaces}{symbols}')