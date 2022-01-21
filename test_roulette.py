from roulette import *

def test_generate_random_1():
    for _ in range(100):
        assert tirer_numero() <= 36, "-random doit générer un chiffre infèrieur à 36"

def test_generate_random_2():
    for _ in range(100):
        assert tirer_numero() >= 0, "-random doit générer un chiffre supérieur à 0"

def test_est_pair_1():
    assert est_pair(3) == False, "3 est un chiffre impair"

def test_est_pair_2():
    assert est_pair(4) == True, "4 est un chiffre pair"

def test_est_impair_1():
    assert est_impair(3) == True, "3 est un chiffre impair"

def test_est_impair_2():
    assert est_impair(4) == False, "4 est un chiffre pair"