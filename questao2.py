    #  0  1  2  3  4  5  6  7
M = [[ 0, 0, 0, 0, 0, 0, 0, 0], #0
     [ 0, 1, 1, 1, 0, 0, 0, 2], #1
     [ 0, 0, 1, 0, 0, 0, 0, 2], #2
     [ 0, 0, 0, 0, 0, 0, 0, 2], #3
     [ 0, 0, 0, 3, 3, 3, 3, 0], #4
     [ 0, 0, 0, 0, 0, 0, 0, 0], #5
     [ 0, 4, 0, 0, 0, 0, 0, 0], #6
     [ 0, 0, 0, 0, 0, 5, 5, 0]] #7
   
    #  0  1  2  3  4  5  6  7
J = [[ 0, 0, 0, 0, 0, 0, 0, 0], #0
     [ 0, 0, 0, 0, 0, 0, 0, 0], #1
     [ 0, 0, 0, 0, 0, 0, 0, 0], #2
     [ 0, 0, 0, 0, 0, 0, 0, 0], #3
     [ 0, 0, 0, 0, 0, 0, 0, 0], #4
     [ 0, 0, 0, 0, 0, 0, 0, 0], #5
     [ 0, 0, 0, 0, 0, 0, 0, 0], #6
     [ 0, 0, 0, 0, 0, 0, 0, 0]] #7     

count = 0
while count <14:
    escolhaLinha = int(input('Diga a linha que quer acertar:'))
    escolhaColuna = int(input('Diga a coluna que quer acertar:'))

    escolhaUsuario = M[escolhaLinha][escolhaColuna]

    count = 0
    if M[escolhaLinha][escolhaColuna] > 0:
        print('BOOOOOM! Você acertou uma embarcação!')
        count = count + 1
        if count == 14:
            print('Você venceu a guerra naval!! PARABÉNS!!')
    else:
        print('SPLASH, Bomba na água!')    

#ARMAZENANDO A ESCOLHA DO USUARIO
M[escolhaLinha][escolhaColuna] = J[escolhaLinha][escolhaColuna]

if escolhaUsuario == M[1][1] and escolhaUsuario == M[1][2] and escolhaUsuario == M[1][3] and escolhaUsuario == M[2][2]:
    print('GLUB GLUB GLUB, VOCÊ AFUNDOU O PORTA AVIÕES!')
if escolhaUsuario == M[1][7] and escolhaUsuario == M[2][7] and escolhaUsuario == M[3][7]:
    print('GLUB GLUB GLUB, VOCÊ AFUNDOU O NAVIO DE 3 CANOS!')    
if escolhaUsuario == M[4][3] and escolhaUsuario == M[4][4] and escolhaUsuario == M[4][5] and escolhaUsuario == M[4][6]:
    print('GLUB GLUB GLUB, VOCÊ AFUNDOU O NAVIO DE 4 CANOS!')    
if escolhaUsuario == M[7][5] and escolhaUsuario == M[7][6]:
    print('GLUB GLUB GLUB, VOCÊ AFUNDOU O NAVIO DE 2 CANOS!')    
if escolhaUsuario == M[6][1]:
    print('GLUB GLUB GLUB, VOCÊ AFUNDOU O NAVIO DE 1 CANO!') 
