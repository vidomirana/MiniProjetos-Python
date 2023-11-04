from getpass import getpass
palavra = getpass('Digite a palavra a ser adivinhada: ').upper()
dica = str(input('Escreva a dica: ')).capitalize()
vazio = []
for i in range(len(palavra)):
    vazio.append('_')
for t in range(1, len(palavra) + 2):  #LOOP DE TENTATIVAS
    print()
    print(f'A dica é: {dica}')
    print(vazio)
    if '_' not in vazio:   #SE ACERTAR APENAS CHUTANDO LETRAS
        print()
        print('PARABÉNS, VOCÊ ACERTOU!')
        print(f'A palavra era {palavra}')
        break
    tent = str(input(f'Tentativa {t}. Digite uma letra: ')).strip().upper()
    if tent == palavra:    #SE ACERTAR DIGITANDO A PALAVRA INTEIRA
        print()
        print('PARABÉNS, VOCÊ ACERTOU!!')
        print(f'A palavra era {palavra}')
        break
    if tent[0] in palavra:
        for p, l in enumerate(palavra):  #ADICIONA A LETRA CHUTADA NA POSIÇÃO CORRETA
            if l == tent[0]:
                vazio.pop(p)
                vazio.insert(p,l)
if '_' in vazio and tent != palavra:
    print('VOCÊ PERDEU!! ')
