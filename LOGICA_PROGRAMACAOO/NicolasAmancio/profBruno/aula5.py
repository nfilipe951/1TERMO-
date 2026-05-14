# 1, o laço 'for' (repetições Determinadas)
# use o 'for' quando vc sabe exatamente quantas vezes algo deve acontecer (como ler 10 sensores ou processar uma lista de peças).
# exemplo: relatório que produção diaria 
# imagine que vc tem uma meta de produzir 5 lotes e queer numerar cada um:

# exemplo1

# for lote in range (1, 6):
#     print(f"processando lote número {lote}...")
#     print("Qualidade verificada. [ok]")
#     print("produção do dia finalizada!")

# #imagine que vc queira armazenar 10 carros 
# for carros in range(10):
#     print(f"Quantidade de carros{carros}")

# exemplo 2
# contar até 4
# for i in range(5):
#     print(i)

# exemplo 3
# pecas= ["Engrenagem","Eixo","Rolamento","Parafuso"]

# for item in pecas:
    # print(f"Item em estoque:{item}")

# pecas:["engrenagem","eixo","rolamento"," parafusos"]
# maquinas= ["máquina 1", "maquina 2"]

# for item in pecas:
    # print (f"item em estoque: {item}")
    # for maq in maquinas:
        # print(f"Máquinas que temos {maq}")

# exercicio 1 
# 1. contador de produção (for)
# uma estreira processa 10 peças por ciclo. Crie um programa que use um for para contar de 1 a 10 e, para cada número
#imprima: "peça nº X processada com sucesso". No final, exiba :"Ciclo de produção concluido"


# for pecas in range (1,11):
#     print(f"numero de peça: {pecas}")
#     print("peça número {pecas} processada com sucesso")

# print("Ciclo de produção concluído")

# exemplo 2
#Imagine a produção de frutas em uma feira. Desejo apresentar as frutas banana, manga, melancia, abacaxi com uma quantidade de 10 bananas, 5 mangas, 10 melancias e 13 abacaxi. 

# for bananas in range(11):
#     print(f"Quantidade de:\n {bananas} bananas \n")

# for mangas in range (6):
#     print(f"Quantidade de:\n {mangas} mangas \n")

# for melancias in range(11):
#     print(f"Quantidade de:\n {melancias} melancias \n")

# for abacaxi in range(14):
#     print(f"Quantidade de:\n {abacaxi} abacaxi \n")

# resultado= abacaxi+bananas+melancias+abacaxi
# print(f"Quantidade de frutas ao total é:\n", resultado)

# exercios #
#montar uma taboada inicialmente pode ser usado por um valor fixo e depois de usar a pergunta

# print("Bem-vindo a tabuada!")
# valor= int(input("Digite o valor para a realização da tabuada:\n"))
# for numeros in range(1,11):
#     print(f"{valor} x {numeros} =",valor*numeros)

#2. o laço while (repetições Intermediarias)
# Use o while quando vc não sabe quando parar. Ele depende de uma condição (como um sensor de segurança ou um botão  de emergência)
#exemplo: Monitor de temperatura(loop infinito controlado"
#repete enquanto a temperatura estiver segura 
#inicio

# temperatura= 25 
# while temperatura < 40:
#     print(f"Temperatura atual: {temperatura}°C. Sistema operando...")
#     temperatura += 3 #simulando o aquecimento da máquina
#     print("ALERTA! temperatura atingiu o limite, Desligando motor...")
          
# exemplo: menu de interação 
# opcao = ""

# while opcao != "sair" and "SAIR":
#     opcao= input("Digite a leitura do sensor ou 'sair' para fechar:").lower()
#     if opcao != "sair":
#       print(f"Dado ' {opcao}' registrado no banco de bancos.")
# print("Sistema encerrado")
        
# exercicio 4
# criar um menu de opcões com 4 itens ex: escolher series apresente sua escolha de series das outras 3 
# qualquer opção diferente sair do mundo

series=""
while series != "drama" and "romance" and "ação":
   series= input("Digite o gênero da série: \n")
   if series!=  "drama" and "romance" and "ação":
    print(f"Tema ' {series}' registratado")
print ("Escolha feita com sucesso")

