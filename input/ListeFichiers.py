# -*- coding:Utf-8 -*-
import os

from os.path import join


class ListeFichiers():
    """
    Cette classe aggrège sous forme d'une liste tous les fichiers dont il faut déterminer la langue.
    """

    """
    La liste des fichiers à étudier (pour le moment sous la forme de leur chemin absolu)
    """
    listeDesFichiers = []

    def __init__(self, emplacementFichiers):
        """
        Le constructeur reçoit un chemin absolu d'un fichier ou d'un dossier. Avec, il doit déterminer la liste des
         fichiers à étudier.
        :param emplacementFichiers: L'emplacement (chemin absolu ou relatif) d'un fichier ou d'un dossier.
        """
        if(os.path.isfile(emplacementFichiers)):
            # Si c'est un fichier simple, on ajoute tout bêtement son chemin absolu à la liste.
            self.listeDesFichiers.append(os.path.abspath(emplacementFichiers))

        elif(os.path.isdir(emplacementFichiers)):
            # Mais si il s'agit d'un dossier, on récupère tous ses fichiers pour les jouter
            # NON RÉCURSIF ! ÇA N'A AUCUN INTÉRÊT.
            listeComplete = os.listdir(emplacementFichiers)

            for fichier in listeComplete:
                if(os.path.isfile(emplacementFichiers + fichier)):
                    self.listeDesFichiers.append(os.path.abspath(emplacementFichiers + fichier))

            #self.listeDesFichiers = [f for f in os.listdir(emplacementFichiers) if os.path.isfile(join(emplacementFichiers, f))]

        else:
            print("Le chemin spécifié ne correspond pas à un fichier.")

        print(self.listeDesFichiers)