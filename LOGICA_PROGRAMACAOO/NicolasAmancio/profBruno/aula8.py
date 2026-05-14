# # clean code - aula 8
# # para que usar?
# # como usar?
# print("Clean Code- Aula 8")
# aula=8
# print(f"Estamos na aula {aula} de clean code")

# # manipulação de arquivos e texto 
# texto= " Python "
# print(texto.strip().upper()) #PYTHON)

# print(texto.strip().capitalize()) #"Python"
# print(texto.strip().title()) #"Python"
# print(texto.strip().replace(" ", "_")) #"Python"
# print(texto.strip().split()) #["Python"]

# # escrevendo
# with open("notas.txt", "w") as arquivo:
#     arquivo.write ("Estudar python hoje!")
#     arquivo.write("\nLer sobre clean code.")

# # lendo
# with open ("notas.txt", "r") as f:
#     conteudo= f.read
#     print(conteudo)


# # execução de comandos do sistema

# import os # importa o módulo os para interagir com o sistema operacional
# #  onde estou?
# print(os.getcwd())

# # listar arquivos na pasta
# print(os.listdir())

# # listar arquivos na pasta
# print(os.listdir())
# print(os.listdir("..")) #lista arquivo na pasta pai
# print(os.listdir("..\\..")) #lista de arquivos na pasta avô
# print(os.listdir("C:\\")) #Lista de arquivos da raiz C
# print(os.listdir("C:\\User")) #Lista de arquivos da pasta Users
# print(os.listdir("C:\\User\\Public")) #Lista de arquivos da pasta public

# # outros comandos úteis:
# # criar pasta
# os.mkdir("nova_pasta")
# # # renomear pasta 
# os.rename("nova_pasta", "pasta_renomeada")
# # # Excluir pasta
# os.rmdir("pasta_renomeada")

# exercicio 1 
# crie uum script que mostre o caminho da pasta atual
# import os 
# print(os.getcwd)

# exercicios 2
# liste os arquivos da pasta atual

# import os 
# print(os.listdir())

# exercicio 3
# crie uma pasta chamada "projetos" e depois renomeie para "meus_projetos". Por fim, exclua a pasta.

# import os 
# print(os.mkdir("projetos"))
# print(os.rename("projetos", "meus_projetos"))
# print(os.rmdir("meus_projetos"))

# exercicio 4 
# crie um arquivo chamado "log.txt" e escreva a mensagem "log de atividades". Depois, leia o conteúdo do arquivo e exiba na tela

# with open("log.txt", "w") as arquivo:
#     arquivo.write("log de atividades")
# with open("log.txt", "r") as arquivo:
#      conteudo = arquivo.read()
#      print(conteudo)

# # exercicio 5
# # crie um dicionario com informações sobre uma pessoa e acesse um valor usando uma chave
# pessoa={
#      "nome": "Alice",
#      "idade": 30,
#      "cidade": "São Paulo"
# }
# print(pessoa["nome"])

# pessoa2={
#      "nome": "Nicolas",
#      "Idade": 67,
#      "Cidade": "São Paulo"
# }
# print(pessoa[""])
# print(pessoa2["nome"])

# exercicio 6
# desligar o pc (comando para windows)

# import os
# with open("desliga.bat", "w") as desligar:
#      desligar.write("shutdown -s -t 3600 -c \Desligamento programado para daqui a 1 hora. Salve seu trabalho!\"") # -s comando para desligar e -t é tempo de definir e -a cancelar desligamento

# with open("desliga.bat","r") as desligar:
#      conteudo = desligar.read()
#      print(conteudo)
     

# exercicio 7 

# criar um arquivo de backup
# escreva um script que crie um arquivo de backup do arquivo "notas.txt" com o nome "notas_backup.txt". O script deve ler o conteúdo de "notas.txt" e escrever no novo arquivo 


# with open("notas.txt", "r") as arquivo_origem:
#      conteudo = arquivo_origem.read()

# with open("notas_backup.txt","w") as backup:
#     backup.write(conteudo)


# exemplo 2: criar um script de limpeza de arquivos 
# escreva um script que liste os arquivos de uma pasta e exclua os arquivos com extensão ".tmp". O script deve exibir uma mensagem para cada arquivo excluido.


# import os 
# pasta= os.listdir()
# for arquivo in pasta:
#      if arquivo.endwith(".txt"):
#           os.remove(arquivo)
#           print(f"Arquivo {arquivo} excluido.")
# print("limpeza de arquivos concluída.")


# exercicio 8: Criar um script de monitoramento de temperatura 
#escreva um script que monitore temperatura de um motor. O script deve ler a temperatura de um arquivo "temperatura.txt" e exibir uma mensagem de alerta se a temperatura estiver acima de 70°C




