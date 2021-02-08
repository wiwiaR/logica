from formula import And
from formula import Not
from formula import Atom


vetorIndice = []
vetorIndiceRetirados = []
vetorCorrespondencia = []
tabelaVerdade = []  # A tabela deve ser criada fora e antes da função
horario = 1
final = ''


def limpaTabela(tabelaVerdade):
    for i in range(len(tabelaVerdade)):
        del(tabelaVerdade[-1])
    return tabelaVerdade


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


def verificaHorario(horario, numeroDeHorarios, final):
    if horario > numeroDeHorarios:
        print('Não é possivel alocar todos os cursos')
    else:
        print(final)
        print('Todos os cursos foram alocados')


def imprimeHorario(formula, horario, choques, numeroDeChoques, final):
    # RECEBE FORMULA (00111) E O HORARIO 0 A PRIORI
    # 01
    j = -1
    for i in range(len(formula)):
        j = j + 1
        if formula[i] == '1':
            final = final + ('Curso {0} alocado no horario H{1}\n'.format(
                vetorIndice[j], horario))
            vetorIndiceRetirados.append(vetorIndice[j])
            del(vetorIndice[j])
            j = j - 1
    if (len(vetorIndice)) == 1:
        horario = horario + 1
        final = final + ('Curso {0} alocado no horario H{1}\n'.format(
            vetorIndice[0], horario))
    else:
        horario = horario + 1
        choques2 = retiraChoques(
            choques, vetorIndiceRetirados, numeroDeChoques)
        numeroDeChoques2 = len(choques2)
        numeroDeCursos2 = len(vetorIndice)
        limpaTabela(tabelaVerdade)
        formula2 = solucionaFormula(vetorIndice, choques2)
        return imprimeHorario(formula2, horario, choques2, numeroDeChoques, final)
    return verificaHorario(horario, numeroDeHorarios, final)


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


def rOr(valor1, valor2):
    if valor1 == 1 or valor2 == 1:
        return 1
    else:
        return 0


def rImplies(esquerda, direita):
    if esquerda == 1 and direita == 0:
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


def solucionaFormula(vetorIndiceA, choquesA):
    resultado = 0
    a = len(vetorIndiceA)
    matrizTabelaVerdade = geraTabelaVerdade(a, a)
    linhaSatisfativel = []
    for i in range(len(matrizTabelaVerdade)):  # 0-15
        resultadoAnterior = 1
        for k in range(a):  # 0-3
            for j in range(len(choquesA)):
                p = int(choquesA[j][0])
                if p == vetorIndiceA[k]:
                    q = int(choquesA[j][2])
                    l = k
                    while l < a:
                        if q == vetorIndiceA[l]:
                            resultado = rAnd(int(matrizTabelaVerdade[i][k]), int(
                                matrizTabelaVerdade[i][l]))
                            resultado = rNot(resultado)*resultadoAnterior
                            resultadoAnterior = resultado
                            if resultado == 1 and j == len(choquesA)-1:
                                linhaSatisfativel = matrizTabelaVerdade[i]
                        l = l+1
    return linhaSatisfativel


numeroDeCursos = int(
    input('Entre com o número de cursos a serem organizados: '))
numeroDeHorarios = int(
    input('Entre com o número de Horarios a serem organizados: '))
numeroDeChoques = int(
    input('Entre com o número de choques a serem organizados: '))
choques = [str(input("Entre com os choques de cursos por alunos com base na ordem apresentada na forma Exemplo(1 2): "))
           for i in range(numeroDeChoques)]
numeroDeCursos = 5


for i in range(numeroDeCursos):
    vetorIndice.append(i+1)
    vetorCorrespondencia.append(i+1)


formula = solucionaFormula(vetorIndice, choques)
imprimeHorario(formula, horario, choques, numeroDeChoques, final)
