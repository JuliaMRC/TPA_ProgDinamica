# Trabalho de Programação -- Programação Dinâmica -- Parte 1

*Autor:* Júlia Miranda R. Campos
*Problema:* 10579	Fibonacci Numbers
## Sobre a Solução
Este diretório contém o código fonte gerado para solucionar o problema 10579	Fibonacci Numbers
do Online Judge. O problema recebeu veredito Accepted, como mostrado na
figura abaixo:
![Veredito](/fibonacci/veredito.PNG)

A programação dinâmica foi usada para poupar que certas contas sejam feitas várias vezes de forma desnecessária no decorrer da execução.
Por exemplo: numa execução comum de Fibonacci para descobrir F(3) precisamos de F(2) e F(1), caso precisamos de F(4) fariamos novamente 
o cálculo para descobrir quem é F(3) e F(2) e assim suscessivamente. Para esse programa, salvamos os valores em questão em um dicionário
e quando necessário buscamos o valor pela key (posição) e descobrimos o value (valor correspondente na sequência de Fibonacci), assim não 
precisamos refazer cálculos.

O programa foi desenvolvido em Python 3. 
