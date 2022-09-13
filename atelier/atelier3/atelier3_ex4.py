# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 14:22:56 2022

@author: lluca
"""

def mot_correspond(mot : str, motif: str)-> bool:
    '''
    bool si le motif correspond au mot

    Parameters
    ----------
    mot : str
        mot.
    motif : str
        motif a point.

    Returns
    -------
    bool
        si motif correspond au mot.

    '''
    if len(mot)==len(motif):
        for i in range(len(mot)):
            if motif[i] != '.':
                if motif[i]!=mot[i]:
                    return False
    else:
        return False
    return True

print(mot_correspond("tarte", "t..t."))

print(mot_correspond("cheval", "c..v..l"))

print(mot_correspond("cheval", "c..v.l"))

def presente(lettre: str, mot: str)->int():
    '''
    si lettre appartient au mot renvoie l'indice de ce dernier sinon renvoie -1

    Parameters
    ----------
    lettre : str
        lettre.
    mot : str
        mot.

    Returns
    -------
    int
        indice ou -1.

    '''
    for i in range(len(mot)):
        if lettre == mot[i]:
            return i
    return -1

print(presente('a','bastia'))
print(presente('a','ajaccio'))
print(presente('a','zebre'))

def mot_possible(mot: str, lettres: str)-> bool:
    """
    return bool si on peut ecrire mot avec lettres

    Parameters
    ----------
    mot : str
        DESCRIPTION.
    lettres : str
        DESCRIPTION.
    Returns
    -------
    bool
        DESCRIPTION.

    """
    liste_mot = []
    liste_lettre = []
    #creation des listes associés au mot et aux lettres
    for lettre in mot:
        liste_mot.append(lettre)
    for lettre in lettres:
        liste_lettre.append(lettre)
    i=0
    while len(liste_mot)>i:
        j=0
        while j<len(liste_lettre):
            if liste_lettre[i]==liste_mot[j]:
                del liste_lettre[i]
                del liste_mot[j]
                break
            j+=1
        i+=1
    return liste_mot==[]
print(mot_correspond('bite', 'itbe'))
        