from time import sleep
from random import randint

cont = 0
pcChoose = randint(1, 10)

print("Vamos jogar um jogo!")
print("Eu escolho um número em 1 e 10 e você tenta adivinhar, cobinados?")

while True:
    cont += 1
    playerChoose = int(input("Digite sua tentativa: "))
    if playerChoose == pcChoose:
        print("Você acertou!")
        break
    else:
        print("Você errou hahaha!")
        if playerChoose > pcChoose:
            print("Chute um pouco mais baixo")

        if playerChoose < pcChoose:
            print("Chute um pouco mais alto")

print(f"Você acertou na {cont}ª tentativa!")
