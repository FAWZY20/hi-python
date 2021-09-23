from random import randint

ton_score = 0
mon_score = 0
fin = 5

def ecrire(nombre):
    if nombre == 1:
        print("pierre", end=" ")
    elif nombre == 2:
        print("papier", end=" ")
    else:
        print("ciseaux", end=" ")


def augmenter_scores(mon_coup, ton_coup):
    global mon_score, ton_score
    if mon_coup == 1 and ton_coup == 2:
        ton_score += 1
    elif mon_coup == 2 and ton_coup == 1:
        mon_score += 1
    elif mon_coup == 1 and ton_coup == 3:
        mon_score += 1
    elif mon_coup == 3 and ton_coup == 1:
        ton_score += 1
    elif mon_coup == 3 and ton_coup == 2:
        mon_score += 1
    elif mon_coup == 2 and ton_coup == 3:
        ton_score += 1

def gagnant():

    if ton_score == fin:
        print("Vous avez gagner")
    elif mon_coup== fin:
        print("Vous avez perdut")

def rejouer():  
        ton_choix = int(input("Voulez-vous rejouez ? 1 : oui, 2: non -> "))
        if ton_choix == 1:
            start()
        else:
            print("merci d'avoir jouer")       

def start():

    while mon_score < fin and ton_score < fin:
    
        mon_coup = randint(1, 3)
        ton_coup = int(input("1 : pierre, 2 : papier, 3 : ciseaux ? "))
        while ton_coup < 1 or ton_coup > 3:
            ton_coup = int(input("1 : pierre, 2 : papier, 3 : ciseaux ? "))
        print("Vous montrez "+ str(ton_coup) + " il montre " + str(mon_coup), end="\n")
        augmenter_scores(mon_coup, ton_coup)
        print("mon score et de -> " + str(mon_score) + " son score et de -> " + str(ton_score), end="\n" )

    print(gagnant(), end="")

start()
rejouer()