import os

#fonction qui prend une liste en argument et renvoie la liste
#la valeur max de la liste et vrai si tous les éléments sont égaux
def max_et_egalite(liste):
    max_val = max(liste)
    egalite = all(x == liste[0] for x in liste)
    return [max_val, egalite]

def genere_nom(agraffe, nom_zip):
    val1 = nom_zip.split('_')[0].replace('$',' ')
    val2 = nom_zip.split('_')[1].replace('$',' ')
    val3 = "_".join(["2_agrafes_toutes_les_", str(agraffe), "pages_RV_agrafes_droites_2pts"])
    nom_fichier = "_".join([val1, val2, val3])
    return nom_fichier

def supprimer_fichiers_avec_prefixe(chemin, prefixes):
    for nom_fichier in os.listdir(chemin):
        for prefixe in prefixes:
            if nom_fichier.startswith(prefixe) and nom_fichier.endswith(".pdf"):
                os.remove(os.path.join(chemin, nom_fichier))