from biblioteca import *
usuario = []
erros = 0
venceu = False

print("---Bem-vindo ao jogo da forca.---")
while True:
    escolhas = input("Informe a sua escolha: ")
    usuario.append(escolhas.lower())
    for letra in palavra:
        if letra.lower() in usuario:
            print(letra, end=" ")
        else:
            print("_", end=" ")
    print()

    if escolhas.lower() not in palavra.lower():
        erros += 1
        print(f"Você tem {7 - erros} tentativas.")
        desenha_forca(erros)

    venceu = True
    for letra in palavra:
        if letra.lower() not in usuario:
            venceu = False

    if erros == 7 or venceu:
        break

if venceu:
    print(f"Você ganhou, parabéns! A palavra era {palavra}.")
else:
    print(f"Você perdeu! A palavra era {palavra}.")
