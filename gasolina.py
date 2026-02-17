import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("gasolina.csv", delimiter=',')

sns.set(style="whitegrid")

plt.figure(figsize=(8,5))

sns.lineplot(
    data=df,
    x="dia",
    y="venda",
    label="Preço da Gasolina (R$)"
)

plt.title("Variação do Preço da Gasolina por Dia")
plt.xlabel("Dia do Mês")
plt.ylabel("Preço (R$)")

plt.legend(title="Legenda")
plt.show()
