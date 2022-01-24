from roulette import *


# tests generate random
def test_generate_random_1():
    for _ in range(100):
        assert tirer_numero() <= 36, "-random doit générer un chiffre infèrieur à 36"

def test_generate_random_2():
    for _ in range(100):
        assert tirer_numero() >= 0, "-random doit générer un chiffre supérieur à 0"

# tests est_pair
def test_est_pair_1():
    assert est_pair(3) == False, "3 est un chiffre impair"

def test_est_pair_2():
    assert est_pair(4) == True, "4 est un chiffre pair"

# tests est_impair
def test_est_impair_1():
    assert est_impair(3) == True, "3 est un chiffre impair"

def test_est_impair_2():
    assert est_impair(4) == False, "4 est un chiffre pair"

# tests est_passe
def test_est_passe_1():
    assert est_passe(3) == False, "3 n'est pas passe"

def test_est_passe_2():
    assert est_passe(26) == True, "26 est passe"

def test_est_passe_3():
    assert est_passe(19) == True, "19 est passe"

def test_est_passe_4():
    assert est_passe(36) == True, "36 est passe"

def test_est_passe_5():
    assert est_passe(18) == False, "18 n'est pas passe"

def test_est_passe_6():
    assert est_passe(37) == False, "37 n'est pas passe"

# tests est_manque
def test_est_manque_1():
    assert est_manque(3) == True, "3 est manque"

def test_est_manque_2():
    assert est_manque(26) == False, "26 n'est pas manque"

def test_est_manque_3():
    assert est_manque(18) == True, "18 est manque"

def test_est_manque_4():
    assert est_manque(0) == True, "36 est manque"

def test_est_manque_5():
    assert est_manque(19) == False, "19 n'est pas manque"

def test_est_manque_6():
    assert est_manque(-1) == False, "-1 n'est pas manque"

# test est_rouge
def test_est_rouge_1():
    assert est_rouge(3) == True, "3 est rouge"

def test_est_rouge_2():
    assert est_rouge(2) == False, "2 n'est pas rouge"

# test est_noir
def test_est_noir_1():
    assert est_noir(2) == True, "2 est noir"

def test_est_noir_2():
    assert est_noir(3) == False, "3 n'est pas noir"

# test est_noir
def test_num_tiers_1():
    io = [
        [5, 1],
        [1, 1],
        [12, 1],
        [13, 2],
        [15, 2],
        [24, 2],
        [25, 3],
        [27, 3],
        [36, 3]
    ]
    for i in range(len(io)):
        assert num_tiers(io[i][0]) == io[i][1], f"{io[i][0]} appartient au tiers {io[i][1]}"

def test_num_lignes_1():
    io = [
        [1, 1],
        [3, 1],
        [13, 5],
        [15, 5],
        [31, 11],
        [33, 11]
    ]
    for i in range(len(io)):
        assert num_lignes(io[i][0]) == io[i][1], f"{io[i][0]} appartient à la ligne {io[i][1]}"

def test_num_colonnes_1():
    io = [
        [1, 1],
        [3, 3],
        [13, 1],
        [15, 3],
        [31, 1],
        [33, 3]
    ]
    for i in range(len(io)):
        assert num_colonnes(io[i][0]) == io[i][1], f"{io[i][0]} appartient à la ligne {io[i][0]} et à la colonne {io[i][1]}"