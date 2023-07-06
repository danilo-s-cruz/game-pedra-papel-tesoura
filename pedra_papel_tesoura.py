"""
Neste projeto do jogo pedra, papel e tesoura.
Os jogadores serão o usuário e o computador.
"""
import random

def resultado(user, computer):
    if user == computer:
        return(f"Você: {user} \nComputador: {computer} \nEmpate!")       
    elif user == "R" and computer == "T":
        return(f"Você: {user} \nComputador: {computer} \nVocê GANHOU!!")
    elif user == "P" and computer == "R":
        return(f"Você: {user} \nComputador: {computer} \nVocê GANHOU!!")
    elif user == "T" and computer == "P":
        return(f"Você: {user} \nComputador: {computer} \nVocê GANHOU!!")
    else:
        return(f"Você: {user} \nComputador: {computer} \nVocê perdeu...")

codigo = ["R", "P", "T"] #R: Pedra, P: Papel, T: Tesoura
while True:
    user = input("Escolha: Ped[r]a, [P]apel, [T]esoura ou [S]air: ").strip().upper()
    if user == "S":
        print("Finalizando... Até mais!")
        break
    if user not in codigo:
        print("Escolha Invalida - Tente Novamente!")
        continue
    computer = random.choice(codigo)
    print(resultado(user, computer))