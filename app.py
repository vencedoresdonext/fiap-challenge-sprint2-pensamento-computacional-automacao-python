import streamlit as st
from simulador import ChargeGridSimulator

st.set_page_config(page_title="ChargeGrid Intelligence - Simulação", layout="wide")

st.title("ChargeGrid Intelligence - Simulação")

sim = ChargeGridSimulator() # conectando com a class do simulador.py

# config para as configuracoes na barra
st.sidebar.header("Configurações")

sim.consumo_predio = st.sidebar.slider(
  "Consumo do Prédio (kW)",
  0, 100, 70
)

quantidade = st.sidebar.slider(
  "Veículos Conectados",
  1, 10, 3
)

for i in range(quantidade):
  sim.adicionar_veiculo(50)

potencias = sim.distribuir_potencia()

col1, col2, col3 = st.columns(3)

# big numbers
with col1:
  st.metric(
    "Consumo do Prédio", f"{sim.consumo_predio} kW"
  )

with col2:
  st.metric(
    "Potência Disponível", f"{sim.potencia_disponivel()} kW"
  )

with col3:
  st.metric(
    "Veículos", quantidade
  )

st.divider() # barrinha para dividir

# distribuindo para os carros
st.subheader("Distribuição")

for veiculo, potencia in potencias.items():
  st.progress(
    min(int(potencia), 100),
    text=f"Carro {veiculo}: {potencia} kW"
  )

st.divider()

# parte para ver o preço baseado na energia e no tempo
st.subheader("Tarifação")

energia = st.number_input(
  "Energia Consumida (kWh)",
  value=30
)

ocioso = st.number_input(
  "Minutos Ociosos",
  value=15
)

valor = sim.calcular_cobranca(
  energia,
  ocioso
)

st.success(f"Valor Total: R$ {valor}")

st.divider()

# simulacao da ocpp
st.subheader("Simulando a OCPP")

pagou = st.checkbox("Pagamento realizado")

status = sim.status_cancela(pagou)

if status == "LIBERADA":
    st.success("Cancela Liberada")
else:
    st.error("Cancela Bloqueada")