# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 02:26:59 2022

@author: USER
"""

def seriefibo (n):
    lista=[]
    for i in range(0,n):
        if i==0 or i==1:
            lista.append(1)
        else:
            lista.append(lista[-2]+lista[-1])
    return lista


nn=int(input("ingresar un numero "))
lista=seriefibo(nn)
print(lista)


    