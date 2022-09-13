# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 14:07:31 2022

@author: lluca
"""



NOM = "lucas leculier"

def nom_prenom(name:str)-> str:
    """
    Prend un nom et un prénom, met le nom en maj
    et la premiere lettre du prenom en maj
    ----------
    name : str
nom + prenom
    Returns
    -------
    str
        nom + prenom modifiés.

    """
    
    prenom = (name.split())[0].capitalize()
    nom = (name.split())[1].upper()
    return prenom + " " + nom

print(nom_prenom(NOM))


def is_domaine(domaine:str)->bool:
    """
    retourne un bool si le domaine entré en parametre est valide

    Parameters
    ----------
    domaine : str
        domaine.

    Returns
    -------
    bool
        bool.

    """
    res=True 
    if domaine[0]=='.' or domaine[-1]=='.' or '..' in domaine : 
        res=False 
    else: 
        i=0 
        taille=len(domaine) 
    while i<taille and res: 
            if not (domaine[i].isalnum() or '.'==domaine[i] or '-' ==domaine[i] ) :
                res=False
            i+=1 
    return res

def is_corps(corps:str)->bool:
    '''
    boolean de la validité du corps

    Parameters
    ----------
    corps : str
        corps.

    Returns
    -------
    bool
        bool.

    '''
    res=True 
    if domaine[0]=='.' or domaine[-1]=='.' or '..' in domaine : 
        res=False 
    else: 
        i=0 
        taille=len(domaine) 
    while i<taille and res: 
            if not (domaine[i].isalnum() or '.'==domaine[i] or '_' ==domaine[i] ) :
                res=False
            i+=1 
    return res


def is_mail(mail:str)->(int,int):
    """
    verifie la validité d'un mail entré en parametre'

    Parameters
    ----------
    mail : str
        mail a check.

    Returns
    -------
    (int,int)
        tuple vérifiant.

    """
    
    
    # verification du arobase
    if not '@' in mail:
        return (0,2)
    
    # arobse donc on peut crée le corps et le domaine
    corps = mail.split('@')[0]
    domaine = mail.split('@')[1]
    
    #verification du . du domaine
    if not '.' in domaine:
        return (0,4)
    

    #validité du corps
        
    elif not is_corps(corps):
        return (0,1)
    #validité du domaine
    elif not is_domaine(domaine):
        return (0,3)
    #si ca marche
    return (1,0)

print(is_mail('bisgambiglia@univ-corse.fr'))
print(is_mail('bijds@univ-corse.fr'))
print(is_mail('bisgambigliauniv-corse.fr'))
print(is_mail('bisgambiglia@univ-co/rse.fr'))
print(is_mail('bisgambiglia@univ-corsefr'))