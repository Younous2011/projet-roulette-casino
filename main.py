from roulette import *

tune = 1000

name = demander_nom()
afficher_regle(name)


while tune > 0:
    print("-"*50)
    pari = demander_pari()
    mise = demander_mise(tune, 500)
    tirage = tirer_numero()
    tune = tune - mise
    gain = calculer_gain(tirage, pari, mise)
    tune = tune + gain

    afficher_tirage(tirage)
    if gain > 0:
        print(f"Wouah ! Vous avez gagné {gain}€ !")
    else:
        print("En fait, vous êtes nul 😁")
    print(f"Tune: {tune}€")