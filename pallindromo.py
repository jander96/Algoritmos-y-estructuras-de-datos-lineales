def is_pallindromo(word:str)-> bool:
    pointer_start = 0
    pointer_end = len(word)-1
    
    while pointer_start< pointer_end:
        if word[pointer_start]!= word[pointer_end]:
            return False
        pointer_start +=1
        pointer_end -= 1
    
    return True

print(is_pallindromo("ana"))