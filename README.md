# Análise da Resposta ao Degrau em Sistemas RC com Transformadas de Laplace

Este repositório contém um exemplo didático de análise da resposta ao degrau unitário em sistemas RC de primeira ordem, utilizando a **Transformada de Laplace** para modelagem simbólica e ferramentas de simulação numérica com Python.

📁 **Arquivo principal**: [`main.py`](main.py)  
🔗 **Repositório**: [https://github.com/vitor-souza-ime/laplace](https://github.com/vitor-souza-ime/laplace)

---

## 📌 Objetivo

Demonstrar, por meio de uma abordagem computacional, como resolver uma equação diferencial de um circuito RC de primeira ordem usando transformadas de Laplace e verificar sua resposta ao degrau unitário, tanto simbolicamente quanto numericamente.

---

## 🧪 Tecnologias e Bibliotecas Utilizadas

- [`SymPy`](https://www.sympy.org): Para manipulação simbólica e transformada de Laplace.
- [`NumPy`](https://numpy.org): Para cálculos numéricos.
- [`Matplotlib`](https://matplotlib.org): Para geração de gráficos.
- [`SciPy`](https://scipy.org): Para simulação da resposta ao degrau via `lti`.

---

## 🚀 Como Executar

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/vitor-souza-ime/laplace.git
   cd laplace
````

2. **Instale as dependências**:

   ```bash
   pip install sympy numpy matplotlib scipy
   ```

3. **Execute o script principal**:

   ```bash
   python main.py
   ```

---

## 📈 Resultado Esperado

Ao executar o script, serão exibidos:

* A função de transferência no domínio de Laplace $Y(s)$
* A resposta no tempo $y(t)$ obtida pela transformada inversa de Laplace
* Um gráfico mostrando a **resposta ao degrau** do sistema RC, que segue o comportamento esperado de um sistema de primeira ordem:

  $$
  y(t) = 1 - e^{-t}
  $$

---

## 📚 Fundamentação Teórica

O circuito RC é modelado pela equação diferencial:

$$
RC \cdot \frac{dy(t)}{dt} + y(t) = x(t)
$$

Ao aplicar a transformada de Laplace com entrada $x(t) = u(t)$, obtém-se:

$$
Y(s) = \frac{1}{s(RC \cdot s + 1)}
$$

E a resposta no tempo é:

$$
y(t) = 1 - e^{-t/RC}
$$

---

## 👨‍🏫 Aplicações

* Ensino de sistemas lineares dinâmicos
* Introdução ao uso de transformadas de Laplace
* Validação de modelos de primeira ordem
* Simulação computacional de circuitos elétricos

---

## 📄 Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

---

```


