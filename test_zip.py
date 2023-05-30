import zipfile
import os

def extraire_pdf_dossiers(zip_path):
    dossiers_a_extraire = ["Grilles de réponses", "Questionnaires"]
    fichiers_pdf_extraits = []

    with zipfile.ZipFile(zip_path, 'r') as zip_file:
        for dossier in dossiers_a_extraire:
            for file_info in zip_file.infolist():
                if file_info.filename.startswith(dossier) and file_info.filename.endswith('.pdf'):
                    file_name = os.path.basename(file_info.filename)
                    zip_file.extract(file_info, path='.')
                    fichiers_pdf_extraits.append(file_name)
                    if dossier == "Grilles de réponses":
                        nouveau_nom = renommer_grille(file_name)
                        nouveau_chemin = os.path.join(os.path.dirname(file_info.filename), nouveau_nom)
                        os.rename(file_name, nouveau_chemin)
                        fichiers_pdf_extraits.remove(file_name)
                        fichiers_pdf_extraits.append(nouveau_chemin)

    return fichiers_pdf_extraits

def renommer_grille(nom_fichier):
    segments = nom_fichier.split('_')
    if len(segments) >= 3:
        lettre = segments[2][0]
        nouveau_nom = f"Grille_{lettre}.pdf"
        return nouveau_nom
    else:
        return nom_fichier
    
zip_path = r's:\QCM_PAPIER\essai\test.zip'
fichiers_extraits = extraire_pdf_dossiers(zip_path)
print("Les fichiers PDF extraits sont :", fichiers_extraits)