import random

Usuario = 0
Computador = 0
a = 1

papel = "Papel"
pedra = "Pedra"
tesoura = "Tesoura"
opcoes = [papel, pedra, tesoura]
print("\t  O JOGO ACABOU DE COMEÇAR")

while a > 0:
    comp = random.choice(opcoes)
    esc = input("{}\n".format(opcoes))
    if comp == "Papel":
        if esc == "Papel":
            print("Empatou, Computador tambem colocou {}".format(comp))
        elif esc == "Pedra":
            print("Perdeu, Computador colocou {}".format(comp))
            Computador = Computador + 1
        elif esc == "Tesoura":
            print("Ganhou, Computador colocou {}".format(comp))
            Usuario = Usuario + 1
    elif comp == "Pedra":
        if esc == "Papel":
            print("Ganhou, Computador colocou {}".format(comp))
            Usuario = Usuario + 1
        elif esc == "Pedra":
            print("Empatou, Computador tambem colocou {}".format(comp))
        elif esc == "Tesoura":
            print("Perdeu, Computador colocou {}".format(comp))
            Computador = Computador + 1
    elif comp == "Tesoura":
        if esc == "Papel":
            print("Perdeu, Computador colocou {}".format(comp))
            Computador = Computador + 1
        elif esc == "Pedra":
            print("Ganhou, Computador colocou {}".format(comp))
            Usuario = Usuario + 1
        elif esc == "Tesoura":
            print("Empatou, Computador tambem colocou {}".format(comp))
    print("Placar: Computador = {} | Usuario = {}".format(Computador, Usuario))
    final = input("Gostaria de jogar novamente? (sim/nao)\n")
    if final == "nao":
        print("\t  FIM DE JOGO\n")
        break
