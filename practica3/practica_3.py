#! /usr/bin/python
# -*- coding: utf-8 -*-

# 3ra Practica Laboratorio
# Complementos Matematicos I
# Consigna: Implementar los siguientes metodos

from practica2 import DisjointSets, partition

'''
Recordatorio:
- Un camino/ciclo es Euleriano si contiene exactamente 1 vez
a cada arista del grafo
- Un camino/ciclo es Hamiltoniano si contiene exactamente 1 vez
a cada vértice del grafo
'''


def Validate_Graph(graph):
    if(type(graph) != tuple):
        raise TypeError('Not graph')
    v,e = graph
    if(type(v) != list):
        raise TypeError('Not graph')
    if(type(e) != list):
        raise TypeError('Not graph')


def check_is_hamiltonian_trail(graph, path):
    """Comprueba si una lista de aristas constituye un camino hamiltoniano
    en un grafo.

    Args:
        graph (grafo): Grafo en formato de listas.
                       Ej: (['a', 'b', 'c'], [('a', 'b'), ('b', 'c')])

        path (lista de aristas): posible camino
                                 Ej: [('a', 'b), ('b', 'c')]

    Returns:
        boolean: path es camino hamiltoniano en graph

    Raises:
        TypeError: Cuando el tipo de un argumento es inválido
    """



def check_is_hamiltonian_circuit(graph, path):
    """Comprueba si una lista de aristas constituye un ciclo hamiltoniano
    en un grafo.

    Args:
        graph (grafo): Grafo en formato de listas.
                       Ej: (['a', 'b', 'c'], [('a', 'b'), ('b', 'c')])

        path (lista de aristas): posible ciclo
                                 Ej: [('a', 'b), ('b', 'c')]

    Returns:
        boolean: path es ciclo hamiltoniano en graph

    Raises:
        TypeError: Cuando el tipo de un argumento es inválido
    """
    pass


def check_is_eulerian_trail(graph, path):
    """Comprueba si una lista de aristas constituye un camino euleriano
    en un grafo.

    Args:
        graph (grafo): Grafo en formato de listas.
                       Ej: (['a', 'b', 'c'], [('a', 'b'), ('b', 'c')])

        path (lista de aristas): posible camino
                                 Ej: [('a', 'b), ('b', 'c')]

    Returns:
        boolean: path es camino euleriano en graph

    Raises:
        TypeError: Cuando el tipo de un argumento es inválido
    """
    pass


def check_is_eulerian_circuit(graph, path):
    """Comprueba si una lista de aristas constituye un ciclo euleriano
    en un grafo.

    Args:
        graph (grafo): Grafo en formato de listas.
                       Ej: (['a', 'b', 'c'], [('a', 'b'), ('b', 'c')])

        path (lista de aristas): posible ciclo
                                 Ej: [('a', 'b), ('b', 'c')]

    Returns:
        boolean: path es ciclo euleriano en graph

    Raises:
        TypeError: Cuando el tipo de un argumento es inválido
    """
    pass


def graph_has_eulerian_trail(graph):
    Validate_Graph(graph)
    if(len(partition(graph).values()) > 1):
        return False
    etiq = {}
    for v in graph[0]: etiq[v] = 0
    for e1,e2 in graph[1]:
        etiq[e1]+= 1
        etiq[e2]+= 1
    impar = 0
    for v in etiq.values():
        if v % 2 :
            impar+= 1
    if impar > 2:
        return False
    return True


    """Comprueba si un grafo no dirigido tiene un camino euleriano.

    Args:
        graph (grafo): Grafo en formato de listas.
                       Ej: (['a', 'b', 'c'], [('a', 'b'), ('b', 'c')])

    Returns:
        boolean: graph tiene un camino euleriano

    Raises:
        TypeError: Cuando el tipo del argumento es inválido
    """



def find_eulerian_trail(graph):
    """Obtiene un camino euleriano en un grafo no dirigido, si es posible

    Args:
        graph (grafo): Grafo en formato de listas.
                       Ej: (['a', 'b', 'c'], [('a', 'b'), ('b', 'c')])

    Returns:
        path (lista de aristas): camino euleriano, si existe
        None: si no existe un camino euleriano

    Raises:
        TypeError: Cuando el tipo del argumento es inválido
    """

    # Sugerencia: Usar el Algoritmo de Fleury
    # Recursos:
    # http://caminoseuler.blogspot.com.ar/p/algoritmo-leury.html
    # http://www.geeksforgeeks.org/fleurys-algorithm-for-printing-eulerian-path/
    pass


def main():
    pass
if __name__ == '__main__':
    main()
