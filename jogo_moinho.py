# 96859 Filipe Resendes

"""
TAD POSICAO
"""

"""
Recebe duas cadeias de carateres correspondentes a coluna
e a linha de uma posicao e devolve a posicao correspondente.
"""
def cria_posicao(col, lin):
    if type(col) == str and type(lin) == str:
        if col == 'a' or col == 'b' or col == 'c':
            if lin == '1' or lin == '2' or lin == '3':
                return [col, lin]
    raise ValueError('cria_posicao: argumentos invalidos')

"""
Recebe uma posicao e devolve uma copia nova da posicao.
"""
def cria_copia_posicao(pos):
    return [pos[0], pos[1]]

"""
Devolve a componente coluna da posicao dada.
"""
def obter_pos_c(pos):
    return pos[0]

"""
Devolce a componente linha da posicao dada.
"""
def obter_pos_l(pos):
    return pos[1]

"""
Verifica se o argumento e um TAD posicao.
"""
def eh_posicao(arg):
    if type(arg) == list:
        if type(arg[0]) == str and type(arg[1]) == str:
            if arg[0] == 'a' or arg[0] == 'b' or arg[0] == 'c':
                if arg[1] == '1' or arg[1] == '2' or arg[1] == '3':
                    return True
    return False

"""
Verifica se as posicoes sao iguais.
"""
def posicoes_iguais(pos1, pos2):
    return pos1 == pos2

"""
Devolve a cadeia de caracteres que representa o argumento.
"""
def posicao_para_str(pos):
    return '%s%s' % (pos[0], pos[1])

"""
Obtem as colunas adjacentes.
"""
def obter_coluna_adj(col):
    if col == 'a':
        return ['a', 'b']
    elif col == 'b':
        return ['a', 'b', 'c']
    else:
        return ['b', 'c']

"""
Obtem as linhas adjacentes.
"""
def obter_linha_adj(lin):
    if lin == '1':
        return ['1', '2']
    elif lin == '2':
        return ['1', '2', '3']
    else:
        return ['2', '3']

"""
Devolce um tuplo com as posicoes adjacentes a posicao dada.
"""
def obter_posicoes_adjacentes(pos):
    if pos == ['a', '1']:
        return 'b1', 'a2', 'b2'
    elif pos == ['b', '1']:
        return 'a1', 'c1', 'b2'
    elif pos == ['c', '1']:
        return 'b1', 'c2', 'b2'
    elif pos == ['a', '2']:
        return 'a1', 'b2', 'a3'
    elif pos == ['b', '2']:
        return 'a1', 'b1', 'c1', 'a2', 'c2', 'a3', 'b3', 'c3'
    elif pos == ['c', '2']:
        return 'c1', 'b2', 'c3'
    elif pos == ['a', '3']:
        return 'a2', 'b2', 'b3'
    elif pos == ['b', '3']:
        return 'b2', 'a3', 'c3'
    elif pos == ['c', '3']:
        return 'b2', 'c2', 'b3'

"""
TAD PECA
"""

"""
Recebe uma cadeia de caracteres correspondentes ao identificador de um dos
dois jogadores ou uma peca livre e devolve a peca correspondente alem de verificar
a validade dos seus argumentos.
"""
def cria_peca(arg):
    if type(arg) == str:
        if arg == 'X' or arg == 'O' or arg == ' ':
            return arg
    raise ValueError("cria_peca: argumento invalido")

"""
Recebe uma peca e devolve uma copia nova da peca.
"""
def cria_copia_peca(peca):
    return peca

"""
Verifica se o argumento e um TAD peca.
"""
def eh_peca(arg):
    if type(arg) == str:
        if arg == 'X' or arg == 'O' or arg == ' ':
            return True
    return False

"""
Verifica se as pecas sao iguais.
"""
def pecas_iguais(peca1, peca2):
    return peca1 == peca2

"""
Devolve a cadeia de caracteres que representa o jogador dono da peca.
"""
def peca_para_str(peca):
    return '[%s]' % peca

"""
Devolve um inteiro correspondente ao jogador.
"""
def peca_para_inteiro(peca):
    if peca == 'X':
        return 1
    elif peca == 'O':
        return -1
    else:
        return 0

