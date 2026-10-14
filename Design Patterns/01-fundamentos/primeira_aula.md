# Primeira aula —  fazer o computador seguir uma instrução

**Pré-requisito:** nenhum. **Chefe:** criar um programa que mostre seu nome, o nome da loja e o preço de um item.

Abra um editor de texto, crie uma pasta para o estudo e salve `aula_01.py`. No terminal dessa pasta, confira `python --version`; no Windows, `py --version` é uma alternativa. Se nenhum funcionar, instale Python pelo [site oficial](https://www.python.org/downloads/) e reabra o terminal. Os exemplos usam Python 3.10 ou superior e apenas a biblioteca padrão.

```python
print("Olá, explorador!")
preco = 35
quantidade = 2
total = preco * quantidade
print("Total:", total)
```

Execute `python aula_01.py` ou `py aula_01.py`. A saída esperada termina em `Total: 70`.

`print` exibe um valor. Aspas delimitam texto. `=` associa um nome a um valor; não significa comparação. `*` multiplica. O programa executa essas linhas em ordem: cria os valores, calcula e exibe.

```text
preco = 35 ─────────┐
                   ├── multiplicação ── total = 70 ── print
quantidade = 2 ─────┘
```

**Missões:** explique `=`; preveja o total para quantidade 3; mude o produto; confira quantidade 0, 1 e 3; resolva o chefe; refaça sem olhar. Quantidade zero dá total zero nesse cálculo; decidir se a loja aceita essa compra é uma regra separada.

**Revisão:** o que é uma instrução? O que delimitam as aspas? Qual a diferença entre o nome `total` e seu valor? Em que ordem as linhas executam? O que mudaria se o preço fosse 40?


## Faça agora

Execute o arquivo de exemplo a partir da raiz do repositório:

```text
python "Design Patterns/01-fundamentos/aula_01.py"
```

Mude preço para 40 e quantidade para 3. Explique por que o total é 120. Depois resolva [E01](../03-exercicios/exercicios_e_gabarito.md) e registre seu resultado em [Progresso](../07-progresso/PROGRESSO.md).

Continue no [Mundo 1 da trilha](../02-trilha/trilha.md) quando conseguir executar, alterar e explicar esse programa.
