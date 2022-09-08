# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 15:47:59 20221
@author: lluca
"""

L = [1,5,7,-7,0,4,-9,-10,0,-1]

def separer(L : list)-> list:
    """
    prend une liste en argument et renvoie une liste contenant les elements
    négatifs a gauche, les positifis a droite et les 0 au milieu sans tri

    Parameters
    ----------
    L : list
        liste de départ.

    Returns
    -------
    list
        liste séparée.

    """
    LSEP = []
    negatifs = 0
    positifs = len(L)-1
    zeros = 0
    for e in L :
        if e<0:
            LSEP.insert(negatifs, e)
            negatifs += 1
        elif e>0:
            LSEP.insert(positifs, e)
            positifs -= 1
        else:
            zeros += 1
    for i in range (zeros):
        LSEP.insert(negatifs, 0)
        negatifs += 1
    print("Liste LSEP :",LSEP)
    print("liste L :",L)



separer(L)