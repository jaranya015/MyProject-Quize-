def convert_to_thai(digit):
    dict_thai = {'1':'๑', '2':'๒', '3':'๓', '4':'๔', '5':'๕', '6':'๖', '7':'๗', '8':'๘', '9':'๙', '0':'๐'}
    thai_number = ''.join([dict_thai[str(d)] for d in digit])
    return thai_number
    
    
enter_number = [int(x) for x in input("Enter only 5 Arabic number: ")]
print(f'Thai number is {convert_to_thai(enter_number)}')