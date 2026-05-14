# 📋 Engenharia e Levantamento de Requisitos de Software

## 📖 Ementa e Conteúdo das Aulas

### 1. Introdução à Engenharia de Requisitos
*   **Ciclo de Vida:** Elicitação, análise, especificação, validação e gerenciamento de escopo.
*   **Importância:** Impacto de requisitos mal definidos no custo e no prazo de projetos de software.

### 2. Classificação de Requisitos
*   **Requisitos Funcionais (RF):** O que o sistema deve fazer (ex: fluxos de dados, regras de negócio, cálculos, geração de relatórios).
*   **Requisitos Não Funcionais (RNF):** Como o sistema deve operar (ex: desempenho, segurança, usabilidade, escalabilidade, portabilidade, restrições técnicas).

### 3. Técnicas de Elicitação de Requisitos
*   **Brainstorming:** Condução de sessões criativas para mapear ideias de funcionalidades sem julgamento prévio.
*   **Entrevistas:** Técnicas de perguntas abertas, fechadas e estruturadas com stakeholders e usuários-chave.
*   **Prototipagem:** Criação de wireframes de baixa, média e alta fidelidade para validação rápida de requisitos de interface.

### 4. Modelagem e Diagramas (UML e Processos)
*   **Diagrama de Casos de Uso:** Mapeamento de Atores, Casos de Uso, relacionamentos de `<<include>>` e `<<extend>>`.
*   **Diagrama de Atividades:** Modelagem do fluxo de trabalho e processos de negócio associados aos requisitos.

### 5. Documentação e Relatórios Técnicos
*   **Documento de Especificação de Requisitos (SRS):** Estrutura padrão IEEE 830 para descrição formal do sistema.
*   **Critérios de Aceite:** Definição clara do que torna uma funcionalidade concluída e aprovada.
*   **Matriz de Rastreabilidade:** Mapeamento do ciclo de vida do requisito desde a origem até o caso de teste.

---

## 🛠️ Modelos e Templates Práticos

### 📑 Estrutura de Especificação (Exemplo)

#### RF-001: Recuperação de Senha
*   **Descrição:** O sistema deve permitir que o usuário recupere sua senha de acesso.
*   **Atores:** Usuário não autenticado.
*   **Fluxo Principal:**
    1. O usuário clica em "Esqueci minha senha".
    2. O sistema solicita o e-mail cadastrado.
    3. O usuário insere o e-mail e clica em "Enviar".
    4. O sistema valida o e-mail e envia um token com link de expiração (15 minutos).
*   **Fluxo Alternativo:** E-mail não encontrado no banco de dados. O sistema exibe mensagem de erro.

#### RNF-001: Tempo de Resposta (Desempenho)
*   **Descrição:** O sistema deve processar a requisição de busca de relatórios em menos de 2 segundos sob carga normal.
*   **Categoria:** Desempenho.

---

### 💬 Roteiro Prático para Técnicas de Elicitação

#### Checklist para Entrevistas
1.  Qual é a principal dor ou problema no processo manual atual?
2.  Quem são as pessoas diretamente envolvidas na operação desta tela/funcionalidade?
3.  Quais informações ou dados de entrada são obrigatórios para concluir esta tarefa?

#### Regras de Ouro para Brainstorming
*   Foco em quantidade de ideias, não em qualidade inicial.
*   Proibido criticar ou descartar ideias durante a fase de geração.
*   Agrupar ideias semelhantes usando mapas mentais ou ferramentas como Miro/Mural.


