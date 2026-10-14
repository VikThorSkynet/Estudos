# Missões e gabarito — Design Patterns em Python

Use junto à [trilha](../02-trilha/trilha.md). As respostas são autorais. Tente primeiro, consulte a dica depois e abra o gabarito só ao terminar sua tentativa. Respostas alternativas são válidas quando respeitam o contrato e você consegue explicar seus custos.

## Missões

| Código | Mundo | Missão | Resultado ou critério |
|---|---:|---|---|
| E01 | 0–1 | Calcular preço 2.500 × quantidade 4 | 10.000 centavos |
| E02 | 1 | Frete grátis a partir de 10.000; abaixo, 1.200 | Totais: 9.999 → 11.199; 10.000 → 10.000 |
| E03 | 1 | Criar função de subtotal com preço não negativo e quantidade inteira positiva | `(3500, 2)` → 7.000; quantidade zero ou fracionária → erro |
| E04 | 1 | Somar uma lista de itens `(preço, quantidade)` | `[(3500, 2), (1500, 1)]` → 8.500; lista vazia → 0 |
| E05 | 1 | Demonstrar dois nomes apontando para uma lista e depois uma cópia independente | Alterar cópia não muda lista original |
| E06 | 2 | Criar dois pedidos com listas independentes | Adicionar a um não muda o outro |
| E07 | 3 | Testar E03: comum, preço zero e quantidade inválida | Três testes passam e verificam promessas distintas |
| E08 | 4 | Criar Simple Factory para normal, expresso e retirada | Retirada custa 0; tipo desconhecido gera erro |
| E09 | 4 | Fazer cinco experimentos de criação | Distinguir Simple Factory, Factory Method, Abstract Factory, Builder e Prototype; analisar Singleton |
| E10 | 5 | Adicionar frete bicicleta: 800 + 100 × peso | Peso 2 → 1.000; consumidor permanece igual |
| E11 | 6 | Adaptar `cobrar(centavos)` para `pagar(reais)` | 12.345 centavos → `Decimal('123.45')` |
| E12 | 6 | Criar Facade de reserva, cobrança e confirmação | Ordem registrada; falha na cobrança não confirma |
| E13 | 6 | Decorar um frete normal com seguro de 500 | Peso 2: 1.400 → 1.900 |
| E14 | 6 | Criar Proxy de catálogo com invalidação explícita | Duas buscas iguais chamam origem uma vez; invalidar permite nova chamada |
| E15 | 7 | Inscrever dois ouvintes e remover um | Primeiro evento chega aos dois; segundo só ao inscrito |
| E16 | 7 | Validar novo → pago → enviado; proibir novo → enviado | Erro não altera o estado anterior |
| E17 | 7 | Template Method com leitura por linhas ou vírgulas | Mesmas regras de limpeza e validação |
| E18 | 8 | Bridge: relatório simples/detalhado × texto/HTML | Novo renderizador não altera tipos de relatório |
| E19 | 8 | Composite: caixa com preço 100 e subcaixa de 200 e 300 | Total 600; caixa vazia 0 |
| E20 | 8 | Flyweight: cem peças, dois tipos de modelo | Dois modelos; posições individuais |
| E21 | 8 | Chain: cupom antes de fidelidade; primeira regra aplicável vence | Cupom e fidelidade simultâneos usam cupom |
| E22 | 8 | Command: adicionar item e desfazer a última adição | Histórico reversível; lista volta ao estado anterior |
| E23 | 8 | Iterator: gerar preços abaixo de 2.000 | `[1500, 2000, 3500, 800]` → `[1500, 800]` |
| E24 | 8 | Mediator: coordenar dois campos e um botão | Botão habilitado apenas quando ambos não vazios |
| E25 | 8 | Memento: salvar e restaurar carrinho | Alterações posteriores não modificam o retrato |
| E26 | 8 | Interpreter: árvore de `2 + 3 * 4` | 14, sem `eval` |
| E27 | 8 | Visitor: relatório e contagem de itens físicos/digitais | Duas operações usam a mesma estrutura |
| E28 | 9 | Refatorar cálculo duplicado e retirar uma classe desnecessária | Saídas acordadas preservadas por testes |
| E29 | 10 | Retry: falhar duas vezes e acertar na terceira | 3 chamadas; atrasos 1 e 2; erro permanente não repete |
| E30 | 10 | Circuit breaker: limiar 2, pausa 10, relógio falso | Rejeição sem chamar origem; recuperação controlada |

