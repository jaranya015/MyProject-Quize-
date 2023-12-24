def encryption(characters):
    dict_characters = {'a':'z', 'b':'y', 'c':'x', 'd':'w', 'e':'v', 'f':'u', 'g':'t', 'h':'s', 'i':'r', 'j':'q', 'k':'p', 'l':'o', 'm':'n', 'z':'a', 'y':'b', 'x':'c', 'w':'d', 'v':'e', 'u':'f', 't':'g', 's':'h', 'r':'i', 'q':'j', 'p':'k', 'o':'l', 'n':'m'}
    encrypted_text = ''.join([dict_characters.get(char, char) for char in characters])
    return encrypted_text
    # encrypted_text = ''.join([dict_characters.get(char) for char in characters])
    # return encrypted_text()

enter = input("Enter 5 characters: ")
enter.lower()
print(f"Encryption is {encryption(enter)}")
