# ChargeGrid Intelligence

## Integrantes

| Nome | RM |
| :--- | :--- |
| Enzo Seiji Delgado Tabuchi | 573156 |
| Henrique Almeida Lucareli | 569183 |
| Leonardo Scotti Tobias | 573305 |
| Luca Almeida Lucareli | 569061 |
| Natan Silva da Costa | 573100 |

---


## Descrição

O ChargeGrid Intelligence é uma plataforma de gerenciamento inteligente para eletropostos comerciais.

A solução realiza:

- Controle dinâmico de demanda
- Balanceamento de carga
- Tarifação automática
- Taxa de ociosidade
- Simulação de integração OCPP
- Simulação de integração MODBUS
- Previsão de demanda utilizando IA

---

## Problema

Comércios que disponibilizam carregadores para veículos elétricos enfrentam:

- Sobrecarga elétrica
- Falta de controle de potência
- Baixa rotatividade das vagas
- Dificuldade de cobrança
- Integrações fragmentadas

---

## Solução

A plataforma monitora o consumo do prédio em tempo real e distribui automaticamente a potência disponível entre os carregadores conectados.

---

## Arquitetura
### Arquitetura Geral

```mermaid
flowchart LR

A[Medidor de Energia<br/>MODBUS]
B[ChargeGrid Intelligence]
C[Carregador GoodWe<br/>OCPP]
D[Dashboard Comercial]
E[Cliente]
F[Sistema de Pagamento]
G[Cancela Inteligente]

A --> B

B --> C
B --> D
B --> F

E --> C

F --> G

D --> E
```

### Arquitetura do Fluxo do Controle da Demanda
```mermaid
flowchart LR

A[Leitura do Consumo Predial]
--> B{Consumo + Recarga<br/>Ultrapassa Limite?}

B -- Sim --> C[Reduz Potência dos Carregadores]
B -- Não --> D[Distribui Potência Normalmente]
C --> E[Atualiza Carregadores via OCPP]
D --> E
E --> F[Dashboard em Tempo Real]
```

### Sequência Operacional
```mermaid
sequenceDiagram
    autonumber

    participant M as Medidor MODBUS
    participant C as ChargeGrid
    participant E as EV Charger OCPP
    participant D as Dashboard

    M->>C: Consumo atual do prédio
    C->>C: Calcula potência disponível
    C->>E: Atualiza limite de recarga
    E->>D: Consumo da sessão

    Note over E,D: Se bateria atingir 100%<br/>e permanecer conectada<br/>por mais de 10 minutos,<br/>é aplicada taxa de ociosidade
```

## Tecnologias

- Python
- Streamlit
- Scikit-Learn

## Execução

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Funcionalidades

### Controle de Demanda
Distribuição de potência.

### Tarifação
Cobrança por consumo energético.

### Ociosidade
Multa após uma permanência excedente.

### OCPP
Simulação de controle de pagamento.

### MODBUS
Simulação de leitura do consumo predial.
