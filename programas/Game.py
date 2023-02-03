from time import sleep
from random import randint

cont = 0
pcChoose = randint(1, 10)

print("Vamos jogar um jogo!")
sleep(0.5)
print("Eu escolho um número em 1 e 10 e você tenta adivinhar, cobinados?")
print("Estou pensando",end="")
for i in range(0, 5):
    print(".", end="")
    sleep(0.75)

print("\nPensei :)")
sleep(0.5)


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
