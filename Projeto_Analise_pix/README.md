
# 📊 Projeto — Análise do Pix no Brasil (2020–2024)
##📌 Descrição

Este projeto tem como objetivo analisar a evolução do Pix no Brasil entre 2020 e 2024, comparando-o a outros meios de pagamento (TED, Cheque e Boleto).
Foram aplicadas técnicas de manipulação de dados com Pandas e visualização com Matplotlib, resultando em insights sobre crescimento, participação relativa e sazonalidade do Pix.

Os dados de Cartão de Credito foram extraidos de dados abertos do Banco Central através do link: https://www.bcb.gov.br/estatisticas/spbadendos?ano=2024
A planilha do Banco Central do Brasil normalmente vem em formato horizontal, por isso tivemos de tratar a tabela e os dados, no repositório as tabelas ja estão no formato adequado para análise!

## 🎯 Objetivo do Projeto
O objetivo deste projeto é:

Analisar a evolução dos métodos de pagamento no Brasil Identificar mudanças no comportamento financeiro da população Comparar métodos tradicionais e digitais Avaliar o crescimento do PIX Explorar relações entre diferentes formas de pagamento

## 📂 Fonte dos Dados

* Os dados utilizados neste projeto foram obtidos de fontes públicas:

>Banco Central do Brasil

* Dados de cartão de crédito sobre transações e valores movimentados.

>https://www.bcb.gov.br/estatisticas/spbadendos?ano=2024

*Kaggle*

* Dataset complementar sobre métodos de pagamento no Brasil.

>https://www.kaggle.com/datasets/clovisdalmolinvieira/brazilian-payment-methods

## 🛠 Tecnologias Utilizadas

    Python
    Pandas
    NumPy
    Matplotlib
    Seaborn

## 📊 Análises Realizadas

O projeto explora diferentes aspectos da evolução dos métodos de pagamento.

#### Evolução do PIX

Análise do crescimento anual do PIX desde sua criação.

📌 **Resultado:**

* O PIX apresenta crescimento explosivo após 2020, indicando rápida adoção da tecnologia de pagamentos instantâneos no Brasil.
* PIX vs Boleto
* Comparação entre dois importantes métodos digitais de pagamento.

📌 **Resultado:**

* O PIX passou a competir diretamente com o boleto como método de pagamento digital.
* Declínio do DOC
* Análise da queda do uso do DOC ao longo dos anos.

📌 **Resultado:**

* O DOC apresenta queda contínua, indicando substituição por métodos mais rápidos como PIX e TED.
* Correlação entre Métodos de Pagamento
* Foi calculada uma matriz de correlação entre os métodos de pagamento.

📌 **Resultado:**

* Métodos digitais tendem a apresentar correlação positiva, indicando crescimento conjunto.

#### 💳 Integração com Dados de Cartão de Crédito

Os dados de cartão de crédito foram integrados ao dataset principal através do campo Ano.

#### 📈 Participação dos Métodos de Pagamento
Foi realizada uma análise da participação relativa dos principais métodos de pagamento no último ano disponível.

Os métodos analisados incluem:

PIX / TED / Boleto / Cartão de crédito

*Essa análise permite visualizar a distribuição atual do sistema de pagamentos brasileiro.*

## 📊 Principais Insights

    ✔ Crescimento acelerado do PIX após 2020
    ✔ Redução significativa do uso de DOC
    ✔ Forte presença do cartão de crédito no sistema de pagamentos
    ✔ Competição direta entre PIX e boleto
    ✔ Digitalização progressiva dos meios de pagamento no Brasil


# 👨‍💻 Autor
### Leonardo Sales

***`Projeto desenvolvido para estudo e análise de Data Science aplicada ao sistema financeiro brasileiro.`***