### Dicas graduais

- E01–E07: escreva a saída esperada no papel; separe dados, cálculo e exibição; não use uma lista de classe para guardar itens de instâncias.
- E08–E11: escreva o contrato que o consumidor espera antes de criar a implementação. Dê nomes e unidades explícitos aos valores.
- E12–E17: registre chamadas numa lista para conferir ordem; defina política de erro e transições antes do código.
- E18–E27: desenhe dois ou três objetos e as setas de colaboração. A intenção importa mais que um nome de classe.
- E28–E30: tenha exemplos que falhem se o comportamento ficar incorreto; use dependências falsas para relógio, espera e serviço.

## Gabarito comentado

### E01 — atribuir e multiplicar

```python
preco_centavos = 2500
quantidade = 4
total_centavos = preco_centavos * quantidade
print(total_centavos)  # 10000
```

Não some 2.500 + 4: quantidade indica quantas unidades custam 2.500 cada. Explique a diferença antes de avançar.

### E02 — a fronteira importa

```python
def total_com_frete(subtotal):
    if subtotal < 0:
        raise ValueError("Subtotal inválido")
    frete = 0 if subtotal >= 10000 else 1200
    return subtotal + frete
```

Exatamente 10.000 já tem frete grátis. Usar `>` mudaria a regra nesse limite. Nesta missão, subtotal zero recebe o frete fixo; aceitar um carrinho vazio é uma decisão de negócio separada.

### E03 — validar o contrato de entrada

```python
def subtotal(preco, quantidade):
    if type(preco) is not int or preco < 0:
        raise ValueError("Preço deve ser um inteiro não negativo")
    if type(quantidade) is not int or quantidade <= 0:
        raise ValueError("Quantidade deve ser um inteiro positivo")
    return preco * quantidade
```

Nesta missão, `type(...) is int` rejeita booleanos: em Python, `bool` é uma subclasse de `int`, mas `True` não é uma quantidade válida no nosso contrato. Preço zero é permitido; quantidade zero não.

### E04 — acumular itens

```python
def subtotal_itens(itens):
    total = 0
    for preco, quantidade in itens:
        total += subtotal(preco, quantidade)
    return total
```

Use a função E03 no mesmo arquivo. A lista vazia não percorre o laço; o acumulador permanece zero. A versão `sum(subtotal(p, q) for p, q in itens)` é equivalente para esse contrato.

### E05 — nomes, referências e cópias

```python
original = ["poção"]
alias = original
alias.append("espada")
assert original == ["poção", "espada"]
copia = original.copy()
copia.append("escudo")
assert original == ["poção", "espada"]
```

`copy()` faz uma cópia superficial. Se os elementos fossem listas, elas continuariam compartilhadas. O exercício de Prototype em E09 explora essa diferença.

### E06 — estado por instância

```python
class Pedido:
    def __init__(self):
        self._itens = []

    def adicionar(self, preco, quantidade):
        subtotal(preco, quantidade)  # valida antes de alterar
        self._itens.append((preco, quantidade))

    def subtotal(self):
        return subtotal_itens(self._itens)
```

Use E03 e E04. Crie `a = Pedido()` e `b = Pedido()`; adicione só em `a`. Confira `b.subtotal() == 0`. Uma entrada inválida não pode deixar um item parcialmente adicionado.

### E07 — três promessas distintas

```python
import unittest

class TesteSubtotal(unittest.TestCase):
    def test_comum(self):
        self.assertEqual(subtotal(3500, 2), 7000)

    def test_preco_zero(self):
        self.assertEqual(subtotal(0, 2), 0)

    def test_quantidade_invalida(self):
        with self.assertRaises(ValueError):
            subtotal(3500, 0)
```

Adicione esses testes ao arquivo que contém E03. Rode `python -m unittest nome_do_arquivo.py`. Depois acrescente quantidade fracionária e booleana como desafio.

### E08 — centralizar seleção

Crie três classes com `calcular(peso)`. Na fábrica, selecione pelo tipo; para retirada, devolva um objeto que retorna zero. Para tipo desconhecido, lance `ValueError`. O [laboratório](../04-exemplos/laboratorio_patterns.py) contém uma implementação executável com validação de peso e um dicionário de construtores.

Trocar `if` por dicionário não elimina a decisão: ela passa a estar na tabela. Isso pode melhorar a leitura, mas não torna automaticamente a fábrica extensível sem qualquer mudança.

