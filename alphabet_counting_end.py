letter_count = {}
while True:
    enter = input("Enter string: ")
    if enter == "end" :
        break
    for char in enter :
        if char.isalpha():
            char_lower = char.lower()
            letter_count[char_lower] = letter_count.get(char_lower,0) + 1
            
print("******************************")
print("*     Alphabet Counting      *")
print("******************************")
for char, count in sorted(letter_count.items()):
    print(f"{char} {count}")
print("******************************")
    
        