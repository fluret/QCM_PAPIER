    """_summary_
    """

import os
from tkinter import messagebox
from tkinter.filedialog import askopenfilename

from gest_zip import extraction
from settings import *
from gest_pdf import *

PREMIERE_PAGE = False
REMPLACE_PREM = False
directory = os.getcwd()

if (
    messagebox.askyesno(
        "Choix pour la première page", "Souhaitez vous conserver la première page ?"
    )
    is True
):
    PREMIERE_PAGE = True
    if (
        messagebox.askyesno(
            "Remplacement de la première page",
            "Souhaitez-vous remplacer cette première page ?"
            "(Si oui vous devez choisir le fichier en question)",
        )
        is True
    ):
        REMPLACE_PREM = True
        prem_page = askopenfilename(initialdir=directory)
        directory2 = os.path.split(prem_page)[0]

NB_PDF = 0
PAGE_DEP = 0

if os.path.exists("Result.pdf"):
    os.remove("Result.pdf")

filename = askopenfilename(initialdir=directory,title="Choisir le fichier zip à traiter")
directory = os.path.split(filename)[0]
filename =os.path.split(filename)[1]

NB_PDF = extraction(filename, directory, LISTES_EXTRACT)

a, b = trouve_max(directory)

maxs,_ = a
maxg, egal = b

if not egal:
    messagebox.showinfo(
    "Avertissement",
    "Les grilles n'ont pas toutes le même nombre"
    " pages. Cela peut poser des problèmes.",
    )

if maxs % 2 != 0:
    if not PREMIERE_PAGE:
        maxs -= 1
    else:
        maxs += 1

if not PREMIERE_PAGE:
    PAGE_DEP = 1

pdf_merger = PdfMerger()
for i in range(NB_PDF // 2):
    with open(os.path.join(directory, "Result" + str(i + 1) + ".pdf"), "wb") as f:
        output = PdfWriter()
        if REMPLACE_PREM:
            with open(prem_page, "rb") as pdfFileObjPremPage:
                pdf_prem_page = PdfReader(pdfFileObjPremPage)
                output.addPage(pdf_prem_page.getPage(0))
                output.write(f)
            PAGE_DEP = 1
        with open(os.path.join(directory, liste_sujet[i]), "rb") as pdfFileObjSujet:
            pdf = PdfReader(pdfFileObjSujet)
            for j in range(PAGE_DEP, len(pdf.pages)):
                output.add_page(pdf.pages[j])
            for k in range(0, maxs - len(output.pages)):
                output.add_blank_page
            output.write(f)
        j = 0
        with open(os.path.join(directory, Liste_Grille[i]), "rb") as pdfFileObjGrille:
            pdf = PdfReader(pdfFileObjGrille)
            for j in range(len(pdf.pages)):
                output.add_page(pdf.pages[j])
                output.add_blank_page
            for k in range(1, (maxg * 2) - (2 * len(pdf.pages)) + 1):
                output.add_blank_page
            output.write(f)
    pdf_merger.append(os.path.join(directory, "Result" + str(i + 1) + ".pdf"))
with open(os.path.join(directory, "Result.pdf"), "wb") as output_file:
    pdf_merger.write(output_file)

messagebox.showinfo(
    "Fin du travail",
    "Travail terminé : le fichier result.pdf a été correctement généré",
)