### E09 — cinco experimentos e uma análise

1. **Factory Method:** reutilize `Entrega.cotar` do Mundo 4 e acrescente `EntregaExpresso.criar_frete`. A operação do criador chama o método redefinível.
2. **Abstract Factory:** `FabricaGelo.criar_arma` e `criar_armadura` devolvem produtos do mesmo elemento; `FabricaFogo` faz o equivalente. Troque a fábrica e confira que os dois produtos mudam juntos.
3. **Builder:** guarde título e linhas em um builder; `construir` rejeita título ausente e devolve uma estrutura independente. Chamadas sucessivas não devem compartilhar acidentalmente a lista de linhas.
4. **Prototype:** use o experimento abaixo e explique cada efeito.
5. **Singleton:** compare dois consumidores de um objeto global mutável com dois consumidores recebendo objetos separados. A dependência explícita facilita isolar os testes. Uma variável global isoladamente não implementa toda a estrutura do padrão.

```python
from copy import copy, deepcopy

base = {"nome": "Mago", "itens": ["cajado"]}
superficial = copy(base)
profunda = deepcopy(base)
superficial["itens"].append("poção")
assert base["itens"] == ["cajado", "poção"]
assert profunda["itens"] == ["cajado"]
```

O gabarito é um conjunto de critérios, porque os produtos e o relatório podem ter formatos diferentes. O resultado deve demonstrar a responsabilidade específica de cada técnica.

### E10 — variar o cálculo

```python
class FreteBicicleta:
    def calcular(self, peso):
        if peso < 0:
            raise ValueError("Peso inválido")
        return 800 + 100 * peso
```

Passe esse objeto ao consumidor do Mundo 5. O novo algoritmo devolve 1.000 para peso 2. Se você adicionou um `if` em `Carrinho.total` para reconhecê-lo, ainda acoplou o consumidor à nova implementação.

### E11 — tradução de unidade e operação

```python
from decimal import Decimal

class LegadoFalso:
    def __init__(self):
        self.recebido = None

    def pagar(self, reais):
        self.recebido = reais
        return "ok"

class Adapter:
    def __init__(self, legado):
        self.legado = legado

    def cobrar(self, centavos):
        return self.legado.pagar(Decimal(centavos) / Decimal(100))

legado = LegadoFalso()
assert Adapter(legado).cobrar(12345) == "ok"
assert legado.recebido == Decimal("123.45")
```

Esse teste verifica o adapter, sem serviço externo. A validação de valores inválidos é uma extensão obrigatória para o projeto final. Um teste do consumidor usando fake deve conferir que ele chama `cobrar` com a unidade correta.

### E12 — coordenação e falha

Uma fachada recebe colaboradores com `reservar`, `cobrar` e `confirmar`. Execute nessa ordem; registre cada chamada. Se `cobrar` lança uma exceção, `confirmar` não deve ocorrer. Defina uma compensação para a reserva, como `liberar`, e teste que ela ocorre.

Uma ordem plausível no exercício é `reservar → cobrar → confirmar`, com `liberar` após falha de cobrança. Isso não resolve atomicidade entre serviços: uma resposta perdida pode esconder uma cobrança realizada. A missão pede coordenação simulada; os limites precisam estar documentados.

### E13 — envolver preservando o contrato

`FreteComSeguro` recebe um frete e implementa `calcular(peso)` delegando e somando 500. O consumidor não precisa saber se usa um frete básico ou decorado. Confira que o frete original continua custando 1.400 e o decorado 1.900.

Desafio de ordem: frete-base de 1.000; seguro fixo de 500; taxa de 10%. Aplicar taxa após seguro dá 1.650; seguro após taxa dá 1.600. Defina o arredondamento se usar valores que não resultem em centavos inteiros.

### E14 — proxy com política explícita

Use um dicionário por identificador. Em `buscar`, consulte a origem apenas se a chave não estiver presente. Ofereça `invalidar(id)` e remova a chave. Registre quantas chamadas chegam à origem. No laboratório, esse exemplo usa valores textuais imutáveis.

Se forem devolvidos objetos mutáveis, o chamador poderá alterar o conteúdo cacheado. Discuta cópia, imutabilidade ou autorização de alteração como parte do contrato. Para dados reais, defina também expiração ou atualização.

### E15 — inscrição e remoção

