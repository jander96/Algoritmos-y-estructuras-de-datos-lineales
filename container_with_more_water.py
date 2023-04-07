#Vamos encontrar el mayor area posible
# Definimos dos apuntadores que representen los lados de mi contenedor 


def container_analizer(lista):
    p1= 0
    p2 = len(lista)-1
    mayor_area = 0
    while p1 != p2:
        base = p2 - p1
        if lista[p1]<lista[p2]: altura = lista[p1]
        else: altura =lista[p2]
        area = base * altura
        
        if area > mayor_area: mayor_area = area
        
        if lista[p1] > lista[p2]: p2-=1 
        else : p1+=1
    
    return mayor_area
    
alturas = [1,8,6,2,5,4,8,3,7]  
print(container_analizer(alturas))