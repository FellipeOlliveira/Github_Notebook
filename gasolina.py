import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("gasolina.csv", delimiter=',')

sns.set(style="whitegrid")

plt.figure(figsize=(8,5))
sns.lineplot(data=df, x="dia", y="venda")

plt.title("Vendas por Dia")
plt.xlabel("Dia")
plt.ylabel("Venda")

plt.show()
