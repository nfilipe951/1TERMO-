# funções 

a=1 #a é uma variável
b=2
c=a+b
print('O valor de A e B é: ',c)

# Variáveis são formas de armazenar informações

# função input
# irá permitir inserir informações
input("Qual é o seu nome?")

# Operadores Matemáticos
# + = soma
# - = subtração
# * = multiplicação
# / = divisão 

# Exemplo 1
# \n quebra a linha
v1 = input("Digite o primeiro valor: \n")
v2 = input("Digite o segundo valor: \n")
vtotal = v1 + v2
print("Qual é o resultado?",vtotal)

# int = valores inteiros Ex: 1, -5
# float = valores com casas decimais Ex; 10.2 , -10.1

# Exemplo 2
x1 = int(input('Digite o primeiro da subtração: \n'))
x2 = int(input('Digite o segundo da subtração: \n '))
xtotal = x1 - x2 
print ("qual é o valor do x \n", xtotal)

# Exemplo 3 e 4 :
# Multiplicar e Dividir 
g1= int(input('Digite o primeiro valor da multiplicação: \n'))
g2 = int(input('Digite o segundo valor da multiplicação: \n '))
gtotal = g1 * g2 
print ("qual é o valor do x \n", gtotal)

s1= int(input('Digite o primeiro da divisão: \n'))
s2 = int(input('Digite o segundo da divisão: \n '))
stotal = s1 / s2 
print ("qual é o valor do x \n",int (stotal))

print("Vamos dividor \n")
d1 = float(input("Digite o primeiro valor desejado \n"))
d2 = float (input("Digite o segundo valor desejado \n"))
dtotal = d1 / d2 
print("Sua divisão é \n", dtotal) 

# concatenar
print('Eu gosto de programar \n + \n Python \n')

# O programa deve permitir que você digite o nome, seu curso e sua idade e também seu hobby

nome= input("Qual é o seu nome? \n")
curso = (input("Qual é o seu curso? \n"))
idade = int(input("Qual é a sua idade? \n"))
hobby = (input("Qual é o seu hobby? \n"))

print("As informações são: \n", "Seu nome é? \n", nome +" \n" "Qual é o seu curso? \n", curso + " \n" "Qual é o seu hobby? \n ", hobby + " \n")

print("Qual é o seu nome?", nome )
print("Qual é o seu curso?", curso)
print("Qual é sua idade?", idade)
print("Qual é seu hobby?", hobby)

# exercício 2 :
# Calculadora dde IMC (Potência e divisão)
# O índice de massa corporal (IMC) é calculado dividindo o peso pela altura ao quadrado ()

print("Bem-vindo a nossa calculadora de IMC")

peso1=float (input("Digite o valor para a realização da divisão:"))
peso2= float (input("Digite o segundo valor para a realização da divisão:"))
Ptotal= peso1 / (peso2 * peso2)

print("O valor do seu IMC é: \n", Ptotal)

# exercício 3
# calculadora completa com os quatros operadores matemáticos
print('bem-vindo a nossa calculadora')

n1= float (input("Digite o primeiro número"))
n2= float (input("Digite o segundo número"))
adição= n1 = n2 
subtração= n1 - n2 
multiplicação= n1 * n2 
divisão= n1 / n2 
print ("Resultado da adição:", str(adição))
print ("Resultado da subtração:", str (subtração))
print ("Resultado da multiplicação:",str(multiplicação))
print ("Resultado da divisão:", str(divisão))

# Logica da calculadora do professor
print("calculadora")
n1= float(input("Digite o valor \n"))
n2= float(input("Digite o outro valor"))
print("A soma é \n", n1 + n2) 
print ("A subtração é \n,", n1 - n2 )

# Exercício 4
# mercado do brunão
# O mercado deve registrar venda de itens e um relatório de cupom fiscal no fim da compra

print("Bem-vindo ao mercado do brunão")
print("iniciar compra \n")
produto= input("Digite o produto: \n")
valor= float (input("Digite o valor do produto"))
qtde= float(input("Digite a quantidade \n"))
total= valor * qtde
print ("Sua compra foi \n", total)
print("cupom fiscal do Mercado do Senai")
print("O produto comprado foi", produto)
print("O valor foi", valor)
print("E a quantidade comprada foi",qtde)

# Exercício 5
# uma tabuada

print("Bem-vindo a calculadora")
n11= float(input("Digite o primeiro número" ))
n22= float (input("Digie o segundo número para a resolução da tabuada"))
resultado= n11 * n22 
print("O resultado é:",resultado)








