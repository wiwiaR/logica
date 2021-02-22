# Projeto 1 de Lógica

Código do projeto 1 da disciplina de lógica de programação.

O trabalho foi feito em dupla por João José e Vitória Ribeiro em linguagem de programação Python.

## Avisos

* Os choques devem ser separados por espaço (exemplo: 1 2).

* Quando colocar o choque dos cursos, coloque em ordem crescente (exemplo: 2 5).

* Devem ser inseridos apenas dois cursos por choque.

* Os cursos são diferenciados por seus índices (por exemplo, o curso 1 e o curso 4 são cursos diferentes).

* A função IsSatisfatível() verifica se o choque de horários é satisfatível e, se for, ele retorna a lista de cursos alocados, caso contrário, retorna apenas a informação de que não é possível fazer a alocação.

## Código de Satisfatibilidade

* Para Solucionar a satisfabilidade de outras fórmulas, apresente a fórmula como no seguinte exemplo: ([['p', '^', 'q'], 'v', [['s', 'v', 'r'], 'v', ['s', '^', 'p']]])

* Os parenteses são subtituidos por colchetes, pois a hierarquia da formula é respeita com base no colchete

* Além disso, os conectivos basicos em String são : '^'==AND, 'v'==OR, '¬'==NOT, '>'==IMPLIES