```python
class Eventos:
    def __init__(self):
        self.ouvintes = []

    def inscrever(self, ouvinte):
        if ouvinte not in self.ouvintes:
            self.ouvintes.append(ouvinte)

    def remover(self, ouvinte):
        self.ouvintes.remove(ouvinte)

    def publicar(self, evento):
        for ouvinte in tuple(self.ouvintes):
            ouvinte(evento)
```

Guarde as funções em variáveis para poder remover a mesma referência. O snapshot `tuple` evita que uma mudança na lista durante a publicação altere a iteração atual. A política aqui é síncrona e interrompe na primeira exceção; outra política deve ser escrita e testada.

### E16 — validar antes de alterar

O mapa de transições do Mundo 7 é suficiente. Faça `novo_estado = transicionar(atual, destino)`; só depois atribua. Uma exceção deixa o estado anterior intacto. Objetos State são uma extensão: delegue operações a uma instância do estado atual. O laboratório contém ambos os mecanismos.

### E17 — uma sequência, duas leituras

O método base chama `ler`, limpa cada registro e rejeita registros vazios; subclasses apenas escolhem `splitlines` ou `split(',')`. A entrada `" espada , escudo "` deve gerar `['ESPADA', 'ESCUDO']` na versão por vírgulas. `"espada,,escudo"` deve gerar erro, conforme nossa política. Se cada subclasse reimplementar `executar`, a sequência deixou de estar centralizada.

### E18 — duas dimensões em composição

`RelatorioSimples` e `RelatorioDetalhado` recebem um renderizador. Cada relatório chama operações como `titulo` e `linha`; `Texto` e `HTML` implementam essas operações. Introduzir `Markdown` exige uma nova implementação do renderizador, mantendo os relatórios. Não crie subclasses combinadas como `RelatorioDetalhadoHTML` para cada combinação.

### E19 — operação uniforme e recursão

```python
class Item:
    def __init__(self, valor):
        self.valor = valor

    def preco(self):
        return self.valor

class Caixa:
    def __init__(self, filhos):
        self.filhos = list(filhos)

    def preco(self):
        return sum(f.preco() for f in self.filhos)

caixa = Caixa([Item(100), Caixa([Item(200), Item(300)])])
assert caixa.preco() == 600
assert Caixa([]).preco() == 0
```

O cliente chama a mesma operação em folha e grupo. Evite incluir uma caixa dentro dela mesma; esse exemplo presume uma árvore válida e não detecta ciclos.

### E20 — separar compartilhado de individual

Uma fábrica conserva `modelos[tipo]`; peças conservam posição e referência ao modelo. Alternando dois tipos por cem peças, `len(modelos) == 2`. Alterar a posição de uma peça não muda a posição de outra. Dados do modelo devem ser tratados como imutáveis nesse exercício. Não coloque a posição dentro do modelo compartilhado.

### E21 — primeira resposta encerra

O tratador de cupom retorna o desconto quando o pedido tem cupom; caso contrário, delega para fidelidade. Fidelidade trata apenas quem atende sua regra; caso contrário, delega para desconto zero. Teste os quatro casos: nenhum, só cupom, só fidelidade, ambos. A regra “primeira aplicável vence” faz ambos usar cupom. Não some descontos se essa não for a política.

### E22 — ações e histórico

Um comando guarda carrinho, item e informação para remover a adição correspondente. `executar` adiciona; `desfazer` reverte. O controlador guarda comandos executados em pilha e desfaz o último. Guardar somente o valor e remover a primeira ocorrência pode apagar um item anterior igual. Use a posição/identificador apropriado ou uma política que permita apenas desfazer na ordem inversa.

### E23 — gerador

```python
def abaixo_do_limite(precos, limite):
    for preco in precos:
        if preco < limite:
            yield preco

resultado = list(abaixo_do_limite([1500, 2000, 3500, 800], 2000))
assert resultado == [1500, 800]
```

O preço 2.000 não entra porque a regra usa “abaixo”. Iterar novamente sobre o mesmo gerador já esgotado não reproduz os valores; crie um novo gerador. A lista `resultado` pode ser percorrida repetidamente.

### E24 — coordenação

Os campos notificam `mediador.alterou()`. O mediador lê ambos e define `botao.habilitado = bool(nome.strip()) and bool(email.strip())`. Nenhum campo manipula diretamente o botão. Essa validação verifica presença, não formato ou existência do endereço de e-mail. Escreva quatro testes para as combinações vazio/preenchido.

