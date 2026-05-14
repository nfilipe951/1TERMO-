#Explicação de def: A palavra-chave "def" é usadaa para definir uma função em python. Uma função é um bloco de código reutilizavel que realiza uma tarefa específica 
#return: A palavra-chave "return" é usada para finalizar a execução de uma função e retornar um valor para o local onde a função foi chamada. O valor retornado pode ser usado posteriormente no código.

# def nome ():
#     nome = input("Digite seu nome: \n")
#     return nome 
# print(f"Olá, {nome()}!")

# def valores():
#     print("Digite três valores:")
#     a = int(input("Digite o primeiro valor: \n"))
#     b = int(input("Digite o segundo valor: \n"))
#     c= int(input("Digite o terceiro valor: \n"))
#     return a, b, c

# print(f"O maior valor é: {max(valores())}")

# # reutilizando funções

# nome()
# valores()

# Conceitos chave
# def: Indica o inicio da definição da função
# nome: Identifica a função para você chamá-la depois
# parâmetros: Dados que a função recebe (opcional)
# return: Envia o resultado de volta para quem chamou a função (opcional)

# def calcular_dobro(numero):
#     return numero * 2
# # como usar: resultado = calcular_dobro(5)
# print(calcular_dobro(5))


# Projeto

# 1= "nr-10"
# 2= "nr-35" 
# 3= "brigada" 

# E= "Elétrica"
# M= "mecânica"
# T= "T.i"
# ADM= "Adiministração" 
# MNT= "Manutenção"  
# TA= "Trabalho em Altura"



def cadastro():

    nome = input(" >>> Digite seu nome completo: \n ")
    setor = input(" >>> Digite o setor em que irá (E= Elétrica // M= mecânica // T= T.i // ADM= Adiministração // MNT= Manutenção // TA= Trabalho em Altura): \n" )
    status = input(" >>> Digite a opção em que deseja (1 para NR-10 // 2 para NR-35 // 3 para brigada): \n")

    if setor == "E" or  setor == "M":
     print(f">>> ATENÇÃO - utilizar luvas de alta tensão e botas dielétricas")
    else:
       print("Tenha zelo pelo o que utilizar. Bom trabalho! ")
print(cadastro())
    


def brigada():
   ano= int("Digite o ano em que estamos: \n")
   