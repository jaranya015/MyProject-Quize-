def decimal_to_binary(decimal):
    binary = ""
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal = decimal // 2
    return binary

decimal = int(input("Enter number: "))
binary = decimal_to_binary(decimal)
print(f"{decimal} is {binary} in base 2.")
