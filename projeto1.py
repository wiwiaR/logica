from formula import And
from formula import Or
from formula import Not
from formula import Atom

vetorIndice = []
vetorIndiceRetirados = []
tabelaVerdade = []  # A tabela deve ser criada fora e antes da função
horario = 1


def retiraChoques(choques, vetorIndiceRetirados, numeroDeChoques):
    c = len(vetorIndiceRetirados)
    i = 0
    k = len(choques)
    while i < k:
        a = int(choques[i][0])
        b = int(choques[i][2])
        for j in range(c):
            if a == vetorIndiceRetirados[j] or b == vetorIndiceRetirados[j]:
                del(choques[i])
                i = i - 1
        i = i + 1
        k = len(choques)
    return choques


def imprimeHorario(formula, horario, choques, numeroDeChoques):

    # Recebe a fórmula (00111) e o horário
    # 01
    j = -1
    for i in range(len(formula)):
        j = j + 1
        if formula[i] == '1':
            print('Curso {0} alocado no horario H{1}'.format(
                vetorIndice[j], horario))
            vetorIndiceRetirados.append(vetorIndice[j])
            del(vetorIndice[j])
            j = j - 1
    if (len(vetorIndice)) == 1:
        horario = horario + 1
        print('Curso {0} alocado no horario H{1}'.format(
            vetorIndice[0], horario))
    else:
        horario = horario + 1
        choques2 = retiraChoques(
            choques, vetorIndiceRetirados, numeroDeChoques)
        numeroDeChoques = len(choques2)
        numeroDeCursos2 = len(vetorIndice)

        formula2 = solucionaFormula(numeroDeCursos2, numeroDeChoques, choques2)
        return imprimeHorario(formula2, horario, choques2, numeroDeChoques)
    return vetorIndice


def solucionaFormula(numeroDeCursos, numeroDeChoques, choques):

    # Retorna a linha que contém maior número de atômicas true (exemplo: 00111)
    if numeroDeChoques == 1:
        matriz = ''
        str(matriz)
        for i in range(numeroDeCursos):
            if int(choques[0][0])-1 == i:
                matriz = matriz + '0'
            else:
                matriz = matriz + '1'
        return matriz

    matrizTabelaVerdade = geraTabelaVerdade(numeroDeCursos, numeroDeCursos)
    tabelaAuxiliar = []
    contador = 0

    for i in range(len(matrizTabelaVerdade)):
        tabelaValor = []
        resultadoLinha = 0
        for j in range(numeroDeChoques):
            p = int(choques[j][0])-1
            q = int(choques[j][2])-1
            aux = rAnd(int(matrizTabelaVerdade[i][p]), int(
                matrizTabelaVerdade[i][q]))
            tabelaValor.append(rNot(aux))

            if j == 1:
                resultadoLinha = rAnd(tabelaValor[j], tabelaValor[j-1])

            if j > 1:
                resultadoLinha = rAnd(tabelaValor[j], resultadoLinha)

            if resultadoLinha == 1 and j == numeroDeChoques-1:
                maximoTrue = 0
                for k in range(numeroDeCursos):
                    maximoTrue = maximoTrue + int(matrizTabelaVerdade[i][k])
                if maximoTrue > contador:
                    contador = maximoTrue
                    tabelaAuxiliar = matrizTabelaVerdade[i]
    return tabelaAuxiliar


def rNot(valor):
    if valor == 0:
        return 1
    else:
        return 0


def rAnd(valor1, valor2):
    if valor1 == 0 or valor2 == 0:
        return 0
    else:
        return 1


# Função para gerar uma tabela verdade (número de variáveis da tabela(fixo), número de variáveis da tabela(recursivo))
def geraTabelaVerdade(m, n):
    bits = 2**m  # determina quantos linhas terá a tabela, valor fixo
    repeticoes_coluna = (bits//(2**n))*2
    repeticoes_linha = (2**n//2)//2
    contador = 0  # Esse contador será sempre incrementado até a quantidade de bits e será zerado quando a função repetir
    if not tabelaVerdade:  # essa condição cria a primeira coluna da tabela
        for i in range(bits // 2):
            tabelaVerdade.append('0')
        for i in range(bits // 2):
            tabelaVerdade.append('1')
    for j in range(repeticoes_coluna):
        for i in range(repeticoes_linha):
            tabelaVerdade[contador] = tabelaVerdade[contador] + '0'
            contador += 1
        for i in range(repeticoes_linha):
            tabelaVerdade[contador] = tabelaVerdade[contador] + '1'
            contador += 1
    if n == 1:
        return tabelaVerdade
    else:
        return geraTabelaVerdade(m, n-1)


def criarFormula(choques):
    formula = []
    for i in range(numeroDeChoques):
        formula.append(
            str(Not(And(Atom('' + choques[i][0]), Atom('' + choques[i][2])))))
    for j in range(len(formula)-1):
        formula[j+1] = str(And(formula[j], formula[j+1]))
        formula[j] = ''
    formula = ''.join(formula)
    return formula


# --- Entradas --- #

numeroDeCursos = int(input("Entre com o número de cursos: "))
numeroDeHorarios = int(
    input('Entre com o número de Horarios a serem organizados: '))
numeroDeChoques = int(
    input('Entre com o número de choques a serem organizados: '))
choques = [str(input("Entre com os choques de cursos por alunos com base na ordem apresentada na forma Exemplo(1 2): "))
           for i in range(numeroDeChoques)]

# --- Saídas --- #

for i in range(numeroDeCursos):
    vetorIndice.append(i+1)

formula1 = criarFormula(choques)
formula = solucionaFormula(numeroDeCursos, numeroDeChoques, choques)
imprimeHorario(formula, horario, choques, numeroDeChoques)
