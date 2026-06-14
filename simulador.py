from dataclasses import dataclass

@dataclass
class Veiculo:
  id: int
  bateria: int
  conectado: bool = True
  minutos_ociosos: int = 0


class ChargeGridSimulator:
  def __init__(self, limite=100, consumo_predio=70):
    self.limite = limite
    self.consumo_predio = consumo_predio

    self.veiculos = []

    self.preco_kwh = 1.20 # aproximadamente 1,20 por kwH
    self.taxa_ociosidade = 0.50 # 50% de ausencia

  # metodo adicionar veiculo
  def adicionar_veiculo(self, bateria):
    novo = Veiculo(id = len(self.veiculos) + 1, bateria = bateria)

    self.veiculos.append(novo)

  # verificar a potencia disponivel
  def potencia_disponivel(self):
    return max(0, self.limite - self.consumo_predio)

  # distribuir a potencia
  def distribuir_potencia(self):
    ativos = [
        i for i in self.veiculos
        if i.conectado
    ]

    if not ativos: return {}

    potencia = self.potencia_disponivel()

    por_veiculo = potencia / len(ativos)

    return {
      v.id: round(por_veiculo, 2)
      for v in ativos
    }

  # calucular o preco final
  def calcular_cobranca(self, energia_consumida, minutos_ociosos):
    energia = energia_consumida * self.preco_kwh

    multa = max(
      0,
      minutos_ociosos - 10
    ) * self.taxa_ociosidade

    return round(energia + multa, 2)

  # status
  def status_cancela(self, pagamento_realizado):
    if pagamento_realizado:
      return "LIBERADA"

    return "BLOQUEADA"
