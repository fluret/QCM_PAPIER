import os
from PyPDF2 import PdfReader, PdfWriter

def add_blank_page_if_odd(pdf_path):
    # Ouvrir le fichier PDF en lecture
    with open(pdf_path, 'rb') as file:
        reader = PdfReader(file)
        num_pages = len(reader.pages)

        # Vérifier si le nombre de pages est pair
        if num_pages % 2 != 0:
            # Créer un nouveau writer pour ajouter la page blanche
            writer = PdfWriter()

            # Copier les pages existantes du lecteur au writer
            for page in reader.pages:
                writer.add_page(page)

            # Ajouter une page blanche
            blank_page = writer.add_blank_page()

            # Créer un nouveau fichier PDF avec la page blanche
            output_path = os.path.splitext(pdf_path)[0] + '_with_blank_page.pdf'
            with open(output_path, 'wb') as output_file:
                writer.write(output_file)

            print(f"Une page blanche a été ajoutée au fichier : {output_path}")
        else:
            print("Le nombre de pages est pair. Aucune modification nécessaire.")

# Exemple d'utilisation
pdf_path = 'chemin/vers/votre/fichier.pdf'
add_blank_page_if_odd(pdf_path)