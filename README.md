# Detecção de Anomalias

Este projeto implementa um modelo simples de detecção de anomalias em dados, sem o uso de bibliotecas externas além do `matplotlib` para visualização. O projeto inclui duas técnicas de detecção de anomalias: uma baseada no desvio padrão e outra baseada no intervalo interquartil (IQR).

## Descrição

### AnomalyDetector

A classe `AnomalyDetector` detecta anomalias nos dados utilizando o desvio padrão. O funcionamento é o seguinte:
1. **Calcular a Média**: Calcula a média dos dados.
2. **Calcular o Desvio Padrão**: Calcula o desvio padrão dos dados.
3. **Definir Limite de Anomalia**: Define os limites de anomalia como média ± (n * desvio padrão).
4. **Detectar Anomalias**: Identifica valores que estão fora do intervalo definido.

### IQRAnomalyDetector

A classe `IQRAnomalyDetector` detecta anomalias utilizando o intervalo interquartil (IQR). O funcionamento é o seguinte:
1. **Calcular Percentis**: Calcula o primeiro quartil (Q1) e o terceiro quartil (Q3).
2. **Calcular IQR**: Calcula a diferença entre Q3 e Q1.
3. **Definir Limite de Anomalia**: Define os limites de anomalia como Q1 - (fator * IQR) e Q3 + (fator * IQR).
4. **Detectar Anomalias**: Identifica valores que estão fora do intervalo definido.

### DataVisualizer

A classe `DataVisualizer` é utilizada para visualizar os dados e as anomalias detectadas. Ela cria um gráfico com os dados e destaca as anomalias detectadas por cada método.

## Como Usar

### Passo 1: Definir os Dados

Defina os dados a serem analisados:

- dados = 'defina seus dados aqui'

### Passo 2: Instanciar os Detectores de Anomalias

#### Crie instâncias das classes AnomalyDetector e IQRAnomalyDetector:

- detector_sd = AnomalyDetector(dados)
- detector_iqr = IQRAnomalyDetector(dados)

### Passo 3: Detectar Anomalias

Chame os métodos de detecção de anomalias:

- anomalias_sd = detector_sd.detectar_anomalias()
- anomalias_iqr = detector_iqr.detectar_anomalias()

### Passo 4: Visualizar os Dados

Utilize a classe DataVisualizer para visualizar os dados e as anomalias:

- DataVisualizer.plotar_dados(dados, anomalias_sd, anomalias_iqr)

### Requisitos
- Python 3.x
- Matplotlib para visualização (pip install matplotlib)
