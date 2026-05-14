# if: "se" a condição for verdadeira
# elif: "senão, se" (usado para múltiplas condições)
# else: "senão" (executa se nenhuma das anteriores for verdadeira)

# print ("expressões logicas")
# idade= int(input("Sigite sua idade"))

# if idade>=18: 
#  print("você é maior de idade")
#  print("pode tirar carta de motorista")
# elif idade>=16:
#  print("voê ainda não é maior, mas pode votar")
# else:
#  print("você é menor de idade")

#  ex:2
# print("Escolha sua modalidade")
# print("Opção 1: TI")
# print("Opção 2: Humanas")
# print("Opção 1: Exatas")
# modalidade= int(input("Digite sua opção de modalidade por números"))
# if modalidade == 1:
#  print("Você escolheu TI")
# elif modalidade == 2:
#  print("Você escolheu humanas")
# else:
#  print("Você escolheu exatas")

# # ex:3
# print("Categorias de Series e filmes")
# print("Escolha uma categoria")
# print("Séries = S")
# print("Filmes = F")
# categoria= input("Categoria")
# if categoria == "S":
#  print("Sua escolha foi para Séries")
# elif categoria=="F":
#  print("Sua escolha foi filmes")
# else:
#  print("Sua escolha não foi nenhuma das alternativas")

# # ex:4

# print("Calculadora com condições")
# print("Escolha como que calcular")
# print("1= soma")
# print("2= subtração")
# print("3= Multiplicação")
# print("4= divisão")
# calculadora= float(input("Digite sua opção para calcular \n"))
# if calculadora ==1:
#  print("1 = Você escolheu sua soma")
#  soma1= int(input("Digite o primeiro valor \n"))
#  soma2= int(input("Digite o segundo valor \n"))
#  print(soma1+soma2)
# elif calculadora ==2:
#     print("2 = Você escolheu subtração")
#     sub1= int(input("Digite o primeiro valor \n"))
#     sub2= int(input("Digite o segundo valor \n"))
#     print(sub1-sub2)

# elif calculadora ==3:
#     mult1= int(input("Digite o primeiro valor \n"))
#     mult2= int(input("Digite o segundo valor \n"))
#     print("3 = Você escolheu multiplicação")
#     print(mult1*mult2)

# elif calculadora ==4:
#     print("4 = Você escolhe divisão")
#     div1= int(input("Digite o primeiro valor \n"))
#     div2= int(input("Digite o segundo valor \n"))
#     print(div1/div2)

# else:
#   print("Você não escolheu nenhuma opção")
#   print("Sair do programa")

# # exerc:1

# #  criar um algoritimo para calcular a média e com base em notas, podem inserir duas notas e apresente a médida porém a nota base de 50 é aprovado e menor que esse valor será reprovado

# print("Bem vindo a calculadora da sua média")
# nota1= int(input("Digite a primeira nota"))
# nota2= int(input("Digite o segundo valor"))
# resul= (nota1-nota2)

# if resul >= 50:
#    print(" aprovado")

# else:
#   print("Reprovado")

# criar um algoritimo para demonstrar a sinalização de um semafaro 
print("vermelho=1")
print("amarelo=2") 
print("verde=3")
vermelho=1
amarelo=2
verde=3
cores= int(input("qual cor você deseja?"))

if cores ==3:
   print("verde")
elif cores ==1:
   print("vermelho")
elif cores ==2:
   print("amarelo")
else:
    print("Somente essas cores!!")

# # exerc:3
# # criar um algoritimo para aplicação de descontos para produtos como sapatos aplicar 10 por cento, para produtos como roupas 5 por cento e perfumes 2 por cento 

print("escolha o produto:")
print("sapato=1")
print("roupa=2")
print("perfume=3")
escolha=  int(input("Digite o número do produto:"))
# sapato=1
# roupa=2
# perfume=3

if escolha ==1:
    qtd = int(input("Digite a quantidade do produto: \n"))
    valor = float(input("Digite o valor do produto: \n"))
    resultado= qtd * valor/ 10
    print("O valor final de Desconto é:\n",resultado)
 
elif escolha ==2:
    qtd = int(input("Digite a quantidade do produto: \n"))
    valor = float(input("Digite o valor do produto: \n"))
    resultado= qtd * valor/ 5
    print("O valor final de Desconto é:\n",resultado)
elif escolha ==3:
    qtd = int(input("Digite a quantidade do produto: \n"))
    valor = float(input("Digite o valor do produto: \n"))
    resultado= qtd * valor/ 2
    print("O valor final de Desconto é:\n",resultado)
else:
    print("número não identificado no sistema")

# exerc:4
#  criar um algoritimo para calcular a média e com base em notas, podemos inserir duas notas e apresente a média porém a nota 0 e 100 para ser aprovado será acima de 70 e menor que 50 esse valor será reprovado porem vamos acrescentar uma nova condição entre 50 e 70 recuperação

print("Bem-vindo a calculadora de média")
nota1= int(input("Digite a primeira nota: \n"))
nota2= int(input("Digite a segunda nota: \n"))
resultado= (nota1+nota2)/2
if resultado >=70:
   print("aprovado")
elif resultado >= 50:
    print("Recuperação")
else:
    print("Resultado")



