import os
from pypdf import PdfWriter, PdfReader, PdfMerger
from tools import *
from settings import *

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

def traite_fichier(maxs, maxg, chemin, nb_pdf, prem_page, page_depart, file_prem_page=None):
    pdf_merger = PdfMerger()
    for i in range(nb_pdf // 2):
        with open(os.path.join(chemin, "Result" + str(i + 1) + ".pdf"), "wb") as f:
            output = PdfWriter()
            #si on décide de remplacer lápremière page on ajoute la nouvelle page dans
            #le fichier de destination et on change la page de départ à 1 
            #pour ajouter le reste des pages
            if prem_page == 2:
                with open(file_prem_page, "rb") as pdfFileObjPremPage:
                    pdf_prem_page = PdfReader(pdfFileObjPremPage)
                    output.addPage(pdf_prem_page.getPage(0))
                    output.write(f)
            #Si on conserve la première page (remplacer ou non) page_depart est à 0
            #dans le cas contraire il est à 1. On ajoute toutes les pages à partir 
            #de page_depart puis ona ajoute assez de pages blanches pour atteindre
            #le nombres de pages du sujet le plus long
            with open(os.path.join(chemin, LISTE_SUJETS[i]), "rb") as pdfFileObjSujet:
                pdf = PdfReader(pdfFileObjSujet)
                for j in range(page_depart, len(pdf.pages)):
                    output.add_page(pdf.pages[j])
                for k in range(0, maxs - len(output.pages)):
                    output.add_blank_page()
                output.write(f)
            j = 0
            with open(os.path.join(chemin, LISTE_GRILLES[i]), "rb") as pdfFileObjGrille:
                pdf = PdfReader(pdfFileObjGrille)
                for j in range(len(pdf.pages)):
                    output.add_page(pdf.pages[j])
                    output.add_blank_page()
                for k in range(0, (maxg * 2) - (2*len(pdf.pages))):
                    output.add_blank_page()
                output.write(f)
        pdf_merger.append(os.path.join(chemin, "Result" + str(i + 1) + ".pdf"))
    with open(os.path.join(chemin, "Result.pdf"), "wb") as output_file:
        pdf_merger.write(output_file)