"""
TAD TABULEIRO
"""

"""
Devolve um tabuleiro de jogo do moinho de 3x3 sem posicoes ocupadas por pecas dos jogadores.
"""
def cria_tabuleiro():
    return [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

"""
Recebe um tabuleiro e devolve uma copia nova do tabuleiro.
"""
def cria_copia_tabuleiro(tab):
    return tab

"""
Devolve o inteiro correspondente a coluna
"""
def obter_coluna_int(col):
    if col == 'a':
        return 1
    elif col == 'b':
        return 2
    else:
        return 3

"""
Devolve a peca na posicao dada do tabuleiro.
"""
def obter_peca(tab, pos):
    return tab[(int(pos[1]) - 1)][obter_coluna_int(pos[0]) - 1]

"""
Devolve todas as pecas da linha ou coluna dada.
"""
def obter_vetor(tab, arg):
    vetor = []
    if arg in ['1', '2', '3']:
        return tuple(tab[int(arg) - 1])
    else:
        for e in tab:
            vetor.append(e[obter_coluna_int(arg) - 1])
        return tuple(vetor)

"""
Coloca a peca dada na posicao dada do tabuleiro.
"""
def coloca_peca(tab, jog, pos):
    tab[(int(pos[1]) - 1)][obter_coluna_int(pos[0]) - 1] = jog
    return tab

"""
Remove a peca dada na posicao dada do tabuleiro.
"""
def remove_peca(tab, pos):
    tab[(int(pos[1]) - 1)][obter_coluna_int(pos[0]) - 1] = ' '
    return tab

"""
Move a peca da posicao dada para uma nova.
"""
def move_peca(tab, pos1, pos2):
    peca = tab[(int(pos1[1]) - 1)][obter_coluna_int(pos1[0]) - 1]
    tab[(int(pos2[1]) - 1)][obter_coluna_int(pos2[0]) - 1] = peca
    tab[(int(pos1[1]) - 1)][obter_coluna_int(pos1[0]) - 1] = ' '
    return tab

"""
Verifica se o argumento e um Tad tabuleiro.
"""
def eh_tabuleiro(arg):
    if type(arg) != list or len(arg) != 3:
        return False
    for tup in arg:
        if type(tup) != list or len(tup) != 3:
            return False
        for pos in tup:
            if type(pos) != str:
                return False
            if pos not in [' ', 'X', 'O']:
                return False
    return True

"""
Verifica se a posicao dada e livre.
"""
def eh_posicao_livre(tab, pos):
    return obter_peca(tab, pos) == ' '

"""
Verifica se os tabuleiros sao iguais.
"""
def tabuleiros_iguais(tab1, tab2):
    return tab1 == tab2

"""
Devolve a cadeia de caracteres que representa a linha do tabuleiro.
"""
def linha_para_string(tab, lin):
    pos1 = ['a', lin]
    pos2 = ['b', lin]
    pos3 = ['c', lin]
    return '[%s]-[%s]-[%s]\n' % (obter_peca(tab, pos1), obter_peca(tab, pos2), obter_peca(tab, pos3))

"""
Devolve a cadeia de caracteres que representa o tabuleiro.
"""
def tabuleiro_para_str(tab):
    cadeia = '   a   b   c\n1 '
    cadeia += linha_para_string(tab, '1')
    cadeia += '   | \ | / |\n2 '
    cadeia += linha_para_string(tab, '2')
    cadeia += '   | / | \ |\n3 '
    cadeia += linha_para_string(tab, '3')
    return cadeia[:-1]

"""
Devolve o tabuleiro que e representado pelo tuplo dado.
"""
def tuplo_para_tabuleiro(tuplo):
    tab = []
    for e in tuplo:
        linha_tab = []
        for i in e:
            if i == 1:
                linha_tab.append('X')
            elif i == -1:
                linha_tab.append('O')
            else:
                linha_tab.append(' ')
        tab.append(linha_tab)
    return tab

"""
Devolve a coluna pedida de um tabuleiro.
"""
def obter_coluna(tab, col):
    return tab[0][col - 1], tab[1][col - 1], tab[2][col - 1]

"""
Devolve a linha pedida de um tabuleiro.
"""
def obter_linha(tab, lin):
    return tab[lin - 1]

"""
Devolve a peca do jogador que tenha as suas 3 pecas em linha.
"""
def obter_ganhador(tab):
    for n in range(1, 4):
        if obter_coluna(tab, n) == ('X', 'X', 'X'):
            return 'X'
        elif obter_linha(tab, n) == ('X', 'X', 'X'):
            return 'X'
        elif obter_coluna(tab, n) == ('O', 'O', 'O'):
            return 'O'
        elif obter_linha(tab, n) == ('O', 'O', 'O'):
            return 'O'
    return ' '

"""
Devolve um tuplo com as posicoes de uma dada peca.
"""
def obter_posicoes_pedidas(tab, peca):
    pos_col = ['a', 'b', 'c']
    pos_lin = ['1', '2', '3']
    pos_livres = []
    for col in pos_col:
        for lin in pos_lin:
            pos = [col, lin]
            if obter_peca(tab, pos) == peca:
                pos_livres.append(pos)
    return tuple(pos_livres)

"""
Devolve um tuplo com as posicoes livres
"""
def obter_posicoes_livres(tab):
    return obter_posicoes_pedidas(tab, ' ')

"""
Devolve um tuplo com as posicoes ocupadas pelas pecas de um jogador dado.
"""
def obter_posicoes_jogador(tab, peca):
    return obter_posicoes_pedidas(tab, peca)

"""
FUNCOES ADICIONAIS
"""

"""
Verifica se o jogo se encontra na fase de colocacao.
"""
def fase_colocacao(tab):
    cont = 0
    for linha in tab:
        for pos in linha:
            if pos != ' ':
                cont += 1
    return cont < 6

"""
Recebe um tabuleiro e uma peca de um jogador e devolve um tuplo com uma ou duas
posicoes que representam uma posicao ou um movimento introdizido manualmente pelo jogador 
"""
def obter_movimento_manual(tab, peca):
    if fase_colocacao(tab):
        pos = input('Turno do jogador. Escolha uma posicao: ')
        if eh_posicao_livre(tab, pos):
            return [[pos[0], pos[1]]]
        raise ValueError('obter_movimento_manual: escolha invalida')
    else:
        mov = input('Turno do jogador. Escolha um movimento: ')
        if obter_peca(tab, [mov[0], mov[1]]) == peca and eh_posicao_livre(tab, [mov[2], mov[3]]):
            return [mov[0], mov[1]], [mov[2], mov[3]]
        raise ValueError('obter_movimento_manual: escolha invalida')

"""
Devolve a peca correspondente ao inteiro dado.
"""
def int_para_peca(n):
    if n == 1:
        return 'X'
    elif n == -1:
        return 'O'
    else:
        return ' '

"""
Devolve a peca adversaria a dada.
"""
def obter_peca_adv(peca):
    return int_para_peca(peca_para_inteiro(peca) * (-1))

"""
Verifica se a peca dada ganhou o jogo.
"""
def eh_vitoria(tab, peca, pos):
    new_tab = coloca_peca(tab, peca, pos)
    return obter_ganhador(new_tab) == peca

"""
Devolve uma posicao uqe repreenta uma jogada na fase de colocacao.
"""
def movimento_colocacao_auto(tab, peca):
    pos_livres = obter_posicoes_livres(tab)
    for pos in pos_livres:
        if eh_vitoria(tab, peca, pos):
            tab = remove_peca(tab, pos)
            return [[pos[0], pos[1]]]
        if eh_vitoria(tab, obter_peca_adv(peca), pos):
            tab = remove_peca(tab, pos)
            return [[pos[0], pos[1]]]
        tab = remove_peca(tab, pos)
    if ['b', '2'] in pos_livres:
        return [['b', '2']]
    cantos = [['a', '1'], ['c', '1'], ['a', '3'], ['c', '3']]
    for canto in cantos:
        if canto in pos_livres:
            return [[canto[0], canto[1]]]
    laterais = [['b', '1'], ['a', '2'], ['c', '2'], ['b', '3']]
    for lateral in laterais:
        if lateral in pos_livres:
            return [[lateral[0], lateral[1]]]

"""
Devolve duas posicoes que representam um movimento escolhido automaticamente
usando os criterios da estrategia facil.
"""
def estrategia_facil(tab, peca):
    for pos in obter_posicoes_jogador(tab, peca):
        for pos_adj in obter_posicoes_adjacentes(pos):
            if eh_posicao_livre(tab, pos_adj):
                return [pos, [pos_adj[0], pos_adj[1]]]
    return obter_posicoes_jogador(tab, peca)[0], obter_posicoes_jogador(tab, peca)[0]

"""
Devolve duas posicoes que representam um movimento escolhido automaticamente
usando os criterios da estrategia normal.
"""
def estrategia_normal(tab, peca):
    for pos in obter_posicoes_jogador(tab, peca):
        for pos_adj in obter_posicoes_adjacentes(pos):
            if eh_posicao_livre(tab, pos_adj):
                if eh_vitoria(tab, peca, pos_adj):
                    tab = remove_peca(tab, pos_adj)
                    return [[pos[0], pos[1]], [pos_adj[0], pos_adj[1]]]
                tab = remove_peca(tab, pos_adj)
    return estrategia_facil(tab, peca)

"""
Recebe um tabuleiro, uma peca de um jogador e uma cadeia de caracteres e devolve
um tuplo com umas ou duas posicoes que representam uma posicao ou um movimento
escolhido automaticamente
"""
def obter_movimento_auto(tab, peca, dif):
    if fase_colocacao(tab):
        return movimento_colocacao_auto(tab, peca)
    else:
        if dif == 'facil':
            return estrategia_facil(tab, peca)
        elif dif == 'normal':
            return estrategia_normal(tab, peca)

"""
Funcao principal que permite jogar um jogo completo do jogo do moinho
de um jogador contra o computador.
"""
def moinho(peca, dif):
    if type(peca) != str or type(dif) != str or (peca != '[X]' and peca != '[O]'):
        raise ValueError('moinho: argumentos invalidos')
    if dif != 'facil' and dif != 'normal':
        raise ValueError('moinho: argumentos invalidos')
    tab = cria_tabuleiro()
    print('Bem vindo ao JOGO DO MOINHO. Nivel de dificuldade %s.' % dif)
    print(tabuleiro_para_str(tab))
    if peca == '[X]':
        while obter_ganhador(tab) == ' ':
            jogada_jog = obter_movimento_manual(tab, 'X')
            if len(jogada_jog) == 1:
                tab = coloca_peca(tab, 'X', jogada_jog[0])
            else:
                tab = move_peca(tab, jogada_jog[0], jogada_jog[1])
            print(tabuleiro_para_str(tab))
            if obter_ganhador(tab) != ' ':
                break
            print('Turno do computador (%s)' % dif)
            jogada_cpu = obter_movimento_auto(tab, 'O', dif)
            if len(jogada_cpu) == 1:
                tab = coloca_peca(tab, 'O', jogada_cpu[0])
            else:
                tab = move_peca(tab, jogada_cpu[0], jogada_cpu[1])
            print(tabuleiro_para_str(tab))
    else:
        while obter_ganhador(tab) == ' ':
            jogada_cpu = obter_movimento_auto(tab, 'X', dif)
            if len(jogada_cpu) == 1:
                tab = coloca_peca(tab, 'X', jogada_cpu[0])
            else:
                tab = move_peca(tab, jogada_cpu[0], jogada_cpu[1])
            print(tabuleiro_para_str(tab))
            if obter_ganhador(tab) != ' ':
                break
            jogada_jog = obter_movimento_manual(tab, 'O')
            if len(jogada_jog) == 1:
                tab = coloca_peca(tab, 'O', jogada_jog[0])
            else:
                tab = move_peca(tab, jogada_jog[0], jogada_jog[1])
            print(tabuleiro_para_str(tab))
            print('Turno do computador (%s)' % dif)
    return peca_para_str(obter_ganhador(tab))

