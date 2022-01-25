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

# test num_tiers
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

# test num_lignes
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

# test num_colonnes
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

# test calculer_gain
def test_calculer_gain_1():
    assert calucler_gain(10, "rouge", 150) == 0, "10 n'est pas rouge ! Le gain doit être à 0"

def test_calculer_gain_2():
    assert calucler_gain(10, "noir", 100) == 200, "10 est noir ! le gain doit être 200 $"

def test_calculer_gain_3():
    assert calucler_gain(5, 4, 100) == 0, "5 est diffèrent de 4 ! le gain doit être 0$"

def test_calculer_gain_4():
    assert calucler_gain(5, 5, 100) == 3600, "5 est égale à 5 ! le gain doit être 3600$"

def test_calculer_gain_5():
    assert calucler_gain(5, "impair", 100) == 200, "5 est impair ! le gain doit être 200$"

def test_calculer_gain_6():
    assert calucler_gain(4, "pair", 100) == 200, "4 est pair ! le gain doit être 200$"

def test_calculer_gain_7():
    assert calucler_gain(5, "pair", 100) == 0, "5 n'est pas pair ! le gain doit être 0$"

def test_calculer_gain_8():
    assert calucler_gain(4, "impair", 100) == 0, "4 n'est pas impair! le gain doit être 0$"

def test_calculer_gain_9():
    assert calucler_gain(20, "passe", 100) == 200, "20 est passe ! le gain doit être 200$"

def test_calculer_gain_10():
    assert calucler_gain(4, "manque", 100) == 200, "4 est manque! le gain doit être 200$"

def test_calculer_gain_11():
    assert calucler_gain(5, "T1", 100) == 300, "5 est du 1er tiers ! le gain doit être 300$"

def test_calculer_gain_12():
    assert calucler_gain(4, "L2", 100) == 1200, "4 est manque! le gain doit être 1200$"

def test_calculer_gain_13():
    assert calucler_gain(5, "C2", 100) == 300, "5 est de la 2ème colonne ! le gain doit être 300$"

def test_calculer_gain_14():
    assert calucler_gain(1, "T2", 100) == 0, "1 n'est pas du 2ème tiers ! le gain doit être 0$"

def test_calculer_gain_15():
    assert calucler_gain(5, "L5", 100) == 0, "5 n'appartient pas à la ligne 5 ! le gain doit être 0$"

def test_calculer_gain_16():
    assert calucler_gain(5, "C3", 100) == 0, "5 n'appartient pas à la 3ème colonne ! le gain doit être 0$"

def test_calculer_gain_17():
    assert calucler_gain(36, "L12", 100) == 1200, "36 appartient à la ligne 12 ! Le gain doir être 1200$"