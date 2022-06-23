gabarito = ['a', 'f', 'c', 'd', 'd', 'a', 'e', 'e', 'b', 'a']

questao1 = input('Diga a resposta da questão 1 de a até f:')
questao2 = input('Diga a resposta da questão 2 de a até f:')
questao3 = input('Diga a resposta da questão 3 de a até f:')
questao4 = input('Diga a resposta da questão 4 de a até f:')
questao5 = input('Diga a resposta da questão 5 de a até f:')
questao6 = input('Diga a resposta da questão 6 de a até f:')
questao7 = input('Diga a resposta da questão 7 de a até f:')
questao8 = input('Diga a resposta da questão 8 de a até f:')
questao9 = input('Diga a resposta da questão 9 de a até f:')
questao10 = input('Diga a resposta da questão 10 de a até f:')

resposta = [questao1, questao2, questao3, questao4, questao5, questao6, questao7, questao8, questao9, questao10]
for i in resposta:
    print('suas respostas:', i)

for i in gabarito:
    print('reposta correta:', i)

cont = 0
if resposta[0] != gabarito[0]:
    print('Questão 1: você errou marcando', resposta[0],',', 'o correto é:', gabarito[0])
else:
    print('Questão 1: Sua resposta está correta!!!!', resposta[0])
    cont = cont + 1

if resposta[1] != gabarito[1]:
    print('Questão 2: você errou marcando', resposta[1],',', 'o correto é:', gabarito[1])
else:
    print('Questão 2: Sua resposta está correta!!!!', resposta[1])
    cont = cont + 1

if resposta[2] != gabarito[2]:
    print('Questão 3: você errou marcando', resposta[2],',', 'o correto é:', gabarito[2])
else:
    print('Questão 3: Sua resposta está correta!!!!', resposta[2])
    cont = cont + 1

if resposta[3] != gabarito[3]:
    print('Questão 4: você errou marcando', resposta[3],',', 'o correto é:', gabarito[3])
else:
    print('Questão 4: Sua resposta está correta!!!!', resposta[3])  
    cont = cont + 1  

if resposta[4] != gabarito[4]:
    print('Questão 5: você errou marcando', resposta[4],',', 'o correto é:', gabarito[4])
else:
    print('Questão 5: Sua resposta está correta!!!!', resposta[4])
    cont = cont + 1

if resposta[5] != gabarito[5]:
    print('Questão 6: você errou marcando', resposta[5],',', 'o correto é:', gabarito[5])
else:
    print('Questão 6: Sua resposta está correta!!!!', resposta[5])
    cont = cont + 1

if resposta[6] != gabarito[6]:
    print('Questão 7: você errou marcando', resposta[6],',', 'o correto é:', gabarito[6])
else:
    print('Questão 7: Sua resposta está correta!!!!', resposta[6])
    cont = cont + 1

if resposta[7] != gabarito[7]:
    print('Questão 8: você errou marcando', resposta[7],',', 'o correto é:', gabarito[7])
else:
    print('Questão 8: Sua resposta está correta!!!!', resposta[7])
    cont = cont + 1

if resposta[8] != gabarito[8]:
    print('Questão 9: você errou marcando', resposta[8],',', 'o correto é:', gabarito[8])
else:
    print('Questão 9: Sua resposta está correta!!!!', resposta[8])
    cont = cont + 1

if resposta[9] != gabarito[9]:
    print('Questão 10: você errou marcando', resposta[9],',', 'o correto é:', gabarito[9])
else:
    print('Questão 10: Sua resposta está correta!!!!', resposta[9])
    cont = cont + 1

print('Sua nota foi:', cont,'/',10)

for i in range(0,10): # o i vai variar de 0 a 9
  if respostasDoAluno[i] == gabarito[i]:
    print('Questão', i,' está correta!')
  else:
    print('Questão', i,' não está correta. A resposta correta é ', gabarito[i])
