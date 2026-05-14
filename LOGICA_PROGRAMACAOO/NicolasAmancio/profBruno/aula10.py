# projeto cancela automática
# criar um algoritimo que consiga gerenciar entrada e saída de veículos, inserido valores por hora permanecida. simple statiments must be se 
# a forma de entrada e saída deve ser especificada e permitir o usuario inserir os dados necessitados para registro do veiculo 
# passos 
# 1- pressionar botão, imprimiu ticket 
# calcular tempo de permanencia 
# pagar ticket 
# devolver ticket na saida 
# 2- acesso por TAGs (sem parar,conect car...)
# liberar e fechar cancelas 
# calcular tempo de permanencia 
# gerar pagamento de fatura
# 3- erros
# verificar sinal de transmissão da TAGs 
# verificar acesso por ticket ou tag ao mesmo tempo 
# perdeu o ticket (levantar informações)
# problemas com a cancela




valorhr = 12
cancela0 = "aberta"
cancela1 = "fechada"
carro = "passar"
detect = "TAG"


while True:
    print("\n--- Bem-vindo ao shopping do brunão ---")
    print("1 - Entrada / 2 - TAG / 3 - Perdi Ticket / 0 - Problema Cancela / S - Sair")
    
    botão = input("Porfavor Digite um número para seguir o procedimento: \n")

    # se quiser sair do programa
    if botão.lower() == 's':
        print("Encerrando programa...")
        break

    # entrar apertando o botão
    if botão == "1":
        print(f"Ticket impresso, acesso liberado, cancela", cancela0)
        hrentrada = int(input("Digite a hora de entrada (0-23): \n"))
        hrsaida = int(input("Digite a hora de saída (0-23): \n"))
        total = (hrsaida - hrentrada) * valorhr 
        print("Total a se pagar é:", total)
        
        pago = int(input("Digite o valor para pagar: "))
        if total == pago:
            print("Cancela", cancela0, "Obrigada volte sempre")
        else:
            print("O Assistente está chegando, porfavor aguarde!")

    # detectar a TAG
    elif botão == "2" or botão.upper() == "TAG":
        print(f"Acesso liberado {detect}, pagamento na fatura, cancela", cancela0)

    # se perder o ticket 
    elif botão == "3":
        print("Será cobrada uma taxa fixa de R$ 50,00.")
        multa = 50
        pmulta = int(input("Digite o valor do pagamento: "))
        if pmulta >= multa:
            print("Pagamento registrado. Cancela", cancela0,)
        else:
            print("Algum erro foi encontrado aguarde o assistente")

    # se a cancela der problema 
    elif botão == "0":
        print("prblema na cancela identificado .")
        print("A cancela está com problema (fechada)")
        print("Por favor, o assistente está chegando aguarde.")

    elif carro == cancela1:  
        print("Cancela", cancela1)
    

    # se não identificar a TAG
        if detect != "TAG":
            print("TAG não identificada")
        else: 
            print("Tente de outra forma, ou espere o assistente")

            