
tabelaVerdade = []


def criarformula(choques):
    formula = []
    formulaAux = []

    formula = ['¬', [choques[0][0], '^', choques[0][1]]]
    if len(choques) == 1:
        return formula
    else:
        i = 1
        while i < len(choques):
            formulaAux = ['¬', [choques[i][0], '^', choques[i][1]]]
            formula = [formulaAux, '^', formula]
            i += 1
        return formula


def valorVerdadeBemEspecifico(formula, truth):
    x = valor_verdade(formula, truth)
    return x


def valor_verdade(phi, verdade):
    if len(phi) == 1:
        return verdade[phi]
    if phi[0] == '¬':
        return not valor_verdade(phi[1], verdade)
    if type(phi[1]) == str:
        if phi[1] == '^':
            return valor_verdade(phi[0], verdade) and valor_verdade(phi[2], verdade)
        if phi[1] == 'v':
            return valor_verdade(phi[0], verdade) or valor_verdade(phi[2], verdade)
        if phi[1] == '>':
            if valor_verdade(phi[0], verdade) == True and valor_verdade(phi[2], verdade) == False:
                return False
            else:
                return True


# Função para gerar uma tabela verdade (número de variáveis da tabela(fixo), número de variáveis da tabela(recursivo))
def geraTabelaVerdade(m, n):
    bits = 2**m  # determina quantos linhas terá a tabela, valor fixo
    repeticoes_coluna = (bits//(2**n))*2
    repeticoes_linha = (2**n//2)//2
    contador = 0  # Esse contador será sempre incrementado até a quantidade de bits e será zerado quando a função repetir
    if not tabelaVerdade:  # essa condição cria a primeira coluna da tabela
        for i in range(bits // 2):
            tabelaVerdade.append('0')
            i += 1
        for i in range(bits // 2):
            tabelaVerdade.append('1')
    for j in range(repeticoes_coluna):
        for i in range(repeticoes_linha):
            tabelaVerdade[contador] = tabelaVerdade[contador] + '0'
            contador += 1
        for i in range(repeticoes_linha):
            tabelaVerdade[contador] = tabelaVerdade[contador] + '1'
            contador += 1
        j += 1
    if n == 1:
        return tabelaVerdade
    else:
        return geraTabelaVerdade(m, n-1)


def makeTruth(numeroDeAtomicas):
    tabelaAux = geraTabelaVerdade(numeroDeAtomicas, numeroDeAtomicas)
    indice = {}
    auxIndice = []
    dicionario = []
    for j in range(len(tabelaAux)):
        for k in range(numeroDeAtomicas):
            if tabelaAux[j][k] == '0':
                auxIndice = ({str(k+1): False})
                indice = {**indice, **auxIndice}
            else:
                auxIndice = ({str(k+1): True})
                indice = {**indice, **auxIndice}
            if k == numeroDeAtomicas-1:
                dicionario.append(indice)
    return dicionario


def satisfativel(numeroAtomicas, formula):
    contadorInsatisfativel = 0
    interpretacoes = makeTruth(numeroAtomicas)
    for i in range(len(interpretacoes)):
        y = valorVerdadeBemEspecifico(formula, interpretacoes[i])
        if y == True:
            print('A interpretacao é satisfatível >>>', interpretacoes[i])
            contadorInsatisfativel = contadorInsatisfativel + 1
    if contadorInsatisfativel == 0:
        print('a formula não possui interpretacao que satisfaca, logo e insatisfativel')
    return


numeroAtomicas = 2
choques = []

formula = [['1', '^', '2'], '^', ['¬', '2']]

if len(choques) == 0:
    satisfativel(numeroAtomicas, formula)
else:
    satisfativel(numeroAtomicas, criarformula(choques))
