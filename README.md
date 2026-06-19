# 🦸‍♂️ Classificador de Nível de Herói

Este projeto prático foi desenvolvido como parte do desafio de código proposto pela **DIO (Digital Innovation One)**. O objetivo principal foi aplicar os conceitos fundamentais da lógica de programação e eu escolhi utilizar Python.

---

## 💻 Sobre o Desafio

O script recebe o **nome** e a **quantidade de experiência (XP)** de um herói e, por meio de uma estrutura de decisão, determina a sua classificação em níveis (elos), cobrindo desde a categoria *Ferro* até *Radiante*.

### Requisitos Técnicos Aplicados:
*   **Variáveis:** Armazenamento dos dados inseridos pelo usuário.
*   **Operadores:** Utilização de operadores de atribuição e comparação.
*   **Laços de Repetição:** Controle de fluxo para validação de dados.
*   **Estruturas de Decisão:** Filtros condicionais (`if`, `elif`, `else`) para categorização do XP.

---

## ⚡ Diferencial Implementado

Para tornar a aplicação mais robusta e evitar falhas de execução (*runtime errors*), foi adicionada uma validação de dados na entrada do XP. 

Utilizando o método `.isdigit()` dentro de um laço de repetição `while`, o programa verifica se o valor digitado é composto apenas por números. Caso o usuário insira letras ou caracteres inválidos, o sistema exibe uma mensagem de alerta e solicita a informação novamente até que o dado seja válido.

---

## 📊 Regras de Negócio (Tabela de Níveis)

| XP Mínimo | XP Máximo | Nível Correspondente |
| :--- | :--- | :--- |
| Menor que 1.000 | — | **Ferro** |
| 1.001 | 2.000 | **Bronze** |
| 2.001 | 5.000 | **Prata** |
| 5.001 | 7.000 | **Ouro** |
| 7.001 | 8.000 | **Platina** |
| 8.001 | 9.000 | **Ascendente** |
| 9.001 | 10.000 | **Imortal** |
| Maior ou igual a 10.001 | — | **Radiante** |

---

## 🚀 Como Executar o Projeto

1. Certifique-se de possuir o **Python 3** instalado em seu ambiente.
2. Clone este repositório ou baixe o arquivo correspondente.
3. Abra o terminal no diretório do projeto e execute o comando:
```bash
   python nome_do_arquivo.py