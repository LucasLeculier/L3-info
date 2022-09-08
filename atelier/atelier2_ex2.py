# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 13:40:17 2022

@author: lluca
"""

L = [10,5,3,2,6,8,20,4,13,7]

def position(L : list,e : int)-> int:
    """
    Renvoie la position de l'entier e dans la liste L
    renvoie -1 si e n'appartiens pas a L'

    Parameters
    ----------
    L : list
        liste.
    e : int
        entier a tester.

    Returns
    -------
    int
        index de la liste.

    """
    if e in L:
         index = 0
         for i in L:
             if i == e:
                 return index
             else: index += 1
    return -1


def position_while(L : list,e : int)-> int:
    """
    Renvoie la position de l'entier e dans la liste L
    renvoie -1 si e n'appartiens pas a L'

    Parameters
    ----------
    L : list
        liste.
    e : int
        entier a tester.

    Returns
    -------
    int
        index de la liste.

    """
    if e in L:
        
        index = 0
        while True :
                if L[index] == e:
                    return index
                else: index += 1
    return -1



def test_pos():
    """
    test de la fonction position dans les deux cas

    """
    print("test position avec e qui appartient a L :", position(L, 20))
    print ("test position avec e qui n'appartient pas a L :",position_while(L, 0))

test_pos()


S = [10,5,5,7,9,4]

def nb_occurences(L: list, e : int)-> int:
    """
    Calcul le nombre d'occurence d'un entier dans une liste donnée

    Parameters
    ----------
    L : list
        liste.
    e : int
        entier a tester.

    Returns
    -------
    int
        nombre de e dans L.

    """
    compteur = 0
    for element in L:
        if element == e:
            compteur += 1
    return compteur

def test_nb_occurences():
    """
    fonction test nb occurence
    """
    print("test nb_occurences liste S :",nb_occurences(S, 5))
    print("test nb_occurences liste vide :",nb_occurences([], 5))

(test_nb_occurences())

def est_triee(L: list)-> bool:
    """
    renvoie true si la liste est triee false si non

    Parameters
    ----------
    L : list
        liste.

    Returns
    -------
    bool
        liste est triee ou non.

    """
    if L:
        index = L[0]
        for i in range(1,len(L)):
            if L[i] < index:
                return False
        return True

def est_triee_while(L: list)-> bool:
    """
    renvoie true si la liste est triee false si non

    Parameters
    ----------
    L : list
        liste.

    Returns
    -------
    bool
        liste est triee ou non.

    """
    if L:
        index = 1
        element = L[0]
        while index < len(L):
            if L[index]<element:
                return False
            else:
                index +=1
        return True
    
def test_est_triee():
    """
    fonction test est_triee
    """
    print("test fct est_triee avec liste triee", est_triee([1,2,3,4,5]))
    print("test fct est_triee_while avec liste triee", est_triee_while([1,2,3,4,5]))
    print("test fct est_triee avec liste non triee",est_triee(L))
    print("test fct est_triee_whille avec liste non triee",est_triee_while(L))

(test_est_triee())

def position_tri(L:list,e:int)->int:
    """
    Recupere la posiition de e dans L via dichotomie

    Parameters
    ----------
    L : list
        liste.
    e : int
        entier a chercher.

    Returns
    -------
    position de e dans L.

    """
    L.sort()
    print(L)
    depart = 0
    arrivee = len(L)-1
    while depart <= arrivee:
        millieu = arrivee + depart // 2
        if L[millieu] == e:
            return millieu
        elif L[millieu]>e:
            arrivee -= 1
        else:
            depart += 1
    
def test_pos_tri():
    """
    test de pos_tri

    """
    print("position de 7 :",position_tri(L, 7))
    
test_pos_tri()

def a_repetition(L : list)-> bool:
    """
    Renvoie true si la liste comporte des répétitions

    Parameters
    ----------
    L : list
        liste.

    Returns
    -------
    bool
        Répétition dans L ou non.

    """
    liste2 = []
    for e in L:
        if e in liste2:
            return True
        else:
            liste2.append(e)
    return False

def test_a_rep():
    """
    fct test a_repetition

    """
    print("test a_rep si répétition :", a_repetition([3,4,3,6]))
    print("test a_rep si pas de répétitions :", a_repetition(L))

test_a_rep()