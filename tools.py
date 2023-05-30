#fonction qui prend une liste en argument et renvoie la liste
#la valeur max de la liste et vrai si tous les éléments sont égaux
def max_et_egalite(liste):
    max_val = max(liste)
    egalite = all(x == liste[0] for x in liste)
    return [max_val, egalite]

