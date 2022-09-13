# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 09:30:11 2022

@author: lluca
"""
import random

def place_lettre(ch : str, mot : str)->list:
    '''
    renvoie une liste de/des emplacements de ch dans mot
    renvoie liste vide si ch n'appartient pas a mot'

    Parameters
    ----------
    ch : str
        caractère a tester.
    mot : str
        mot.

    Returns
    -------
    list
        liste des ch dans mot.

    '''
    lst_final = []
    for i in range (len(mot)):
        if mot[i]==ch:
            lst_final.append(i)
    return lst_final


#placesLettre('b','bonjour')-> [0]•
print(place_lettre("b","bonjour"))

#placesLettre('a','bonjour')-> []•
print(place_lettre('a','bonjour'))

#placesLettre('m','maman')-> [0,2]
print(place_lettre('m','maman'))


def outputStr(mot:str, lpos:list)-> str:
    """
    renvoie la chaine de de caractère correspondant au mot caché et aux lettres
    trouvées

    Parameters
    ----------
    mot : str
        mot a cacher.
    lpos : list
        emplacement des caractères de mot a afficher.

    Returns
    -------
    str
        mot avec lpos affichées.
    """
    string = ''
    for i in range (len(mot)):
        if i in lpos:
            string += mot[i]
        else:
            string += '_'
    return string

#•outputStr('bonjour',[])-> '_ _ _ _ _ _ _'
print(outputStr('bonjour',[]))

#•outputStr('bonjour',[0])-> 'b _ _ _ _ _ _' 
print(outputStr('bonjour',[0]))

#•outputStr('bonjour',[0,1,4])-> 'b o _ _ o _ _' 
print(outputStr('bonjour',[3,1,4]))

#•outputStr('bon',[0,1,2])-> 'bon'
print(outputStr('bon',[0,1,2]))

 

lst =['paris','londres','madrid','berlin','new-york']


    

f_capitales = open('capitales.txt','r')

def build_list(fichier : str) -> list:
    """
    créer une liste via un fichier entré en parametre

    Parameters
    ----------
    fileName : str
        fichier.

    Returns
    -------
    list
        liste.

    """
    liste = []
    f = open(fichier,'r')
    c = f.readline().lower()
    while c:
        liste.append(c.split("\n")[0])
        c = f.readline().lower()
    f.close()
    return liste

CAPITALES = build_list('capitales.txt')


def build_dict(liste: list)-> dict:
    '''
    créer un diction pour ajuster la difficulté 

    Parameters
    ----------
    liste : list
        liste entré.

    Returns
    -------
    dict
        dictionenaire en fonction du nbr de caractères .

    '''
    dictionnaire = {}
    taille_min = len(min(liste,key=(len)))
    taille_max = len(max(liste,key=(len)))
    for i in range (taille_min,taille_max+1):
        liste_inter = []
        for e in liste:
            if len(e)== i:
                liste_inter.append(e)
        dictionnaire[i]= liste_inter
    return dictionnaire
dictionnaire = build_dict(CAPITALES)

def select_word(sorted_words:dict, word_len:int)->str:
    '''
    récupère un mot du dictionnaire en fonction de la difficultée word_len 
    choisie

    Parameters
    ----------
    sorted_words : dict
        dictionnaire.
    word_len : int
        nombre de caractères dans le mot a choisir.

    Returns
    -------
    str
        mot choisis.

    '''
    taille_liste = sorted_words[word_len]
    choix = random.randint(0, len(taille_liste)-1)
    mot = sorted_words[word_len][choix]
    return sorted_words[word_len][choix]


def jeu(liste : list):
    """
    jeu du pendu
    """
    erreurs = 0
    lpos=[]
    mot = ''
    #Choix difficulté avec un while true pour exiger une des 3 réponses
    while True :
        difficulte = input("quel niveau de difficulté souhaitez-vous ? (facile (moins de 7 lettres) \n \
           moyen (de 7 a 9 lettres) \n difficile (plus de 9 lettres \ :")
        if difficulte in ['facile','moyen','difficile']:
            break
    # récupération du nombre de caractère que le mot contiendra
    dictionnaire = build_dict(liste)
    #Le while true sert a éviter les cas ou le nombre de caractère ne correspond
    #A aucun pays i.e. lorsque mot = [] par exemple dictionnaire[16] = []
    while True:
        if difficulte == 'facile':
            #len((min(liste,key=(len)))) récupere le nombre de caractères du mots le plus cours de la liste
            choix = random.randint(len((min(liste,key=(len)))), 6)
        elif difficulte == 'moyen':
            choix = random.randint(7, 9)
        else:
            choix = random.randint(10, len(max(liste,key=(len)))-1)
        mot = select_word(dictionnaire, choix)
        if mot != []:
            break
    while erreurs < 5 :
        #lancement de la partie jeu
        sortie = (outputStr(mot, lpos))
        print(sortie)
        lettre = input('entrez une lettre ')
        if lettre in mot : 
            liste = place_lettre(lettre, mot)
            for e in liste:
                lpos.append(e)
            sortie = (outputStr(mot, lpos))
            if sortie == mot:
                print('gagné')
                exit()
        else :
            erreurs += 1
        print(sortie)
        print('nombre erreur(s) :',erreurs)
    print("perdu vous avez 5 erreurs")
    print("le mot était :", mot)
#jeu(CAPITALES)
print(dictionnaire)