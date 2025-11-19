import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# =============================
#   CARREGAR DADOS
# =============================
# Lê o arquivo data.txt ignorando o cabeçalho
df = pd.read_csv("data.txt", sep=r"\s+", header=0)

t = df.iloc[:, 0].values
f = df.iloc[:, 1].values

# =============================
#   FUNÇÃO PARA R² AJUSTADO
# =============================
def r2_ajustado(r2, n, k):
    return 1 - (1 - r2) * (n - 1) / (n - k - 1)

# =============================
#   PROCESSAR REGRESSÕES
# =============================
resultados = []

for grau in range(1, 11):
    poly = PolynomialFeatures(degree=grau)
    t_poly = poly.fit_transform(t.reshape(-1, 1))

    modelo = LinearRegression()
    modelo.fit(t_poly, f)
    
    f_pred = modelo.predict(t_poly)

    r2 = r2_score(f, f_pred)
    r2_adj = r2_ajustado(r2, len(t), grau)

    coef = modelo.coef_
    intercept = modelo.intercept_

    resultados.append((grau, intercept, coef, r2_adj))

    # =============================
    #   PLOT DA REGRESSÃO
    # =============================
    plt.figure(figsize=(8, 5))
    plt.scatter(t, f, color='black', s=15, label="Dados")
    
    t_grid = np.linspace(min(t), max(t), 500).reshape(-1, 1)
    t_grid_poly = poly.transform(t_grid)
    f_grid = modelo.predict(t_grid_poly)

    plt.plot(t_grid, f_grid, label=f"Polinômio grau {grau}")
    
    plt.xlabel("t")
    plt.ylabel("f(t)")
    plt.title(f"Regressão Polinomial — Grau {grau}")
    plt.grid(True)
    plt.legend()
    plt.savefig(f"regressao_grau_{grau}.png", dpi=150)
    plt.close()

# =============================
#   TABELA FINAL EM CSV
# =============================
linhas_csv = "grau,intercept,coeficientes,r2_ajustado\n"

for grau, intercept, coef, r2_adj in resultados:
    coef_str = "|".join([f"{c:.6f}" for c in coef])
    linhas_csv += f"{grau},{intercept:.6f},{coef_str},{r2_adj:.6f}\n"

with open("tabela_resultados.csv", "w") as f_out:
    f_out.write(linhas_csv)

# =============================
#   GRÁFICO DE R² AJUSTADO
# =============================
graus = [r[0] for r in resultados]
r2_vals = [r[3] for r in resultados]

plt.figure(figsize=(8, 5))
plt.plot(graus, r2_vals, marker='o')
plt.xlabel("Grau do Polinômio")
plt.ylabel("R² Ajustado")
plt.title("R² Ajustado em Função do Grau do Polinômio")
plt.grid(True)
plt.savefig("grafico_r2_ajustado.png", dpi=150)
plt.close()

print("\nProcesso concluído!")
print("→ Foram gerados:")
print("  • regressao_grau_1.png até regressao_grau_10.png")
print("  • grafico_r2_ajustado.png")
print("  • tabela_resultados.csv\n")
