# Design Patterns em Python

Esta pasta é um percurso de estudo do zero ao avançado. Ela explica o que são padrões de projeto, para que servem e como reconhecer um problema em que podem ajudar.

**Comece por [Como estudar](COMO_ESTUDAR.md) e pela [primeira aula](01-fundamentos/primeira_aula.md).** Depois siga a trilha na ordem dos mundos. Você não precisa entender o laboratório completo nem assistir a todos os vídeos no primeiro dia.

## O que são Design Patterns?

São soluções de organização do código para problemas recorrentes em determinados contextos. Eles ajudam a distribuir responsabilidades e facilitar mudanças e testes. Um padrão não é uma biblioteca nem uma regra que deve aparecer em todo programa.

Por exemplo: uma loja pode usar Strategy para trocar o cálculo do frete, Adapter para integrar um provedor de pagamento e Observer para avisar interessados depois de uma compra. Cada um resolve uma dificuldade diferente.

## Onde está cada material

| Material | Para que usar |
|---|---|
| [Como estudar](COMO_ESTUDAR.md) | Entender o ritmo, a rotina e os critérios de avanço |
| [01 — Fundamentos](01-fundamentos/primeira_aula.md) | Fazer o primeiro programa e entender suas linhas |
| [02 — Trilha](02-trilha/trilha.md) | Seguir 12 mundos com explicações, diagramas e missões |
| [03 — Exercícios e gabarito](03-exercicios/exercicios_e_gabarito.md) | Resolver 30 exercícios e conferir o raciocínio |
| [04 — Exemplos](04-exemplos/README.md) | Executar o laboratório e seus testes |
| [05 — Projeto final](05-projeto-final/README.md) | Construir a Loja da Guilda e defender as escolhas |
| [06 — Vídeos e fontes](06-fontes/videos_e_notas.md) | Consultar os 13 vídeos únicos, links e notas |
| [07 — Progresso](07-progresso/PROGRESSO.md) | Registrar tentativas, XP e revisões |
| [Caderno completo](caderno_completo.md) | Ler o conteúdo principal em um único Markdown |

## Ordem de aprendizado

```text
Primeiro programa
    → lógica e funções
    → orientação a objetos e contratos
    → testes e SOLID
    → criação e Strategy
    → Adapter, Facade, Decorator e Proxy
    → Observer, State e Template Method
    → catálogo GoF completo
    → refatoração e resiliência
    → projeto final
```

A trilha cobre os 23 padrões GoF. O foco prático inicial está em Simple Factory, Factory Method, Strategy, Adapter, Facade, Decorator, Proxy, Observer, State e Template Method. Singleton é estudado com seus custos e riscos. Simple Factory não faz parte dos 23 padrões GoF.

## Prática e gamificação

Cada mundo tem missões de explicar, prever, construir, verificar, vencer um desafio e revisar. São até 160 XP por mundo, com insígnias de progresso. Os pontos ajudam a registrar prática; para avançar, você também precisa resolver os desafios e explicar suas escolhas.

Estimativa da trilha: 128 horas, aproximadamente 22 semanas a 6 horas por semana ou 32 semanas a 4 horas. Ajuste ao seu ritmo.

## Requisitos para executar

Python 3.10 ou superior e um editor de texto. Não há pacotes externos para instalar. Na raiz do repositório:

```text
python "Design Patterns/01-fundamentos/aula_01.py"
python "Design Patterns/04-exemplos/laboratorio_patterns.py"
python -m unittest discover -s "Design Patterns/04-exemplos" -p "test_*.py" -v
```

No Windows, `py` pode substituir `python`. Se houver erro de comando não encontrado, siga as instruções da primeira aula.

## Sobre as fontes

O material foi preparado em 14/10/2026. Metadados e legendas automáticas dos 13 vídeos foram acessados. As notas usam descrições e trechos consultados das legendas e não alegam revisão audiovisual integral. As falas completas dos vídeos não são reproduzidas. As explicações, exercícios e exemplos em Python são autorais.

O laboratório é uma demonstração didática com serviços simulados e memória local; o projeto final é um exercício para você construir. Consulte os limites no README dos exemplos.
