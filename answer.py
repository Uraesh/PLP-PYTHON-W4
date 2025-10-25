def process_file():
    try:
        filename = input("Entrez le nom du fichier à lire : ")
        with open(filename, "r") as infile:
            content = infile.readlines()

        with open("output.txt", "w") as outfile:
            for line in content:
                outfile.write(line.upper())

        print("Le fichier 'output.txt' a été créé avec succès.")

    except FileNotFoundError:
        print("Erreur : le fichier spécifié est introuvable.")
    except IOError:
        print("Erreur : impossible de lire ou écrire dans le fichier.")
    except Exception as e:
        print(f"Une erreur inattendue est survenue : {e}")

process_file()
