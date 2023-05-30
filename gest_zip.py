from zipfile import ZipFile
import os

def extraction(nomzip, chemin, liste_extract):
    with ZipFile(os.path.join(chemin, nomzip), "r") as zipObj:
        # Get a list of all archived file names from the zip
        NB_PDF = 0
        listOfFileNames = zipObj.namelist()
        # Iterate over the file names
        
        for nomzip in listOfFileNames:
            if nomzip.startswith(tuple(liste_extract)):
                NB_PDF += 1
                zipInfo = zipObj.getinfo(nomzip)
                nom = os.path.split(nomzip)[-1]
                if nom[11] == "r":
                    zipInfo.filename = "Grille" + nom[20] + ".pdf"
                elif nom[11] == "q":
                    zipInfo.filename = "Sujet" + nom[21] + ".pdf"
                zipObj.extract(zipInfo, chemin)
    return NB_PDF