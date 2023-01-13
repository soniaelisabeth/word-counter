def character_counter(words):
    counter = 0
    
    for word in words:
        if word == "\n":
            continue
        counter = counter + 1
    
    return counter