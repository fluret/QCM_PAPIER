import os
from tkinter import messagebox, simpledialog
from tkinter.filedialog import askopenfilename

from gest_zip import extraction
from settings import *
from gest_pdf import *
from settings import *
from tools import genere_nom, supprimer_fichiers_avec_prefixe

# 0 : suppression première page
# 1 : première page d'origine
# 2 : remplacement première page
premiere_page = 0
nb_pdf = 0
page_dep = 1


directory = os.getcwd()
file_prem_page = None

if (
    messagebox.askyesno(
        "Choix pour la première page", "Souhaitez vous conserver la première page ?"
    )
    is True
):
    premiere_page = 1
    page_dep = 0
    if (
        messagebox.askyesno(
            "Remplacement de la première page",
            "Souhaitez-vous remplacer cette première page ?"
            "(Si oui vous devez choisir le fichier en question)",
        )
        is True
    ):
        premiere_page = 2
        page_dep = 1
        file_prem_page = askopenfilename(initialdir=directory)
        directory2 = os.path.split(file_prem_page)[0]


if os.path.exists("Result.pdf"):
    os.remove("Result.pdf")

filename = askopenfilename(
    initialdir=directory, title="Choisir le fichier zip à traiter"
)
directory = os.path.split(filename)[0]
filename = os.path.split(filename)[1]

nb_pdf = extraction(filename, directory, LISTES_EXTRACT)

a, b = trouve_max(directory)

maxs, _ = a
maxg, egal = b

if not egal:
    messagebox.showinfo(
        "Avertissement",
        "Les grilles n'ont pas toutes le même nombre"
        " pages. Cela peut poser des problèmes.",
    )

# Le nombre de page max du sujet doit être pair
# Si sans enlever la première page on est impair
# alors il faut ajouter une page sinon il faut en enlever une
if maxs % 2 != 0:
    if premiere_page != 0:
        maxs += 1
    else:
        maxs -= 1

traite_fichier(maxs, maxg, directory, nb_pdf, premiere_page, page_dep, file_prem_page)

agraffe = maxs + (maxg * 2)

if (
    messagebox.askyesno(
        "Nom du fichier final", "Le nom de votre fichier est il standardisé ?"
    )
    is True
):
    NOM_FICHIER = genere_nom(agraffe, filename)
    NOM_FICHIER = simpledialog.askstring(
        "Confirmation",
        "Modifier le nom généré si nécessaire sinon valider",
        initialvalue=NOM_FICHIER,
    )
else:
    NOM_FICHIER = simpledialog.askstring(
        "Choix du nom", "Saisir le nom que vous souhaitez utiliser"
    )

os.rename(
    os.path.join(directory, "Result.pdf"), os.path.join(directory, NOM_FICHIER + ".pdf")
)

if (
    messagebox.askyesno(
        "Nettoyage", "Souhaitez-vous supprimer les fichiers intermédiaires ?"
    )
    is True
):
    supprimer_fichiers_avec_prefixe(directory, LISTE_SUPPRESSION)



messagebox.showinfo(
    "Fin du travail",
    "Travail terminé : le fichier result.pdf a été correctement généré",
)
