import matplotlib.pyplot as plt

class AnomalyDetector:
    def __init__(self, dados):
        self.dados = dados
        self.media = self.calcular_media()
        self.desvio_padrao = self.calcular_desvio_padrao()
    
    def calcular_media(self):
        soma = sum(self.dados)
        quantidade = len(self.dados)
        media = soma / quantidade
        return media
    
    def calcular_desvio_padrao(self):
        soma_dos_quadrados = sum((x - self.media) ** 2 for x in self.dados)
        variancia = soma_dos_quadrados / len(self.dados)
        desvio_padrao = variancia ** 0.5
        return desvio_padrao
    
    def definir_limite_anomalia(self, fator=3):
        limite_superior = self.media + fator * self.desvio_padrao
        limite_inferior = self.media - fator * self.desvio_padrao
        return limite_inferior, limite_superior
    
    def detectar_anomalias(self):
        limite_inferior, limite_superior = self.definir_limite_anomalia()
        anomalias = [valor for valor in self.dados if valor < limite_inferior or valor > limite_superior]
        return anomalias


class IQRAnomalyDetector:
    def __init__(self, dados):
        self.dados = sorted(dados)
        self.q1 = self.calcular_percentil(25)
        self.q3 = self.calcular_percentil(75)
        self.iqr = self.q3 - self.q1
    
    def calcular_percentil(self, percentil):
        index = int(len(self.dados) * percentil / 100)
        return self.dados[index]
    
    def definir_limite_anomalia(self, fator=1.5):
        limite_inferior = self.q1 - fator * self.iqr
        limite_superior = self.q3 + fator * self.iqr
        return limite_inferior, limite_superior
    
    def detectar_anomalias(self):
        limite_inferior, limite_superior = self.definir_limite_anomalia()
        anomalias = [valor for valor in self.dados if valor < limite_inferior or valor > limite_superior]
        return anomalias


class DataVisualizer:
    @staticmethod
    def plotar_dados(dados, anomalias_sd, anomalias_iqr):
        plt.figure(figsize=(10, 5))
        plt.plot(dados, label='Dados', color='blue')
        plt.scatter(
            [i for i, val in enumerate(dados) if val in anomalias_sd],
            [val for val in dados if val in anomalias_sd],
            color='red', label='Anomalias (Desvio Padrão)'
        )
        plt.scatter(
            [i for i, val in enumerate(dados) if val in anomalias_iqr],
            [val for val in dados if val in anomalias_iqr],
            color='orange', label='Anomalias (IQR)'
        )
        plt.legend()
        plt.xlabel('Índice')
        plt.ylabel('Valor')
        plt.title('Detecção de Anomalias')
        plt.show()



dados = dados("")

# Detecção de Anomalias usando Desvio Padrão
detector_sd = AnomalyDetector(dados)
anomalias_sd = detector_sd.detectar_anomalias()

# Detecção de Anomalias usando IQR
detector_iqr = IQRAnomalyDetector(dados)
anomalias_iqr = detector_iqr.detectar_anomalias()

# Visualização dos dados e anomalias
DataVisualizer.plotar_dados(dados, anomalias_sd, anomalias_iqr)
