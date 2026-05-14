# for i in range(1,11):
#     print (f"\nTabuada do {i}:")
#     for j in range (1,11):
#         print(f"{i} x {j}= {i*j}")
        
# # Listas de temperaturas lidas pelo sensor por minuto
# leituras= [70, 75, 82, 98, 110, 80]

# for temp in leituras:
#     if temp > 100:
#         print(f"CRÍTICO: {temp}°C detectado! Acionado parada de emergência.")
#         break #o loop para aqui e Não lê os próximos valores (85 e 80)
#     print(f" Temperatura está em {temp}°C. Operação normal.")

# print("Sistema desligado. Aguardando manutenção.")

# materiais= ["metal", "metal", "plastico", "metal", "vidro", "metal"]
# for pecas in materiais:
#     if pecas!= "metal":
#         print(f"Aviso: peça de {pecas} detectada. Desviado para descarte...")
#         continue #pula o restaurante do código abaixo e vai para a proxima peça 

#     #este código só roda se a peça for de metal
#     print (f"Processando peça de {pecas}. Furando e polindo...")
# print("Fim do lote de produção")

#ex 1 
#tente criar um codigo que conte de 1 a 10, mas use o continue para não imprimir o número 5 ( simulandp uma falha de sensor específico no item 5)


# for numeros in range (1,10):
#     if numeros == 5:
#      continue
#     print(f"falha no sensor do item {numeros}")

# ex2
#simule um semafaro com parada para cada cor. Determine um tempo que deseja para que quando mudar para tal cor ele represente uma pausa
 
# from time import sleep 
# print("vermelho=1")
# print("amarelo=2") 
# print("verde=3")
# vermelho=1
# amarelo=2
# verde=3
# cores= int(input("qual cor você deseja?"))
# for i in range(1,6):
#  if cores ==3:
#    print("verde")
#    sleep(1)
# for i in range(1,6):
#  if cores ==1:
#    print("vermelho")
#    sleep(1)
# for i in range (1,6):
#  if cores ==2:
#    print("amarelo")
#    sleep(1)
# else:
#     print("Somente essas cores!!")

# ex4 soma de cargas de energia (for)
#uma fábrica tem 5 máquinas. Peça ao usuario (via input dentro do loop) o consumo em kwh de cada uma das 5 máquinas. Ao final do loop, o programa deve exibir o consumo total da fábrica.
 
# total=0
# for i in range(1,6):
#   consumo= float(input(f"Digite o valor do consumo das {i} maquinas: \n "))
#   total += consumo
# print("O valor final do consumo das máquinas é:", {total})

# ex5 Identificador de peças com defeitos (for+if)
# percorra uma lista de medidas de peças: 
#medidas= [50.1, 49.8, 52.0, 48.5]
# o padrão de qualidade aceita apenas peças com exatamente 50.0 ou mais 
# use um for para ler a lista e, para cada peça, diga se ela está aprovada ou rejeitada

# medida= [50.1,49.8, 52.0, 48.5]
# for i  in medida:
#     if i > 50.0:
#         print(f"{i} peça aprovada")

#     elif i < 50.0:
#         print(f"{i} peça reprovada")

#     else:
#         print("sistema encerrado")

# ex6:
#uma balança industrial está pesando um lote de 6 sacos de insumos. O peso ideal de cada saco é 50kg, mas o sistema aceita variações

# pesos=[50.1,50.2, 49.0,49.0]
# print(pesos)
# for i in range(4):
#     if pesos[i] >= 50:
#         print("Saco", i+1, "- peso ideal")
#     else:
#         print("Saco", i+1, "- peso com alteração")

# peso= float(input("Digite o peso: \n"))
# for i in range (6):
#     if peso > 50.0:
#         print(f"{peso} dentro do padrão")

#     elif peso < 50.0:
#         print(F"{peso} fora do padrão")

# ex7 sistema inteligente de manutenção 
#crie um programa que receba dois dados: a pressão atual(float) e as horas de uso de aculadas (int) de uma turbina
#o programa deve classificar o estado da máquina seguindo esta hierarquia:
#crítico (propriedade 1): se a pressão for maior que 100 ou as horas de uso forem que 10.000
# mensagem: "parada imediata: risco de falha catastrofica "
# alerta( prioridade 2): se a presssão estiver entre 80 e 100 (inclusive)
# mensagem:"Manutenção agendada: pressão acima do ideal"
# monitoramento:(prioridade 3): se as horas do uso forem entre 8.000 e 10.000
# mensagem: "aviso": maquina aproximando da revisão de 10k horas
# normal: para qualquer outro caso que não se encaixe nos acima 
# mensagem: "sistema operal": todos os parâmetros dentro da normalidade


