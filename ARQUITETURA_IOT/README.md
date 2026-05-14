# 🌐 Arquitetura IoT (Internet das Coisas)

## 📖 Ementa e Conteúdo das Aulas

### 1. Introdução à Arquitetura IoT
*   **Conceitos Básicos:** Definição, histórico e impacto do ecossistema IoT.
*   **Modelo de Camadas:** Camada de Percepção (Sensores/Atuadores), Camada de Rede (Gateways) e Camada de Aplicação (Nuvem).
*   **Protocolos de Comunicação:** Introdução ao MQTT, HTTP e CoAP.

### 2. Fundamentos de Hardware com Arduino
*   **Anatomia da Placa:** Portas Digitais, Analógicas, PWM, Alimentação e Microcontrolador ATmega328P.
*   **Componentes Eletrônicos:** Uso de protoboard, resistores, LEDs, diodos e transistores.
*   **Sensores e Atuadores:** Leitura de temperatura (DHT11/LM35), presença (PIR) e controle de relés/motores.

### 3. Programação para IoT: C++ (Edge/Dispositivo)
*   **Estrutura Básica:** Funções obrigatórias `setup()` e `loop()`.
*   **Sintaxe e Tipos de Dados:** `int`, `float`, `char`, `boolean` e manipulação de strings.
*   **Controle de Fluxo:** Condicionais (`if/else`, `switch`) e laços de repetição (`while`, `for`).
*   **Interrupções e Temporização:** Substituição do `delay()` por `millis()` para multitarefa.
*   **Comunicação Serial:** Uso do `Serial.begin()`, `Serial.print()` e leitura de comandos.

### 4. Programação para IoT: Python (Gateway e Integração)
*   **Comunicação Serial com Arduino:** Uso da biblioteca `pySerial` para ler dados do microcontrolador.
*   **Manipulação de Dados:** Estruturas de dados em Python (`listas`, `dicionários`, `JSON`).
*   **Conectividade e Protocolos:** Publicação e subscrição de dados usando a biblioteca `paho-mqtt`.
*   **Armazenamento e Visualização:** Criação de scripts para salvar dados em bancos (SQLite) ou enviar para dashboards (ThingsSpeak).


