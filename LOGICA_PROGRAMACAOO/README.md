# 💻 Lógica de Programação com Python e GitHub

## 📖 Ementa e Conteúdo das Aulas

### 1. Fundamentos de Desenvolvimento e Versionamento
*   **Introdução à Lógica:** O que é um algoritmo, pensamento computacional e resolução de problemas.
*   **O Ambiente de Trabalho:** Instalação do Python, configuração do VS Code e uso do terminal.
*   **Git e GitHub Base:** O que é controle de versão, criação de conta no GitHub, configuração de `user.name` e `user.email`.
*   **Fluxo de Trabalho Inicial:** Inicializar repositório (`git init`), verificar status (`git status`), adicionar arquivos (`git add`) e criar pontos de salvamento (`git commit`).

### 2. Estruturas Fundamentais em Python
*   **Variáveis e Tipos de Dados:** Conceito de memória, tipos `int`, `float`, `str`, `bool` e a função `type()`.
*   **Entrada e Saída de Dados:** Interação com o usuário via `print()` e `input()` (e a necessidade de conversão de tipos/casting).
*   **Operadores Matemáticos e Lógicos:** Operadores aritméticos (`+`, `-`, `*`, `/`, `//`, `%`), relacionais (`>`, `<`, `==`, `!=`) e lógicos (`and`, `or`, `not`).

### 3. Estruturas de Controle de Fluxo
*   **Condicionais (Tomada de Decisão):** Sintaxe do `if`, `elif` e `else`. Recuo (identação) como regra estrutural do Python.
*   **Repetições (Laços de Iteração):** 
    *   Uso do `while` para repetições baseadas em condições de parada.
    *   Uso do `for` em conjunto com a função `range()` para repetições com número definido de passos.

### 4. Coleções de Dados e Modularização
*   **Listas:** Criação, indexação, fatiamento (slicing) e métodos principais (`.append()`, `.pop()`, `.len()`).
*   **Funções:** Modularização de código, declaração com `def`, passagem de parâmetros, argumentos e retorno de valores com `return`.

### 5. Colaboração e Portfólio no GitHub
*   **Conexão Remota:** Criação de repositórios no GitHub, vinculação local via `git remote add` e envio de código via `git push`.
*   **Boas Práticas de Commit:** Como escrever mensagens de commit claras e significativas.
*   **Portfólio:** Organização do perfil do GitHub e criação de um arquivo `README.md` descritivo para os projetos de lógica.

---

## 🛠️ Exemplos Práticos de Código e Comandos

### 🐍 Desafio de Lógica em Python
*Este script exercita entrada de dados, conversão de tipos, estruturas condicionais e laço de repetição.*

```python
# Programa para calcular a média de notas de um aluno e validar aprovação

print("--- SISTEMA DE NOTAS DA DISCIPLINA ---")

# Lista para armazenar as notas
notas = []
quantidade_notas = 3

# Laço para capturar as notas do aluno
for i in range(1, quantidade_notas + 1):
    while True:
        nota = float(input(f"Digite a nota {i} (0 a 10): "))
        if 0 <= nota <= 10:
            notas.append(nota)
            break
        print("Nota inválida! Digite um valor entre 0 e 10.")

# Cálculo da média utilizando funções nativas
media = sum(notas) / len(notas)

print(f"\nMédia final do aluno: {media:.2f}")

# Estrutura condicional para determinar o status
if media >= 7.0:
    print("Situação: APROVADO! 🎉")
elif media >= 5.0:
    print("Situação: RECUPERAÇÃO. 📚")
else:
    print("Situação: REPROVADO. ❌")
```

---

### 🐙 Guia de Comandos Git para os Alunos

#### Configuração Inicial (Apenas na primeira aula)
```bash
git config --global user.name "Seu Nome Completo"
git config --global user.email "seu_email@provedor.com"
```

#### Ciclo Diário de Envio de Exercícios para o GitHub
```bash
# 1. Inicializa o Git na pasta do projeto (feito apenas uma vez por projeto)
git init

# 2. Verifica quais arquivos foram criados ou modificados
git status

# 3. Adiciona todos os arquivos editados para a área de preparação (Stage)
git add .

# 4. Salva as alterações localmente com uma mensagem descritiva
git commit -m "Adiciona exercício de cálculo de média com validação"

# 5. Vincula o repositório local ao link do GitHub (feito apenas uma vez por projeto)
git remote add origin github.com

# 6. Envia o código do seu computador para o servidor do GitHub
git push -u origin main
```


