#code du tictac toe modifiable

import time


#dimensions
DIMENSIONS = int(input("Entrez la valeur de la dimension de tableau que vous voulez"))

#table
TABLE_DATA = []

for i in range(DIMENSIONS**2):
    TABLE_DATA.append(str(i+1))


#creation du tableau

def tableau(DIMENSIONS : int, TABLE_DATA:list[str]):
    j=0
    i = 0
    row=''
    d = DIMENSIONS
    print('-'*DIMENSIONS*4)
    while i < DIMENSIONS:
        for elt in TABLE_DATA[j:d]:
            if len(elt) == 1:
                row += '|  '+elt+'  |'
            else :
                row += '|  '+elt+' |'
        i += 1
        print(row)
        print('-'*DIMENSIONS*4)
        row = ''
        j += DIMENSIONS
        d += DIMENSIONS


def intro(DIMENSIONS: int)-> tuple[str]:
    print('*'*33)
    print("|BIENVENUE AU JEU DU TIC TAC TOE|", sep="  ")
    print('*'*33)
    print("\n")

    time.sleep(3)
    nom1 = input("Entrer le nom du premier joueur\n")
    nom2 = input("Entrer le nom du deuxième joueur\n")

    print(nom1, " , ", nom2, "Voici le tableau de jeux   ")
    tableau(DIMENSIONS, TABLE_DATA)

    time.sleep(2)
    print("Le joueur", nom1," auras les 'X' et le joueur ", nom2," auras les 'O'")
    time.sleep(1)

    print("Les règles sont simples.")
    time.sleep(1)
    print("Vous choisissez un numero de case à remplacer avec votre signe")
    time.sleep(1)

    print("Pret ????? ")
    time.sleep(1)
    print("Que le meilleur gagne")
    time.sleep(1)
    return nom1, nom2


def winner_if(DIMENSIONS:int, nom1:str, nom2: str):
    combinaisons_gagnantes = []
    x = 0

    # Check rows
    for y in range(DIMENSIONS, DIMENSIONS**2 + 1, DIMENSIONS):
        combinaisons_gagnantes.append(TABLE_DATA[x:y])
        x = y

    # Check columns
    for r in range(DIMENSIONS):
        combo1 = []
        for j in range(r, len(TABLE_DATA), DIMENSIONS):
            combo1.append(TABLE_DATA[j])
        combinaisons_gagnantes.append(combo1)

    # Check main diagonal
    combo2 = []
    for i in range(DIMENSIONS):
        combo2.append(TABLE_DATA[(DIMENSIONS + 1) * i])
    combinaisons_gagnantes.append(combo2)

    # Check anti-diagonal
    combo3 = []
    for i in range(1, DIMENSIONS + 1):
        combo3.append(TABLE_DATA[(DIMENSIONS - 1) * i])
    combinaisons_gagnantes.append(combo3)

    # Check for a winner
    for combo in combinaisons_gagnantes:
        if all(x == combo[0] for x in combo) and combo[0] in ['X', 'O']:
            if combo[0] == 'X':
                print("Le gagnant est ", nom1)
            else:
                print("Le gagnant est ", nom2)
            return 0
    return None


res = []
def play_turn(nom:str, signe:str, DIMENSIONS:int):
    print("C'est le tour du joueur", nom," de jouer")
    val = int(input( ))
    while val in res or val > DIMENSIONS**2 or val < 1:
        val = int(input("Entrez un autre numéro de case"))
    res.append(val)
    TABLE_DATA[val-1] = signe
    tableau(DIMENSIONS, TABLE_DATA)



def game_launch(nom1:str, nom2:str, DIMENSIONS: int):
    for i in range(DIMENSIONS**2):
        if i % 2 == 0 :
            play_turn(nom1, 'X', DIMENSIONS)
        else :
            play_turn(nom2, 'O', DIMENSIONS)
        if winner_if(DIMENSIONS, nom1, nom2) == 0:
            break





def main():
    nom1, nom2 = intro(DIMENSIONS)
    game_launch(nom1, nom2, DIMENSIONS)
main()