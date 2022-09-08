# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 10:53:25 2022

@author: lluca
"""
L = [10,5,3,2,5,8,20,4,9,9]

def  sommeL_fori(L : list)->float:
    """
    Calcul la somme des valeurs d'une liste

    Parameters
    ----------
    L : list
        Liste

    Returns
    -------
    float
        Somme des valeurs

    """
    somme = 0
    for i in range (len(L)):
        somme += L[i]
    return somme

def  sommeL_for_e_in(L : list)->float:
    """
    Calcul la somme des valeurs d'une liste

    Parameters
    ----------
    L : list
        Liste

    Returns
    -------
    float
        Somme des valeurs

    """
    somme = 0
    for e in L:
        somme += e
    return somme

def  sommeL_while(L : list)->float:
    """
    Calcul la somme des valeurs d'une liste

    Parameters
    ----------
    L : list
        Liste

    Returns
    -------
    float
        Somme des valeurs

    """
    somme = 0
    element = 0
    while element < len(L) :
        somme += L[element]
        element +=1
    return somme


# La fonction qui utilise for e in Liste semble la plus adaptée.

def test_exercice1():
    """
    Fonction test

    """
    print("TEST SOMME")
    #Test liste vide
    print("Test liste vide : ", sommeL_for_e_in([]))
    #Test liste 1111
    S=[1,10,100,1000,10000]
    print("Test liste 11111 :",sommeL_for_e_in(S))
    return("teste liste while :",sommeL_while(S))

print(test_exercice1())

def moyenne(L : list)-> float:
    """
    renvoie la moyenne des valeurs d'une liste

    Parameters
    ----------
    L : list
        liste a traiter.

    Returns
    -------
    float
        moyenne.

    """
    if len(L)==0: #Cas liste vide
        return 0
    somme = sommeL_for_e_in(L)
    moyenne = somme/len(L)
    return moyenne

def test_moyenne():
    """
    test d'une moyenne quelconque et essai du cas liste vide'

    """
    print("test moyenne quelconque :",moyenne(L))
    return("test moyenne liste vide :",moyenne([]))
print(test_moyenne())

def nb_sup_for_i(L : list,e : int)-> int:
    """
    Prend une liste et un entier, renvoie le nombre d'entiers de la liste 
    supérieurs a l'entier entré en parametre

    Parameters
    ----------
    L : list
        liste.
    e : int
        entier a tester.

    Returns
    -------
    int
        nombre de valeurs supérieur à e.

    """
    compteur = 0
    for i in range (len(L)):
        if L[i]>e:
            compteur += 1
    return compteur

def nb_sup_for_e_in(L : list,e : int)-> int:
    """
    Prend une liste et un entier, renvoie le nombre d'entiers de la liste 
    supérieurs a l'entier entré en parametre

    Parameters
    ----------
    L : list
        liste.
    e : int
        entier a tester.

    Returns
    -------
    int
        nombre de valeurs supérieur à e.

    """
    compteur = 0
    for element in L:
        if element>e:
            compteur += 1
    return compteur
def test_nb_sup():
    """
   Fonction test des fct nb supérieurs
    """
    print("test fonction nb_sup :", nb_sup_for_i(L, 5) )
    
    return("test fonction nb_sup avec liste vide:",nb_sup_for_e_in([], 5))

print(test_nb_sup())

def moyenne_sup(L:list,e:int)-> float:
    """
    récupère la liste des elements de L str supérieur a e et renvoie la moyenne
    de ces derniers

    Parameters
    ----------
    L : list
        liste.
    e : int
        element a évaluer.

    Returns
    -------
    float
        moyenne des element de L supérieurs a e.

    """
    liste_element_sup =[]
    for element in L:
        if element>e:
            liste_element_sup.append(element)
    return moyenne(liste_element_sup)

def test_moyenne_sup():
    """
    Fonction test de la fct moyennne sup

    """
    print("test moyenne_sup liste L :",moyenne_sup(L,5))
    return("test moyenne_sup liste vide",moyenne_sup([],5))
print(test_moyenne_sup())

def val_max(L: list)-> float:
    """
    Renvoie la valeur max d'une liste

    Parameters
    ----------
    L : list
        liste.

    Returns
    -------
    float
        val max de la liste.

    """
    if len(L)==0:
        return 0
    maximum = L[0]
    for e in L :
        if e > maximum:
            maximum = e
    return maximum

def test_val_max():
    """
    fonction test de val_max

    """
    print("test val_max liste L :", val_max(L))
    return ("test val_max liste vide :", val_max([]))

print(test_val_max())

def ind_max(L:list)->int:
    """
    renvoie l'index la valeur max de la liste L

    Parameters
    ----------
    L : list
        liste.

    Returns
    -------
    int
        index de la val max de L.

    """
    if len(L)==0:
        return 0
    index = 0
    maximum = L[0] 
    for i in range(1,len(L)):
        if L[i] > maximum :
            maximum = L[i]
            index = i
    return index


def test_ind_max():
    """
    fonction test de ind_max
    
    """
    print("test ind_max liste L :",ind_max(L))
    return("test ind_max liste vide :",ind_max([]))
print(test_ind_max())
