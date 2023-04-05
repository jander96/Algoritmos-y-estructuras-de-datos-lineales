def is_alien_sorted(palabras,orden):
    # Crear mapa de diccionario
    mapa_diccionario = {}
    for i in range(0,len(orden)):
        mapa_diccionario[orden[i]] = i
    
    # Revisar el orden de las palabras
    for i in range(1,len(palabras)):
        if not is_sorted(mapa_diccionario,palabras[i-1],palabras[i]):
            return False
    return True
        

def is_sorted(mapa_diccionario: dict, palabra1: str, palabra2: str):
    longitud = min(len(palabra1),len(palabra2))
    for i in range(0,longitud):
        if mapa_diccionario[palabra1[i]] < mapa_diccionario[palabra2[i]]:
            return True
        if mapa_diccionario[palabra1[i]] > mapa_diccionario[palabra2[i]]:
            return False
    #Caso cuando no se retorna nada porque no se cumplió ninguna condicion
    #de arriba sino que todas eran iguales
    return len(palabra1) < len(palabra2)
        


alfabeto= "abcdefghijklmnñopqrstuvwxyz"
palabras = ["ama","amaca","amacaron","amacaronera","be","bebe","camisa","amicaina"]

print(is_alien_sorted(palabras,alfabeto))