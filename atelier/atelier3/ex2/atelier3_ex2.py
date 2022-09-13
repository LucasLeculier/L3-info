
def mots_Nlettres(lst_mot : list, n : int)-> list:
    """
    renvoie les mots de lst_mot qui contiennent n lettres

    Parameters
    ----------
    lst_mot : list
        liste de mots.
    n : int
        taille voulu.

    Returns
    -------
    list
        liste des mots de lst_mot contenant n lettres.

    """
    nouvelle_lis = []
    for mot in lst_mot:
        if len(mot) == n:
            nouvelle_lis.append(mot)
    return nouvelle_lis

print(mots_Nlettres(["jouer","bonjour", "punir", "jour", "aurevoir", "revoir", "pouvoir", "cour", "abajour", "finir", "aimer"],5))


def commence_par(prefixe : str,mot : str)-> bool:
    """
    verifie si le mot passé en parametre commence par prefixe

    Parameters
    ----------
    prefixe : str
        début de mot a tester.
    mot : str
        mot a tester.

    Returns
    -------
    bool
        retourne si mot commence par prefixe.

    """
    taille = len(prefixe)
    return prefixe == mot[:taille]


def fini_par(suffixe : str,mot : str)-> bool:
    """
    verifie si le mot passé en parametre fini par suffixe

    Parameters
    ----------
    suffixe : str
        fin de mot a tester.
    mot : str
        mot a tester.

    Returns
    -------
    bool
        retourne si mot fini par suffixe.

    """
    taille = len(suffixe)
    return suffixe == mot[-taille:]

print(commence_par('pu', 'punir'))
print(commence_par('z', 'punir'))
print(fini_par('unir', 'punir'))
print(fini_par('pu', 'punir'))


def commencent_par(prefixe : str, lst_mot : list)->list:
    """
    renvoie la liste des mots de lst_mot qui commencent pas prefixe

    Parameters
    ----------
    prefixe : str
        début de mot.
    lst_mot : list
        liste des mots a tester

    Returns
    -------
    list
        liste mots valides.

    """
    nouvelle_list = []
    taille = len(prefixe)
    for mot in lst_mot:
        if prefixe == mot[:taille]:
            nouvelle_list.append(mot)
    return nouvelle_list


def finissent_par(suffixe : str, lst_mot : list)->list:
    """
    renvoie la liste des mots de lst_mot qui finissent pas suffixe

    Parameters
    ----------
    suffixe : str
        fin de mot.
    lst_mot : list
        liste des mots a tester

    Returns
    -------
    list
        liste mots valides.

    """
    nouvelle_list = []
    taille = len(suffixe)
    for mot in lst_mot:
        if suffixe == mot[-taille:]:
            nouvelle_list.append(mot)
    return nouvelle_list

LISTE = ["jouer","bonjour", "punir", "jour", "aurevoir", "revoir", "pouvoir", "cour", "abajour", "finir", "aimer"]

print(commencent_par('jou', LISTE))
print(commencent_par('z', LISTE))
print(finissent_par('our',LISTE))
print(finissent_par('pu', LISTE))


def liste_mots (lst_mot : list, prefixe : str, suffixe : str, n : int) :
    """
    récupère les mots de la liste qui commencent pas prefixe, finissent par suffixe
    et continennent n caractères

    Parameters
    ----------
    lst_mot : list
        liste.
    prefixe : str
        debut de mot.
    suffixe : str
        fin de mot
    n : int
        taile du mot.

    Returns
    -------
liste des mots validés
    """
    lst_n = mots_Nlettres(lst_mot, n)
    list_pref = commencent_par(prefixe, lst_n)
    list_suf = finissent_par(suffixe, list_pref)
    return list_suf

print(liste_mots(['intraveineuse','maison'], 'intra', 'euse', 13))

FICHIER = open('littre.txt','r',encoding='utf-8')

def d(fichier):
    f = open(fichier)
    c = f.readline()
    while c !='':
        print(c)
        c = FICHIER.readline()
    fichier.close()
d('littre.txt')

