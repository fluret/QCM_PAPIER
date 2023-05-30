import os
from PyPDF2 import PdfReader, PdfWriter

def add_blank_pages_to_match_even_page_count(folder_path):
    pdf_files = [f for f in os.listdir(folder_path) if f.endswith('.pdf')]

    # Trouver le nombre de pages maximum parmi les fichiers PDF du dossier
    max_pages = 0
    for pdf_file in pdf_files:
        file_path = os.path.join(folder_path, pdf_file)
        with open(file_path, 'rb') as file:
            reader = PdfReader(file)
            num_pages = len(reader.pages)
            if num_pages > max_pages:
                max_pages = num_pages

    # Ajouter des pages blanches pour atteindre un nombre total de pages pair
    for pdf_file in pdf_files:
        file_path = os.path.join(folder_path, pdf_file)
        with open(file_path, 'rb') as file:
            reader = PdfReader(file)
            num_pages = len(reader.pages)
            if num_pages < max_pages:
                # Créer un nouveau writer pour ajouter les pages blanches
                writer = PdfWriter()
                for page in reader.pages:
                    writer.add_page(page)

                # Ajouter les pages blanches nécessaires
                num_blank_pages = max_pages - num_pages
                for _ in range(num_blank_pages):
                    blank_page = writer.add_blank_page()

                # Créer un nouveau fichier PDF avec les pages blanches ajoutées
                output_path = os.path.join(folder_path, f"{os.path.splitext(pdf_file)[0]}_with_blank_pages.pdf")
                with open(output_path, 'wb') as output_file:
                    writer.write(output_file)

                print(f"Le fichier {pdf_file} a été mis à jour avec {num_blank_pages} pages blanches.")

# Exemple d'utilisation
folder_path = 'chemin/vers/votre/dossier'
add_blank_pages_to_match_even_page_count(folder_path)