import random as rd
import numpy as np


class KleurenCombo:
    ''' Deze klasse bevat alle attributen en methoden om het spel Mastermind te spelen'''

    def __init__(self, selectie=[0,0,0,0]):
        self.selectie = selectie
        self.create_np_array()

    def create_np_array(self):
        if len(self.selectie) != 4:
            print('Kies exact 4 kleuren')
            self.play_the_game()
        else:
            self.np_selectie = np.array(self.selectie)

    def print_combo(self):
        print(self.np_selectie)

    def play_the_game(self):
        gok = input("Doe een nieuwe gok: ").strip()
        self.selectie = [x.upper() for x in gok]
        self.create_np_array()
        self.vergelijk()

    def vergelijk(self):
        if np.array_equal(start.np_selectie, self.np_selectie):
            print("Proficiat!")
            print(f"Het juiste antwoord was inderdaad: {start.np_selectie}")
        elif np.array_equal(self.np_selectie, ["S", "T", "O", "P"]):
                print(f"Jammer! Het juiste antwoord was: {start.np_selectie}")
        else:
            self.check_colors()
            self.play_the_game()

    def check_colors(self):
        aantal_juiste_plaatsen = 0
        start_kopie = start.np_selectie.copy()
        gok_kopie = self.np_selectie.copy()

        for i in range(4):
            if gok_kopie[i] == start_kopie[i]:
                aantal_juiste_plaatsen += 1
                gok_kopie[i] = "X"
                start_kopie[i] = "Y"

        aantal_foute_plaatsen = 0
        for i in range(4):
            for j in range(4):
                if gok_kopie[i] == start_kopie[j]:
                    aantal_foute_plaatsen += 1
                    gok_kopie[i] = "X"
                    antwoord_kopie[j] = "Y"

        print(f" - {aantal_juiste_plaatsen} letters op de juiste plaats")
        print(f" - {aantal_foute_plaatsen} letters op een foute plaats")


kleuren = ("R", "G", "B", "O", "P", "W")
selectie = [rd.choice(kleuren) for x in range(4)]

# create start object (and print)
start = KleurenCombo(selectie)

start.print_combo()
# create gok object
gok = KleurenCombo()

# start the game
gok.play_the_game()




