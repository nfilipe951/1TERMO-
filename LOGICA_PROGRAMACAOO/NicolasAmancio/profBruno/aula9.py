# tratamendo de erros com python
# erro comuns:
# -ZeroDivisionError: divisão por Zero
# -ValueError: conversão de tipo inválida
# -IntexError: acesso a índice fora do limite
# -keyError: acesso a chave inexistente em dicionário

# Exemplo de tratamento de erros
# print("Exemplo de tratamento de erros")
# try:
#    num1= int(input("Digite o primeiro número...")) 
#    num2= int(input("Digite o segundo número..."))
#    resultado= num1/num2
#    print(f"O resultado da divisão é: {resultado:.2f}")

# # except ZeroDivisorError:
# # print("Erro: Não é possivel dividir por zero.")

# # except ValueError:
# # print("Erro: entrada inválida. Por favor, Digite um número inteiro.")
# except NameError:
#    print("Erro: Variável não definida.")

# except Exception as e:
#     print(f"Ocorreu um erro inesperado: {e}")

# if num1 > 100:
#      print("O número difitado é maior que 100")
#      for i in range(1, 6):
#        print(f"{num1} x {i} = {num1 * 1}")
#        if num1 * i > 1000:
#          print(" O resultado da multiplicação é maior que 1000.")
#          try:
#            pass 
#          except Exception as e :
#            print(f"Ocorreu um erro inesperado: {e}")

# else:
#     print("O número digitado é menor ou iguala 100.")


# exerecicio 1
# escreva um programa que solicite ao usuário um número inteiro e calcule a média de uma lista números. O programa deve tratar os seguinteserros:
# valorError: se o usuário digitar um valor que não seja um número inteiro

# try:
#    n1= int(input("Digite o primeiro valor: \n"))
#    n2= int(input("Digite o segundo número: \n"))
#    calculo=(n1+n2)/2
#    print(f"O resultado da divisão é: {calculo}")
# except ValueError:
#    print("Erro: você digitou algo errado")

# for i in range(1,2):
#    print(f"{n1} x {i} = {n1 * i}")
#    numero= float(input("Digite um valor"))

# except NameError:
# print("Erro:variael não definida")

# exercicio 2
# escreva um programa que solicite ao usuário uma lista de palavras e conte quantas vezes cada palavra aparece na lista. O programa deve tratar os seguintes erros:
# -ValueError: se o usuário digitar um valor que não seja uma string

# try:
   

# palavra= str(input("Digite palavra para a realização da lista: \n"))
#    texto = "palavra"
#    print(texto.strip().count("palavra")) 
# except ValueError:
#    print("Erro: Palavras não identifica")


# modelo do professor
# try:
#    palavras= input("Digite uma lista de palavras separadas por espaço...").slipt()
#    contagem = {}
#    for palavra in palavras:
#       if palavra in contagem:
#          contagem [palavra] += 1
#       else:
#          contagem[palavra] = 1
#     print("Contagem de palavras:")
#     for palavra, contagem in contagem.items():
#     print(f"{palavra}: {contagem}")
# except ValueError:
#       print("Erro: Entrada inválida. Por favor, digite uma lista de palavras separadas por espaço")

# exerecicio 3
# escrever um programa mais simples com teste de tratamento de erros, como por exemplo, solicitar ao usuário um númeero. O programa deve tratar os seguintes erros:
# -ValueError: se o usuário digitar um valor que não seja um número
# -eroDivisionError: se o usuário digitar zero como divisor

try:
   nun= int(input("Digite um número: \n"))
   print("O numéro é", nun)
except ValueError:
   print(f"Erro: não foi identificado um número")
except ZeroDivisionError:
   print(f"Erro: não foi identificado o número",nun)
