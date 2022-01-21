# Imports
import random


# Q1
def tirer_numero() -> int:
    """
        Cette fonction génere un chiffre 'random' entre 0 et 36
    """    
    return random.randint(0, 36)

# Q2
def demander_nom() -> str:
    """
        Cette fonction demande un nom au joueur pour ensuite la retourner
    """
    nom = input("Entrez votre nom : ")
    return nom

# Q3
def est_pair(n:int) -> bool:
    """
        Cette fonction retourne 'True' si le chiffre est pair
        Parameters : 
            n (int) : un entier quelconque
        Returns:
            b (bool) : True if n is even
    """
    if n % 2 == 1:
        return False
    else:
        return True

def est_impair(n:int) -> bool:
    """
        Cette fonction retourne 'True' si le chiffre est impair
        Parameters : 
            n (int) : un entier quelconque
        Returns:
            b (bool) : True if n is odd
    """
    return n % 2 == 1

def est_passe(n:int) -> bool:
    """
        Cette fonction retourne 'True' si le chiffre est entre 19 et 36
        Parameters : 
            n (int) : un entier quelconque
        Returns:
            b (bool) : True if n is [19, 36]
    """
    return n >= 19 and n <= 36
