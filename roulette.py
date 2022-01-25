# Imports
import random
from math import ceil
import string


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

def est_manque(n:int) -> bool:
    """
        Cette fonction retourne 'True' si le chiffre est entre 0 et 18
        Parameters : 
            n (int) : un entier quelconque
        Returns:
            b (bool) : True if n is [0, 18]
    """
    return n >= 0 and n <= 18

def est_rouge(n:int) -> bool:
    """
        Cette fonction retourne 'True' si le chiffre est rouge
        Parameters : 
            n (int) : un entier quelconque
        Returns:
            b (bool) : True if n in dans la liste des chiffres rouge
    """
    list_rouge = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
    return n in list_rouge

def est_noir(n:int) -> bool:
    """
        Cette fonction retourne 'True' si le chiffre est entre 0 et 18
        Parameters : 
            n (int) : un entier quelconque
        Returns:
            b (bool) : True if n is [0, 18]
    """
    liste_noir = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
    return n in liste_noir

def num_tiers(n:int) -> int:
    """
        Cette fonction retourne 1 si le chiffre est entre 1 et 12, retourne 2 si le chiffre est entre 13 et 24 et retourne 3 si le chiffre est entre 25 et 36
        Parameters : 
            n (int) : un entier quelconque
        Returns:
            n (int) : 1 if n in [0, 12], 2 if in [13, 24] and 3 if n in [25, 36]
    """
    return ceil(n / 12) # On arrondi par excès

def num_lignes(n:int) -> int:
    """
        Cette fonction retourne 1 si le chiffre appartient à la première ligne, 2 si le chiffre appartient à la deuxième etc..
        Parameters : 
            n (int) : un entier quelconque
        Returns:
            n (int) : 1 if n is in the first line, 2 if n is in the second line and more...
    """
    return ceil(n / 3) # On arrondi par excès

def num_colonnes(n:int) -> int:
    """
        Cette fonction retourne 1 si le chiffre est à la ligne et à la colonne 1 etc...
        Parameters:
            n (int) : un entier quelconque
        Returns:
            n (int) : 1 if n is in the first line and at the first column and more...
    """
    """
        n = (l - 1) * 3 + c car pour retrouver le chiffre n, nous comptons combien de chiffres avant cette ligne (l - 1 * 3),
        puis on rajoute le numéro de colonnes correspondant.
        c = n - 3 * (l - 1)
        l = ceil(n/3)
    """
    return n - 3 * (ceil(n / 3) - 1)
    
from typing import Union

def calucler_gain(n:int, pari:Union[int, str], mise:int) -> int:
    """
        Cette fonction prend en paramètre n, le pari du joueur et la mise en retour
        Parameters:
            n (int) : un entier quelconque
        Returns:
            n (int) : 1 if n is in the first line and at the first column and more...
    """

    if pari == n:
        return mise*36

    elif pari == "rouge" and est_rouge(n) == True:
        return mise*2

    elif pari == "noir" and est_noir(n):
        return mise*2

    elif pari == "pair" and est_pair(n):
        return mise*2

    elif pari == "impair" and est_impair(n):
        return mise*2

    elif pari == "manque" and est_manque(n):
        return mise*2

    elif pari == "passe" and est_passe(n):
        return mise*2

    elif type(pari) == str and pari[0] == "T" and num_tiers(n) == int(pari[1]):
        return mise*3

    elif type(pari) == str and pari[0] == "C" and num_colonnes(n) == int(pari[1]):
        return mise*3

    elif type(pari) == str and pari[0] == "L" and num_lignes(n) == int(pari[1:]):
        return mise*12

    else:
        return 0
