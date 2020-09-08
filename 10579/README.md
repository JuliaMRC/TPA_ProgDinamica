# Trabalho de Programação -- Programação Dinâmica -- Parte 1

*Autor:* Júlia Miranda R. Campos
*Problema:* 10579	Fibonacci Numbers
## Sobre a Solução
Este diretório contém o código fonte gerado para solucionar o problema 10579	Fibonacci Numbers
do Online Judge. O problema recebeu veredito Accepted, como mostrado na
figura abaixo:
![Veredito](/10579/10579-veredito.PNG)

A programação dinâmica foi usada para poupar que certas contas sejam feitas várias vezes de forma desnecessária no decorrer da execução.
Numa execução comum de Fibonacci para descobrir F(3) precisamos calcular F(2) e F(1), caso precisamos de F(4) faríamos novamente o cálculo, 
com recorrências, de F(3), gerando um efeito cascata. Para esse programa, salvamos os valores em questão em um dicionário
e quando necessário buscamos o valor pela key (posição) e descobrimos o value (valor correspondente na sequência de Fibonacci), assim não 
precisamos refazer cálculos.

O programa foi desenvolvido em Python 3. 
