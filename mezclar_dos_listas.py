def merge_sorted(nums1: list, n : int, nums2: list, m : int) -> list:
    # Crea los apuntadores 
    p1 = n-1
    p2 = m-1
    p = len(nums1)-1

    # Ciclo hasta que alguno de la listas llegue al menor
    while  p1 >= 0 and p2 >= 0:
        if nums1[p1] < nums2[p2]:
            nums1[p] = nums2[p2]
            p2 -= 1
        else:
            nums1[p] = nums1[p1]
            p1 -= 1
        p -= 1
    # Tenemos el caso en el que las listas no tienen el mismo tamaño
    # Esto quiere decir que la lista de elementos mayores habrá llegado a -1 
    # primero, que es la condicion que cierra el ciclo, quedando sin evaluar 
    # elementos del listado donde son mas pequeños los valores.Esto quiere
    # decir que la lista que queda sin evaluar, todos sus items son mas
    # pequeños que la lista que se evaluó y ademas al tratarse de elementos 
    # ordenados es solo añadirlos al inicio de la lista que vamos a retornar 
    # como resultado. Si la lista que termino mas rapido fue la primera y nos 
    # quedaron elementos de la 2da lista, es solo añadir estos al inicio, Si 
    # la lista que termino mas rapido fue la segunda esto quiere decir, que los
    # elementos que quedaron en la primera son los mas pequeños y ya estan ordenados
    # y no hay que añadir nada, por tanto solo evaluamos añadir los elementos de la 
    # segunda lista en la primera y no lo contrario
    if n != m:
        nums1[:p2+1] = nums2[:p2+1]

    return nums1


list1 = [1, 2, 3, 9, 0, 0, 0]
list2 = [23, 43, 83]

print(merge_sorted(list1,4, list2,3))
