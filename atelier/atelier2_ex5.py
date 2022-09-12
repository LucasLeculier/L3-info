# -*- coding: utf-8 -*-
def histo(f:list)->list:
    """
    comptage de f

    Parameters
    ----------
    f : list
        liste d'entrée.

    Returns
    --------
    list
        liste de sortie .

    """
    h = []
    for i in range(max(f)):
        h.append(0)
    for e in f:
        h[e-1] += 1
    return h


def vitrine(L: list,e: int)->list:
    """
    prend une liste et renvoie 2 liste de taille max e, 

    Parameters
    ----------
    L : list
        liste.
    e : int
        taille max des listes de sorties.

    Returns
    -------
    list
        vitrines.

    """
    vitrine1 = []
    vitrine2 = []
    liste_bieng = []
    #for element in L:
    histogramme= histo(L)
    
    for i in range (len(histogramme)) :
        if histogramme[i] > 1:
            for j in range (histogramme[i]):
                liste_bieng.append(L[i + 1])
                
    for element in liste_bieng:
        if len(vitrine1) == e or element in vitrine1 :
            if len(vitrine2) == e or element in vitrine2 :
                None
            else:
                vitrine2.append(element)
        else:
             vitrine1.append(element)
    for element in L:
        if len(vitrine1) == e or element in vitrine1 :
            if len(vitrine2) == e or element in vitrine2 :
                None
            else:
                vitrine2.append(element)
        else:
             vitrine1.append(element)
    return vitrine1,vitrine2

        




print(vitrine( [1,2,2,3,4,5,5], 4))
print(histo([1,2,2,3,4,5,5]))