# 1. Registro de Operador: Peça o nome do operador e o turno (A, B ou C). Exiba:
# "Operador [Nome] registrado no Turno [Turno]. Boa jornada!"

# nome= str(input("Digite seu nome:\n"))
# turno= str(input("digite seu turno (A, B ou C): \n"))
# print(f"Operador {nome}", f"registrado no turno {turno}")

# 2. Cálculo de Produção: Peça a quantidade de peças produzidas em 1 hora. Calcule e
# exiba quantas peças serão produzidas em um turno de 8 horas.

# peças= int(input("Digite a quandidade de peças em 1 hora: \n"))
# horas=8 
# resultado= peças*horas
# print(f"Quantidade peças produzidas em oito horas é de {resultado}")

# 3. Conversor de Unidade: O sistema lê uma pressão em Bar. Converta para PSI (1 Bar
# ≈ 14.5 PSI) e exiba com duas casas decimais.

# print("Bem-vindo ao conversor de unidade")
# bar= float(input("Digite o valor da pressão (bar): \n"))
# variavel= 14.5
# resultado= bar*variavel
# print(f"o valor de Bar transformado em PSI é de", {resultado})

# 4. Média de Qualidade: Peça 3 notas de inspeção de uma peça (0 a 10). Exiba a média
# aritmética simples delas.

# print("Bem-vindo a calculadora de peças")
# m1= int(input("Digite o valor da peça (0 a 10): \n"))
# m2= int(input("Digite o valor da segunda peça(0 a 10); \n"))
# m3= int(input("Digite o valor da terceira peça(0 a 10); \n"))
# resul= (m1+m2+m3)/3 
# print(f"Sua média final é",(resul))

# Termostato Inteligente: Peça a temperatura de um motor.
# ● Abaixo de 40°C: "Baixa carga".
# ● Entre 40°C e 70°C: "Normal".
# ● Acima de 70°C: "ALERTA: Resfriamento Ativado!".

# print("Bem-vindo ao termostrato inteligente:")
# temp= int(input("Digite a temperatura do MOTOR: \n"))
# if temp>=40:
#     print(f"Baixa carga")
# elif 40 < temp < 70:
#     print(f"Normal")
# else:
#     print(f"ALERTA: Resfriamento Ativado!")

# 6. Classificador de Lotes: O usuário insere o código do produto. Se começar com "A",
# exiba "Alimentos". Se "E", "Eletrônicos". Para qualquer outro, "Desconhecido".

# print("Bem-vindo ao classificador de lotes")
# Ali= str(input("Digite A para alimento: \n"))
# Ele= str(input("Digite E para eletronicos; \n"))
# if Ali=="A":
#     print(f"Alimentos")
# elif Ele=="E":
#     print(f"Eletronicos")
# else:
#     print(f"Desconhecido")

# 7. Segurança de Operação: A máquina só liga se o sensor_porta == "fechada" E o
# botao_emergencia == "desligado". Peça esses dois inputs e diga se a máquina pode
# iniciar.

# segurança de operação

# print("Maquina")
# sensorporta= str(input("Digite 'fechada' para inicializar a maquina: \n"))
# botaodemergencia= str(input("Digite 'desligado' para inicialiazar a maquina: \n"))
# if sensorporta=="aberta" and botaodemergencia =="ligado":
#     print(f"A maquina não pode ser inicializada")
# elif sensorporta=="fechada" and botaodemergencia =="desligado":
#     print("Maquina pode ser inicializada")
# else:
#     print(f"Sistema finalizado")
    

# 8. Cálculo de Descarte: Peça o total de peças produzidas e o total de defeituosas. Se
# o descarte for maior que 5% do total, exiba "Revisar Processo", caso contrário,
# "Processo Otimizado".

# total= int(input("Digite total de peças produzidas: \n"))
# defeito= int(input("Digite o valor de peças de feituosas:\n"))
# if defeito>=(total * 0.05):
#     print(f"Revisar processo")
# else:
#     print("Processo otimizado")


#  9. Validação de Medida: Uma peça deve ter entre 9.8mm e 10.2mm. Peça a medida e
# diga se está dentro da tolerância, acima ou abaixo.


# print("Validação de Medida")
# valor= float(input("Digite a medida da peça: \n"))
# if valor < 9.8:
#    print(f"Abaixo da tolerância")
# elif valor > 10.2:
#     print(f"Acima da tolerância")
# else:
#     print(f"Dentro da tolerância")

# 10.Contagem Regressiva de Setup: Use um for para fazer uma contagem regressiva
# de 10 até 1 para o início de uma prensa, e finalize com "Prensa Ativada!".

# print("Contagem Regressiva: \n")
# for i in range(10,0,-1):
#     print(i)
# print(f"Prensa Ativada!")

# 11.Soma de Produção (Acumulador): Use um while para pedir o peso de várias caixas.
# O loop para quando o usuário digitar 0. No fim, mostre o peso total acumulado.

# totalpeso = 0 
# while True:
#     peso= float(input(f"Digite o peso de caixa: \n "))
#     if peso == 0:
#      break
#     totalpeso += peso
# print(f"Peso total acumulado: {totalpeso}")

# 12.Múltiplas Leituras: Use um for para pedir a temperatura de 5 sensores diferentes.
# Ao final, mostre qual foi a maior temperatura lida.

mtemp=0 
for i in range(5):
    temp= int(input(f"temperatura do sensor:"))
    if temp > mtemp :
     total=i+temp
print(f"temperatura captada", (total))

# 13.Painel de Login: Crie um while que peça a senha do supervisor ("admin123").
# Enquanto ele errar, o programa diz "Acesso Negado". Ele tem apenas 3 tentativas.
# Se esgotar, exiba "Painel Bloqueado".

# senha="admin123"
# while True:

   



    
