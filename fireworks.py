print("Fireworks Counter")
def frireworke():
    dict_frirework = {}
    while True :
        input_frire_worke = input("Enter color code: ").lower()
        color = ''.join(char for char in input_frire_worke if char.isalpha())
        count = ''.join(char for char in input_frire_worke if char.isdigit())
        if input_frire_worke == "END" or input_frire_worke == "end" :
            break
        
        if color and count:  
            count = int(count) 
            dict_frirework[color] = dict_frirework.get(color, 0) + (count)
    
        print(f"{color}\t->\t{count}")
                
    print("Fireworks Statistic") 
    for key, value in dict_frirework.items():
        print(f"{key}\t->\t{value}")
        
frireworke()
    
                