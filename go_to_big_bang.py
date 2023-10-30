"""
En el a˜no 2049 se descubrieron los agujeros de gusano. Un agujero de gusano es un t´unel que a
traviesa el espacio y el tiempo. Los agujeros de gusano tienen algunas propiedades peculiares:
• Los agujeros de gusano son unidireccionales.
• El tiempo que se tarda en viajar a trav´es de un agujero de gusano es insignificante.
• Un agujero de gusano tiene dos extremos, cada uno situado en un sistema estelar.
• Un sistema estelar puede tener m´as de un punto final de agujero de gusano dentro de sus l´ımites.
• Por alguna raz´on desconocida, partiendo de nuestro sistema solar, siempre es posible acabar en
cualquier sistema estelar siguiendo una secuencia de agujeros de gusano.
• Entre cualquier par de sistemas estelares hay como m´aximo un agujero de gusano en cada direcci´on.
• No hay agujeros de gusano con ambos puntos finales en el mismo sistema estelar.
• Todos los agujeros de gusano tienen una diferencia de tiempo constante entre sus puntos finales. Por
ejemplo, un agujero de gusano puede hacer que la persona que viaja a trav´es de ´el termine 15 a˜nos en
el futuro. Otro agujero de gusano puede hacer que la persona termine 42 a˜nos en el pasado.
Una f´ısica brillante que vive en la Tierra quiere utilizar los agujeros de gusano para estudiar el Big Bang.
Para esto ella encontr´o la forma de viajar al pasado usando los agujeros de gusano. Escriba un algoritmo
(escrito en Java,Python,c) que le permita a ella saber si es posible hacer esto. Los sistema estelares ser´an
nombrados usando n´umeros naturales: 0,1,2,... nuestro sistema estelar es el 0. Su algoritmo recibir´a una
lista de la siguiente manera:
[ cantidad_sistamas_estelares: Nat,
cantidad_agujero_gusano: Nat,
viajes_agujeros_gusano: List[List[Int]]]
]
Donde un ejemplo de la lista viajes_agujeros_gusano puede ser: [0,4,20]. Significando que una
persona puede viajar por un agujero de gusano para llegar del sistema estelar 0 al 4 pero
terminar´a 20 a˜nos en el futuro. Dada una entrada como la descrita anteriormente, su algoritmo debe responder True cuando sea posible viajar al Big Bang y False en otro caso. La
complejidad m´axima del algoritmo debe ser O(cantidad sistamas estelares3
). A continuaci´on se
muestran algunos ejemplos:
[2,2[[0,1,-1],[1,0,0]]] -> True
[4,4,[[0 1 10],[1 2 20],[2 3 30],[3 0 -60]] -> False
[3,3,[[0,1,1000],[1,2,15],[2,1,-42]] -> True
[6,10,[[3,0,119],[1,4,-267],[3,1,232],[5,0,-87],[3,2,466],[0,2,-172],
[0,4,18],[1,5,537],[3,5,-307],[0,3,844]]] -> False
"""

def floyd_warshall(adjacency_matrix):
    for intermediate in range(len(adjacency_matrix)):
        for initial in range(len(adjacency_matrix)): 
            for final in range(len(adjacency_matrix)):
                if adjacency_matrix[initial][intermediate] + adjacency_matrix[intermediate][final] <= adjacency_matrix[initial][final]:
                    adjacency_matrix[initial][final] = adjacency_matrix[initial][intermediate] + adjacency_matrix[intermediate][final]

    for initial in range(len(adjacency_matrix)):
            if adjacency_matrix[initial][initial] < 0:
                return True
    
    return False



def main():
    sistemas_cantidad, _, conexiones = eval(input())
    adjacency_matrix = [[0 if i==j else float('inf') for i in range(sistemas_cantidad)] for j in range(sistemas_cantidad) ]
    for conexion in conexiones:
        adjacency_matrix[conexion[0]][conexion[1]] = conexion[2]
    print(floyd_warshall(adjacency_matrix))

main()