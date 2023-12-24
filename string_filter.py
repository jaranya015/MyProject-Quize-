enter = input("Enter text: ")
enter2 = input("Enter filter word: ")
encode_text = enter.replace(enter2 , '*'*len(enter2))
print(f'Text after filter is "{encode_text}"')
    
    
    