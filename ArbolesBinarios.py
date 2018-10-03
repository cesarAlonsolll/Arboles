# -*- coding: utf-8 -*-
"""
Created on Tue Oct 02 08:53:40 2018

@author: cesar alonso
"""

class ArbolBinario():
    
    def __init__(self, dato, izq=None, der=None):
        self.dato = dato
        self.izq = izq
        self.der = der
    
def buscarEnArbol(dato, arbol):
    if dato == arbol.dato:
        return True
    elif dato>arbol.dato:
        if arbol.der!=None:
            return buscarEnArbol(dato, arbol.der)
        else:
            return False
    elif dato<arbol.dato:
        if arbol.izq!=None:
            return buscarEnArbol(dato, arbol.izq)
        else:
            return False
        
def contarNodos(arbol):
     if arbol==None:
         return 0
     elif arbol.izq==None==arbol.der:
         return 0
     else:
         return 1 + contarNodos(arbol.izq) + contarNodos(arbol.der)

def contarHojas(arbol):
    if arbol==None:
        return 0
    elif arbol.izq==None==arbol.der:
        return 1
    else:
        return contarHojas(arbol.izq)+contarHojas(arbol.der)

def contarElementos(arbol):
    if arbol==None:
        return 0
    else:
        return 1+contarElementos(arbol.der)+contarElementos(arbol.izq)
    
def insertarElemento(dato, arbol):
    if arbol==None:
        arbol=ArbolBinario(dato)
    else:
        if dato < arbol.dato:
            arbol.izq=insertarElemento(dato,arbol.izq)
        else:
            arbol.der=insertarElemento(dato,arbol.der)
    return arbol

def preOrden(arbol):
    if arbol==None:
        return []
    elif arbol.izq==None==arbol.der:
        return [arbol.dato]
    else:
        return [arbol.dato]+preOrden(arbol.izq)+preOrden(arbol.der)

def posOrden(arbol):
    if arbol==None:
        return []
    elif arbol.izq==None==arbol.der:
        return [arbol.dato]
    else:
        return posOrden(arbol.izq)+posOrden(arbol.der)+[arbol.dato]

def enOrden(arbol):
    if arbol==None:
        return []
    elif arbol.izq==None==arbol.der:
        return [arbol.dato]
    else:
        return enOrden(arbol.izq)+[arbol.dato]+enOrden(arbol.der)
    
a1 = ArbolBinario(dato=12,
                     izq=ArbolBinario(dato=8,
                                      izq=ArbolBinario(dato=4),
                                      der=ArbolBinario(dato=10,
                                                   izq=ArbolBinario(dato=9),
                                                   der=ArbolBinario(dato=11))
                                      ),
                     der=ArbolBinario(dato=25,
                                      izq=ArbolBinario(dato=17),
                                      der=ArbolBinario(dato=30,
                                                   izq=ArbolBinario(dato=28),
                                                   der=ArbolBinario(dato=50))
                                      ))
