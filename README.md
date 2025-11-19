# Análise de Regressão Polinomial para Modelagem de Dados

Este projeto explora a aplicação de técnicas de regressão polinomial para modelar uma relação não linear a partir de um conjunto de dados experimentais. Utilizando Python e bibliotecas como `scikit-learn`, `pandas` e `matplotlib`, o código ajusta polinômios de diferentes graus (1 a 10) aos dados para encontrar o modelo que melhor descreve o fenômeno, evitando o sobreajuste (*overfitting*).

Este trabalho foi desenvolvido para a disciplina de **Computação Inteligente** por **Claudeny Nivaldo Avelino**, sob orientação do **Prof. Juno Vitorino Saraiva**.

![Gráfico de R² Ajustado](https://i.imgur.com/uQd4uYF.png )
*Gráfico principal do projeto, mostrando o ponto de equilíbrio entre ajuste e complexidade do modelo.*

---

## 🎯 Contexto do Problema

Em pesquisas científicas, é comum coletar dados sem conhecer a relação matemática exata entre as variáveis. Este projeto simula o caso de um pesquisador que, ao estudar uma reação físico-química, coletou um conjunto de amostras `(t, f(t))`, onde `t` é o tempo e `f(t)` é o resultado observado.

O objetivo é encontrar um modelo matemático que explique e preveja os valores de `f(t)` a partir de `t`, utilizando apenas os dados disponíveis.

---

## 🛠️ Metodologia e Ferramentas

O script `regressao_polinomial.py` implementa uma solução completa para este problema:

1.  **Carrega os dados** do arquivo `data.txt` usando `pandas`.
2.  **Ajusta 10 modelos** de regressão polinomial, com graus variando de 1 a 10, utilizando `PolynomialFeatures` e `LinearRegression` do `scikit-learn`.
3.  **Avalia cada modelo** calculando o **R² ajustado**, uma métrica que penaliza a complexidade excessiva e ajuda a identificar o risco de *overfitting*.
4.  **Visualiza os resultados** gerando gráficos para cada ajuste e um gráfico final que mostra a evolução do R² ajustado.
5.  **Exporta os resultados**, incluindo coeficientes e métricas, para o arquivo `tabela_resultados.csv`.

### Tecnologias Utilizadas
*   **Python 3**
*   **NumPy**: Para operações numéricas.
*   **Pandas**: Para manipulação e leitura dos dados.
*   **Matplotlib**: Para a geração dos gráficos.
*   **Scikit-learn**: Para a implementação dos modelos de regressão.

---

## 🚀 Como Executar o Projeto

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/seu-usuario/seu-repositorio.git
    cd seu-repositorio
    ```

2.  **Crie e ative um ambiente virtual** (recomendado ):
    ```bash
    # Para Windows
    python -m venv .venv
    .\.venv\Scripts\activate

    # Para macOS/Linux
    python3 -m venv .venv
    source .venv/bin/activate
    ```

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```
    *Nota: Certifique-se de que o arquivo `requirements.txt` contém `numpy`, `pandas`, `matplotlib` e `scikit-learn`.*

4.  **Execute o script principal:**
    ```bash
    python regressao_polinomial.py
    ```

---

## 📊 Resultados e Análise

Após a execução, o script irá gerar os seguintes arquivos:

*   `regressao_grau_1.png` a `regressao_grau_10.png`: Gráficos do ajuste de cada modelo polinomial sobre os dados.
*   `grafico_r2_ajustado.png`: Gráfico que mostra a evolução do R² ajustado em função do grau do polinômio.
*   `tabela_resultados.csv`: Tabela com o grau, intercepto, coeficientes e R² ajustado para cada um dos 10 modelos.

### Conclusão da Análise

A análise do gráfico `grafico_r2_ajustado.png` é crucial. Observa-se que o valor do R² ajustado cresce rapidamente até o **grau 8**, ponto a partir do qual os ganhos se tornam marginais.

Isso indica que o **modelo polinomial de grau 8** oferece o melhor equilíbrio entre precisão e complexidade. Modelos com grau superior (9 e 10) provavelmente estão se sobreajustando (*overfitting*) ao ruído dos dados, o que prejudicaria sua capacidade de prever novas observações.

---

## 📜 Licença

Este projeto é de código aberto e está disponível para uso e modificação.
