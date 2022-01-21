# Imports
import random


# Q1
def tirer_numero() -> int: 
    return random.randint(0, 36)

# Q2
def demander_nom() -> str:
    nom = input("Entrez votre nom : ")
    return nom

# Q3
def est_pair(n:int) -> bool:
    if n % 2 == 1:
        return False
    else:
        return True
