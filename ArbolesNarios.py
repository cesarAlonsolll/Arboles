# -*- coding: utf-8 -*-
"""
Created on Tue Oct 02 13:29:48 2018

@author: cesar alonso
"""

class ArbolNario():
    
    def __init__(self, dato, arboles=[]):
        self.dato = dato
        self.arboles = arboles
        
def buscarEnArbol_1(dato, arbol):
    
    def buscarEnArbol_2(dato, lista):
        if lista==[]:
            return False
        else:
            return buscarEnArbol_1(dato, lista[0]) or buscarEnArbol_2(dato, lista[1:])
    
    if arbol.arboles==[]:
        return dato==arbol.dato
    else:
        if dato==arbol.dato:
            return True
        else:
            return buscarEnArbol_1(dato, arbol.arboles[0]) or buscarEnArbol_2(dato, arbol.arboles[1:])
        
def contarElementos_1(arbol):
    
    def contarElementos_2(lista):
        if lista==[]:
            return 0
        else:
            return contarElementos_1(lista[0])+contarElementos_2(lista[1:])
    
    if arbol.arboles==[]:
        return 1
    else:
        return 1+contarElementos_1(arbol.arboles[0])+contarElementos_2(arbol.arboles[1:])
    
a1 = ArbolNario(dato=2,
                arboles=[ArbolNario(dato=4,
                                    arboles=[ArbolNario(dato=12),ArbolNario(dato=24),ArbolNario(dato=40)]),
                         ArbolNario(dato=8,
                                    arboles=[ArbolNario(dato=16),ArbolNario(dato=32)]),
                         ArbolNario(dato=5,
                                    arboles=[ArbolNario(dato=25),ArbolNario(dato=50)])])
