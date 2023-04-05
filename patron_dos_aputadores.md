# Patrón de dos apuntadores #

Este es un patron muy utilizado para trabajar con las **listas / array** y es que tenemos
a dos enteros que se refieren a posiciones de indices diferentes en la lista y lo vamos moviendo dependiendo de nuestro problema.

Aplicando la logica cuando _iteramos_ las listas / array ya sea a traves de un for o con un while podemos tener referencias a elementos en diferentes posiciones de dicha lista.

Podemos tener varias conbinaciones:

+ Uno avanza desde el inicio hasta el final y el otro desde el final hasta el inicio de la lista 
+ Ambos avanzan en el mismo sentido pero uno consecutivo al otro 
+ Ambos avanzan en el mismo sentido pero a ritmos diferentes ejemplo uno puede avanzar 2 posiciones y el primer solo una por lo que tenemos un apuntador el doble de veloz que el otro
+ Otras combinaciones que no conozco


Estos apuntadores pueden ser muy utiles en mis algoritmos, los cuales veremos más adelante