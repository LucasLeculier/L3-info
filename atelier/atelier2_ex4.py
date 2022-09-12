# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 16:12:21 2022

@author: lluca
"""
F=[6,5,6,7,4,0,1,5]

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

print("resultat histo F : ",histo(F))

def est_injective(l: list)->bool:
    """
    renvoie true si la fonction entree en parametre est injective

    Parameters
    ----------
    f : list
        liste.

    Returns
    -------
    bool
        fonction injective.

    """
    liste_test = histo(l)
    for e in liste_test:
        if e>1 :
            return False
    return True

def test_est_injective():
    """
    fonction test injectivité

    """
    print("test injectivité fonction non injective :",est_injective(F))
    print("test injectivité fonction injective :",est_injective([1,2,3,4,5,6,7,8]))

test_est_injective()

def est_surjective(l: list)->bool:
    """
    renvoie true si la fonction entree en parametre est surjective

    Parameters
    ----------
    f : list
        liste.

    Returns
    -------
    bool
        fonction surjective.

    """
    liste_test = histo(l)
    for e in liste_test:
        if e==0 :
            return False
    return True

def test_est_surjective():
    """
    fonction test jusjectivité

    """
    print("test injectivité fonction non surjective :",est_injective(F))
    print("test injectivité fonction surjective :",est_injective([1,2,3,4,5,6,7,8]))

test_est_surjective()

def est_bijective(L: list) -> bool :
    """
    renvoie boolean si la liste est bijective

    Parameters
    ----------
    L : list
        liste a tester.

    Returns
    -------
    bool
        est bijective.

    """
    return est_injective(L) and est_surjective(L)

def test_est_bijective():
    """
    fonction test est_bijective

    """
    print("test  fonction non surjective :",est_bijective(F))
    print("test  fonction bijective :",est_bijective([1,2,3,4,5]))
    print("test fonction non injective :",est_bijective([1,1,4]))
    
test_est_bijective()


#Question 2





# Question 3
import matplotlib.pyplot as plt

def test_histogramme_plt(L: list):
    """
    affiche un histogramme en plot

    Parameters
    ----------
    L : list
        DESCRIPTION.

    Returns
    -------
    None.

    """
    plt.hist(L, range = (0, max(L)), bins = 5, color = 'yellow',
                edgecolor = 'red')
    plt.xlabel('valeurs')
    plt.ylabel('nombres')
    plt.title('Exemple d\' histogramme simple')
test_histogramme_plt(F)