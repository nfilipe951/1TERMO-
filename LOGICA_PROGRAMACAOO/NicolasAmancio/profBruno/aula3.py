# def saudacao(Nicolas):
#       return f"olá, {Nicolas}!"

# mensagem = saudacao("Nicolas")
# print(mensagem)

# # exemplo 2 

# nome = input("Seu nome:")
# idade= int(input("Sua idade:")) #converte texto para inteiro
# print(f"{nome} tem {idade} anos")

# # exercício 1 
# # Cálculo de notas por semetre onde  terá duas notas formativas e uma nota somativa para encerrar 
# # os valores de notas são de 0 a 100 

# print("Bem-vindo ao calculador de notas ")
# nota1= int(input("Digite o valor da primeira nota para o calculo: \n"))
# nota2= int(input("Digite o valor da segunda nota para o calculo: \n"))
# nota3= int(input("Digite o valor da terceira nota para o calculo: \n"))
# total= (nota1 + nota2 + nota3)/3
# print(f"Sua nota final é: \n {total}")

# # exemplo 3

# print("Bem-vindo ao calculador de notas ")
# nota1= int(input("Digite o primeiro valor para o calculo: \n"))
# nota2= int(input("Digite o segundo valor para o calculo: \n"))
# nota3= int(input("Digite o terceiro valor o calculo: \n"))
# total= (nota1 + nota2 + nota3)/3
# print(f"Sua nota do primeiro semestre é: \n {total}")

# nota11= int(input("Digite o primeiro valor para o calculo: \n"))
# nota22= int(input("Digite o segundo valor para o calculo: \n"))
# nota33= int(input("Digite o terceiro valor o calculo: \n"))
# total2= (nota11 + nota22 + nota33)/3
# print(f"Sua nota do segundo semestre é: \n {total2}")
# print(f"Sua nota dos dois semestres é: \n {total} e {total2}")

# print("As médias do semestres são: " , round(total,2) )

# # round serve para arredondar casas decimais 

# # exemplo 3 
# def boas_vindas(nome,cargo):
#       print(f"olá, {nome}! Você é o novo {cargo}")

# boas_vindas("Ana", "Desenvolvedora")
# boas_vindas("Carlos", "Gerente")

# # exemplo 4
# def configurar_conexao(servidor, porta=8080):
#       print(f"Conectando a {servidor} na porta {porta}...")
      
# configurar_conexao("192.168.1.1")
# configurar_conexao("10.0.0.1",3000)
# configurar_conexao("192. 168.1.2")
# configurar_conexao("10.0.0.2",3001)

# exercício 2 

# nome= str(input("Digite seu nome: \n"))
# curso= str(input("Qual o seu curso: \n"))
# idade= int(input("Qual o ano em que nasceu: \n"))
# ano= int(input("Digite o ano atual: \n"))
# idade2= ano - idade
# print("Seu nome é:",{nome})
# print("Seu curso é:",{curso})
# print("Sua idade é:",{idade2})

# # exercício 3

# v1= float(input("Digite o valor da conta: \n"))
# g= int(input("Digite o valor da gorgeta: \n"))
# v2= v1 / g 
# print("valor da gorgeta é: \n",v2)

# exercício 4 

# p1= float(input("Digite o número: \n"))
# resultado1= p1 - 1
# print("O valor do antecessor é: \n",resultado1)
# resultado2= p1 + 1
# print("O valor do sucessor é: \n",resultado2)

# exercício 5
qnt= int(input("Digite a quantidade de livros: \n"))
valorL= float(input("Digite o valor dos livros: \n"))
resul= qnt * valorL /5
print("O valor final de Desconto é:\n",resul)






