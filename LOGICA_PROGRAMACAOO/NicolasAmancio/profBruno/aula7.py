# correção
1
# print("registo de operador")
# operador= input("Digite seu nome...")
# turno= input("Digite seu turno...")
# print(f"operador {operador} registrado no turno {turno}. Boa jornada!")

2
# print("Cálculo de Produção")
# produção-hora= int(input("Digite a quantidade de peças produzidas em 1 hora... \n"))
# produção-turno= produção-hora*8

# print(f"Quantidade de peças produzidas em um turno de 8 horas: {produção-turno}")

3
# print("Conversor de unidade")
# pressaobar= float(input("Digite a pressão de bar..\n"))
# pressaopsi= pressaobar * 14.5
# print(f"Pressão em PSI: {pressaopsi:.2f}")
# print(f"Pressão em PSI: {pressaopsi}", round(pressaopsi, 2))

4
# print("Inspeção de Peças")
# nota1= float(input("Digite a nota da inspeção 1 (0 a 10)..."))
# nota2= float(input("Digite a nota da inspeção 2 (0 a 10)..."))
# nota3= float(input("Digite a nota da inspeção 3 (0 a 10)..."))
# média= (nota1+ nota2 + nota3)/3
# print(f"Média de qualidade de peça: {média:.2f}")
# print(f"Média de qualidade da peça: ", round(média,2))

5.1
# print("termostrato Inteligente")
# temperatura= float(input("Digite a temperatura do motor em °C...\n"))
# if temperatura < 40:
#     print("Baixa carga")
# elif 40 <= temperatura <= 70:
#     print("Normal")
# else:
#     print("ALERTA: Resfriamento ativado!")


5.2
# print("Termostrato Inteligente - Versão 2")
# temperatura= float(input("Digite a temperatura do motor em °C...\n"))
# if temperatura < 40:
#     print("Baixa carga")
# elif temperatura >= 70:
#     print("ALERTA: Resfriamento ativado!")
# else:
#     print("Normal")


6.1
# print("Classificador de Loter")
# codigoproduto= input("Digite o código do produto... \n")
# if codigoproduto == "A":
#     print("Alimento")
# elif codigoproduto ("E"):
#     print("Eletrônicos")
# else:
#     print("Desconhecido")

6.2
# print("Classificador de Loter")
# codigoproduto= input("Digite o código do produto... \n")
# if codigoproduto.startswith ("A"):
#     print("Alimento")
# elif codigoproduto.startswith ("E"):
#     print("Eletrônicos")
# else:
#     print("Desconhecido")

7
# print("Segurança de Operação")
# sensorporta= input("Digite o status do botão de emergência (ligado/desligado)...\n")
# botaoemergencia= input("Digite o status do botão de emergência (ligado/desligado)...\n")
# if sensorporta == "fechada" and botaoemergencia == "deligado":
#     print("A máquina pode iniciar.")
# else:
#     print("A máquina não pode iniciar.")

8
# print("Cálculo de Descarte")
# totalpecas= int(input("Digite o total de peças produzidas... \n "))
# totaldef= int(input("Digite o total de peças defeituosas... \n"))
# despercent= (totaldef/ totalpecas)*100
# if despercent > 5:
#     print("Revisar Processo")
# else:
#     print("Processo Otimizado")
# print(f"Descarte percentual: {despercent:.2f}%")

9
# print("Vlidação da Média")
# media= float(input("Digite a media da peça em mm ...\n"))
# if media > 9.8:
#     print("A peça está abaixo da tolerância.")
# elif media > 10.2:
#     print("A peça está acima da tolerância")
# else:
#     print("A peça está dentro da tolêrancia")

10
# print("Contagem regressiva de setup")
# for contagem in range(10, 0, -1):
#     print(contagem)
# print("Prensa ativada!")

11
# print("Soma de produção (Acumulador):")
# pesototal = 0
# while True:
#     pesocaixa= float(input("Digite o peso da caixa (0 para parar)...\n"))
# if pesocaixa ==0:
#     break
# pesototal += pesocaixa
# print(f"Peso total acumulado:{pesototal:.2f} kg")

12
# print("Multiplas leituras")
# temperaturas:[]
# for i in range(1, 6):
#     temp= float(input(F"Digite a temperatura do sensor {i} em °C..."))
# temperaturas.append(temp)

# print(f"Maior temperatura lida: {max(temperaturas):.2f} °C")

# print(f"Maior temperatura lida: {max(temperaturas):.2f}°C")
# print(f"Menor temperatura lida: {min(temperaturas):.2f} °C")
# print(f"Soma temperatura lida: {sum(temperaturas):.2f} °C")

13
# print("painel de login")
# senhacorreta= "admin123"
# tentativa=3
# while tentativa > 0 :
#     senha=input("Digite a senha do supervisor...")
#     if senha == senhacorreta:
#         print("Acesso Permitida")
#         break
# else:
#     tentativa -=1
#     print(f"Acesso negado. Tentativas restantes:{tentativa}")
#     if tentativa==0:
#         print("Painel Bloqueado")

14
# print("Simulador de estoque")
# estoque = 100
# while True:
#     print("\nMenu":)
#     print("1. Adicionar itens")
#     print("2. Remover itens")
#     print("3. Sair")
#     escolha= input("Escolha uma opção (1, 2 ou 3)...")

#     if escolha ==1:
#         quantidade = int(input("Digite a quantidade de itens a adicionar..."))
#         estoque+= quantidade
#         print(f"Escolha atualizado: {estoque} itens")

#     elif escolha =="2":
#         quantidade = int(input("Digite a quantidade de itens a remover..."))
#         estoque-=quantidade
#         print(f"Estoque atualizado: {estoque} itens")
#         if estoque =="3":
#             print("Estoque Crítico!")

#     elif escolha =="3":
#         print("Saindo do simulador de estoque.")
#         break
#     else:
#       print("Opção inválida. Tente novamente.")

15
# print("Relatório de Turno Completo")
# totalpecas=5
# pecasaprovadas=0
# for i in range(1, totalpecas+1):
#      diametro= float(input("Digite o diâmetro da peça {i} em mm..."))
#      if 19.9 <= diametro <= 20.1:
#           pecasaprovadas += 1
# eficiencia = (pecasaprovadas/totalpecas)*100
# print(f"Total de peças aprovadas: {pecasaprovadas}")
# print(f"Eficiência do lote: {eficiencia:.2f}%")