### E25 — retrato independente

Para itens imutáveis, guarde uma tupla em `salvar()` e crie uma lista nova em `restaurar(retrato)`. Para itens mutáveis, defina uma política de cópia adequada. O histórico conserva retratos, não deve editar internamente o carrinho. Verifique que adicionar depois do retrato não altera o retrato anterior.

### E26 — árvore de expressão

```python
class Literal:
    def __init__(self, valor):
        self.valor = valor
    def avaliar(self):
        return self.valor

class Soma:
    def __init__(self, esquerda, direita):
        self.esquerda, self.direita = esquerda, direita
    def avaliar(self):
        return self.esquerda.avaliar() + self.direita.avaliar()

class Multiplicacao(Soma):
    def avaliar(self):
        return self.esquerda.avaliar() * self.direita.avaliar()

expressao = Soma(Literal(2), Multiplicacao(Literal(3), Literal(4)))
assert expressao.avaliar() == 14
```

Neste exemplo compacto, a subclasse reutiliza o armazenamento dos dois operandos. Num projeto maior, uma classe-base `ExpressaoBinaria` comunica melhor essa relação. A estrutura da árvore expressa a precedência; ainda não há parsing de uma string.

### E27 — operações externas sobre tipos estáveis

`Fisico.aceitar(v)` chama `v.visitar_fisico(self)`; `Digital.aceitar(v)` chama `v.visitar_digital(self)`. Um `VisitanteRelatorio` devolve descrições; um `VisitanteContagem` atualiza contadores por tipo. Use o mesmo conjunto de itens com os dois visitantes. Uma nova operação cria um visitante; um novo tipo de item exige que os visitantes saibam tratá-lo.

### E28 — comportamento e complexidade

Antes, duas rotas calculam o mesmo subtotal em blocos duplicados. Extraia uma função de cálculo e preserve exemplos com zero itens, um item e múltiplos itens. Se você criou uma classe que apenas repassa o argumento para essa função e não representa outra responsabilidade, experimente removê-la. O gabarito é a preservação das promessas com uma estrutura que você consegue justificar; contar classes não mede qualidade.

### E29 — repetir apenas falhas permitidas

Crie um serviço que conta chamadas: nas primeiras duas lança `ErroTemporario`, na terceira retorna `ok`. A função de retry captura apenas `ErroTemporario`, limita a três tentativas totais e chama uma função `esperar` com 1 e 2. Injete `atrasos.append` como espera para testar sem dormir. Uma `ValueError` deve propagar na primeira tentativa.

O [laboratório](../04-exemplos/laboratorio_patterns.py) implementa essa política e valida o número de tentativas. Jitter é uma extensão: injete também uma fonte aleatória e teste os limites dos atrasos, sem exigir um número aleatório específico.

### E30 — memória entre chamadas

Com relógio começando em zero, provoque duas falhas temporárias. O circuito abre. Uma terceira chamada é rejeitada e **não incrementa o contador de chamadas do serviço**. Avance o relógio para 10; uma chamada de teste pode passar. Sucesso fecha e zera o contador; falha reabre e reinicia o prazo.

O laboratório implementa uma simulação sequencial. Ela não é uma solução pronta para múltiplas threads/processos. Uma versão concorrente deve controlar atomicamente as chamadas de teste e o estado. Testes com relógio falso verificam a política sem exigir espera real.

## Cinco desafios finais com respostas esperadas

1. **“Um `if` prova código ruim?”** Não. Avalie tamanho, estabilidade, duplicação e mudança necessária.
2. **“Toda Factory é Factory Method?”** Não. Identifique a estrutura do criador e o método redefinível, não apenas o nome.
3. **“Observer torna tudo assíncrono?”** Não. O exemplo local é síncrono e precisa de política de exceção.
4. **“Uma máquina de estados sempre exige classes State?”** Não. Uma tabela pode bastar; objetos State distribuem comportamento.
5. **“Retry pode duplicar um pagamento?”** Pode. Uma falha na resposta não prova ausência de efeito; a operação exige política de idempotência no local apropriado.

## Registro de tentativas

| Data | Exercício | Minha previsão | Resultado | Dificuldade | Próxima revisão |
|---|---|---|---|---|---|
| | | | | | |

Ao pedir ajuda, envie o código, o resultado esperado, o resultado observado e uma frase sobre sua tentativa. Assim podemos corrigir o raciocínio e não apenas substituir sua resposta.
