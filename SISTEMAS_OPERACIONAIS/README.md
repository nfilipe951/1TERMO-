# 💻 Lógica de Programação: Infraestrutura com Windows e Linux

## 📖 Ementa e Conteúdo das Aulas

### 1. Fundamentos de Sistemas Operacionais para Programadores
*   **Papel do S.O.:** Como a lógica de programação interage com o hardware através do Windows e Linux.
*   **Interface Gráfica (GUI) vs. Terminal (CLI):** Por que desenvolvedores utilizam a linha de comando.
*   **Variáveis de Ambiente:** O que é a variável `PATH` e como ela permite a execução de programas globalmente.

### 2. Manipulação de Arquivos e Diretórios via Terminal
*   **Navegação Básica:** Comandos para listar arquivos, criar pastas, mover, copiar e deletar elementos.
*   **Caminhos Absolutos vs. Relativos:** Entendendo a árvore de diretórios em ambos os sistemas.
*   **Permissões de Arquivos:** Noções básicas de segurança, leitura, escrita e execução (especial foco em Linux).

### 3. Automatização e Scripts de Inicialização
*   **Automação de Tarefas:** Introdução ao conceito de scripts para executar sequências lógicas de comandos.
*   **Scripts em Windows:** Criação de arquivos em lote estruturados (`.bat` ou `.cmd`).
*   **Scripts em Linux:** Introdução ao Shell Scripting básico (`.sh`) e uso do interpretador Bash.

### 4. Preparação de Ambientes de Desenvolvimento
*   **Gerenciadores de Pacotes:** Instalação automatizada de ferramentas de programação via terminal (Winget/Chocolatey no Windows e APT no Linux).
*   **Execução de Código:** Como compilar ou interpretar programas diretamente pela linha de comando em ambas as plataformas.

---

## 🛠️ Guia Comparativo de Comandos (CLI)


| Ação Pretendida | Terminal Windows (CMD / PowerShell) | Terminal Linux (Bash) |
| :--- | :--- | :--- |
| **Listar conteúdo da pasta** | `dir` | `ls` ou `ls -la` |
| **Mudar de diretório (pasta)** | `cd nome_da_pasta` | `cd nome_da_pasta` |
| **Voltar uma pasta atrás** | `cd ..` | `cd ..` |
| **Criar uma nova pasta** | `mkdir nome_da_pasta` | `mkdir nome_da_pasta` |
| **Criar um arquivo vazio** | `type nul > arquivo.txt` ou `echo. > arq.txt` | `touch arquivo.txt` |
| **Limpar a tela do terminal** | `cls` | `clear` |
| **Visualizar texto do arquivo** | `type arquivo.txt` | `cat arquivo.txt` |
| **Remover um arquivo** | `del arquivo.txt` | `rm arquivo.txt` |
| **Remover uma pasta vazia** | `rmdir nome_da_pasta` | `rmdir nome_da_pasta` |

---

## 📜 Exemplos Práticos de Scripts de Automação

### 🪟 Script para Windows (`organizador.bat`)
*Este script automatiza a criação de uma estrutura padrão de pastas para projetos de lógica.*

```cmd
@echo off
echo --- CRIANDO ESTRUTURA DE PROJETO LOGICA ---
mkdir projeto_logica
cd projeto_logica
mkdir codigos
mkdir documentacao
echo. > codigos\principal.py
echo Estrutura criada com sucesso no Windows!
pause
```

### 🐧 Script para Linux (`organizador.sh`)
*Este script executa a mesma lógica de criação de diretórios no ambiente Linux.*

```bash
#!/bin/bash
echo "--- CRIANDO ESTRUTURA DE PROJETO LOGICA ---"
mkdir -p projeto_logica/{codigos,documentacao}
touch projeto_logica/codigos/principal.py
echo "Estrutura criada com sucesso no Linux!"
# Nota: Para rodar este script, use o comando: chmod +x organizador.sh
```









