import os
from pypdf import PdfWriter, PdfReader, PdfMerger
from tools import *

def trouve_max(chemin):
    sujet = []
    grille = []
    for file in os.listdir(chemin):
        if (file.startswith("Grille") or file.startswith("Sujet")) and file.endswith(
            ".pdf"
        ):
            with open(os.path.join(chemin, file), "rb") as pdfFileObj:
                # output = PdfWriter()
                pdf = PdfReader(pdfFileObj)
                if file.startswith("Sujet"):
                    numPages = len(pdf.pages)
                    sujet.append(numPages)
                elif file.startswith("Grille"):
                    numPages = len(pdf.pages)
                    grille.append(numPages)
    return max_et_egalite(sujet), max_et_egalite(grille)