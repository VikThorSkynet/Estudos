# Caderno completo — Design Patterns em Python

Preparado em 14/10/2026, com Python como linguagem escolhida para começar do zero.

**Conteúdo:** links e notas de 13 vídeos únicos; trilha autoral em 12 mundos; diagramas; 30 exercícios com gabarito; missões, XP e projeto final.

**Sobre as transcrições:** as legendas automáticas foram acessadas para consultar os conteúdos, mas este caderno não reproduz transcrições integrais de vídeos de terceiros. A primeira parte contém resumos e distingue a consulta das explicações autorais.

## Navegação

- [Vídeos, links e notas](#videos)
- [Trilha do zero ao avançado](#trilha)
- [Exercícios e gabarito](#gabarito)

**Para começar hoje:** entre na trilha, faça o Mundo 0 e resolva E01 antes de abrir o gabarito. Não é necessário assistir a todos os vídeos primeiro.

O código complementar está em [04-exemplos/laboratorio_patterns.py](04-exemplos/laboratorio_patterns.py). As subpastas deste módulo contêm os cadernos separados, as instruções e os testes. O laboratório é uma demonstração intermediária; o projeto final é uma missão para você construir.


---

<a id="videos"></a>

## Parte 1 — Vídeos e notas

Consulta em 14/10/2026. Foram identificados **13 vídeos únicos**: os 11 itens públicos retornados pela playlist e dois vídeos avulsos adicionais. O vídeo de Simple Factory foi enviado avulso e também está na playlist, na posição 10; foi registrado uma única vez.

### O que foi acessado

**Metadados e legendas automáticas em português foram acessados para os 13 vídeos.** As notas abaixo usam descrições dos autores e trechos textuais consultados das legendas; não representam revisão audiovisual integral. Legendas automáticas podem errar nomes, termos técnicos e pontuação.

**Este arquivo contém notas e resumos, não transcrições integrais.** Não reproduzo integralmente falas de vídeos de terceiros a partir dos links. Se você fornecer os textos das transcrições, posso organizá-los em Markdown com os respectivos links.

As primeiras tentativas de páginas retornaram HTTP 429. A consulta posterior de metadados e trilhas de legendas foi bem-sucedida; essa falha inicial não significa que as legendas estavam ausentes.

A playlist pode mudar após a consulta. A lista cobre os 11 itens públicos retornados nesta data; itens privados, removidos ou não retornados não foram identificados.

### Links originais recebidos

- [Vídeo 1](https://youtu.be/9sI8KHEjs0M?si=DGY0dsQgSkPrXPmB)
- [Vídeo 2](https://youtu.be/J-lHpiu-Twk?si=YHQKUh3o6JBMwS9j)
- [Playlist](https://youtube.com/playlist?list=PLNHxHgB-_LTt67szNmMsZwqBKq9jH4uKJ&si=IBf1I0VGnGeIpf6e)
- [Simple Factory, também presente na playlist](https://youtu.be/3-ESljj0jgI?si=qn1WLH1uYZpOUvIu)

### Inventário

| Código | Posição na playlist | Vídeo | Canal | Duração | Legendas acessadas |
|---|---:|---|---|---:|---|
| V01 | avulso | [5 Design Patterns Que Todo Dev Deveria Conhecer](https://www.youtube.com/watch?v=9sI8KHEjs0M) | Augusto Galego | 16:41 | automáticas, pt-orig |
| V02 | avulso | [Design Patterns // Dicionário do Programador](https://www.youtube.com/watch?v=J-lHpiu-Twk) | Código Fonte TV | 8:22 | automáticas, pt-orig |
| V03 | 1 | [Padrão de Projeto Proxy: Melhore a Arquitetura do Seu Código Usando Orientação a Objetos!](https://www.youtube.com/watch?v=el1MtIPXTqo) | Renato Augusto | 19:14 | automáticas, pt-orig |
| V04 | 2 | [Padrão de Projeto Singleton: Multithreading & Testes Unitários Expõem os Riscos deste Design Pattern](https://www.youtube.com/watch?v=E8ey3HjSthg) | Renato Augusto | 21:52 | automáticas, pt-orig |
| V05 | 3 | [Padrão de Projeto Decorator: O Design Pattern que Flexibiliza seu Código com Orientação a Objetos!](https://www.youtube.com/watch?v=7B60j9EGrrU) | Renato Augusto | 25:04 | automáticas, pt-orig |
| V06 | 4 | [Padrão de Projeto Template Method: Como Eliminar Códigos Duplicados Usando Orientação a Objetos!](https://www.youtube.com/watch?v=j5fGTi8ObK4) | Renato Augusto | 16:52 | automáticas, pt-orig |
| V07 | 5 | [SOLID, Clean Code e Design Patterns: Pare de Buscar o Código Perfeito!](https://www.youtube.com/watch?v=yZRd_EWUs1g) | Renato Augusto | 8:22 | automáticas, pt-orig |
| V08 | 6 | [Padrão de Projeto Observer: Como Criar Código Reativo e Escalável Usando Orientação a Objetos!](https://www.youtube.com/watch?v=mv9JxI85Ac8) | Renato Augusto | 20:53 | automáticas, pt-orig |
| V09 | 7 | [Padrão de Projeto Facade: O Design Pattern Que Simplifica Código Complexo com Orientação a Objetos!](https://www.youtube.com/watch?v=4Aq9UHQ5f5Y) | Renato Augusto | 11:43 | automáticas, pt-orig |
| V10 | 8 | [Padrão de Projeto State: Domine o Design Pattern de Transições de Estado com Orientação a Objetos!](https://www.youtube.com/watch?v=OrCgWzpNszk) | Renato Augusto | 25:57 | automáticas, pt-orig |
| V11 | 9 | [Padrão de Projeto Adapter: Melhore sua Orientação a Objetos e Testes Unitários! Design Pattern (GOF)](https://www.youtube.com/watch?v=Fg1kEjaaBrs) | Renato Augusto | 18:30 | automáticas, pt-orig |
| V12 | 10 | [Padrão de Projeto Simple Factory: O Design Pattern Mais Fácil Explicado!](https://www.youtube.com/watch?v=3-ESljj0jgI) | Renato Augusto | 13:32 | automáticas, pt-orig |
| V13 | 11 | [Padrão de Projeto Strategy: Tudo o Que Você Precisa Saber Sobre Esse Design Pattern (GOF)](https://www.youtube.com/watch?v=DzlXwgsc_AU) | Renato Augusto | 22:12 | automáticas, pt-orig |

Duração total dos vídeos únicos: **3 h 49 min 14 s**. Tempo de assistir não equivale ao tempo de aprender; a trilha reserva bastante espaço para construir e revisar.

### Notas por vídeo

#### V01 — 5 Design Patterns Que Todo Dev Deveria Conhecer

Fonte: [Augusto Galego — assistir](https://www.youtube.com/watch?v=9sI8KHEjs0M). Duração: 16:41.

**Assunto:** Strategy, Observer, Adapter, máquina de estados e retry/circuit breaker.

**Resumo:** Apresenta cinco conjuntos de técnicas para facilitar manutenção e lidar com integrações. Strategy aparece com alternativas de notificação; Observer, com interessados em eventos; Adapter, com interfaces de pagamento incompatíveis. Depois, modela estados de um pedido por transições permitidas e aborda novas tentativas, backoff exponencial, jitter e bloqueio temporário de chamadas a um serviço indisponível. O conjunto mistura padrões GoF com modelos e técnicas de resiliência.

**Trechos para localizar os temas:** [1:00](https://www.youtube.com/watch?v=9sI8KHEjs0M&t=60s), [6:00](https://www.youtube.com/watch?v=9sI8KHEjs0M&t=360s), [8:00](https://www.youtube.com/watch?v=9sI8KHEjs0M&t=480s), [11:00](https://www.youtube.com/watch?v=9sI8KHEjs0M&t=660s), [14:00](https://www.youtube.com/watch?v=9sI8KHEjs0M&t=840s). Os tempos são pontos de entrada aproximados dos trechos consultados; não são capítulos oficiais nem delimitações exatas.

**Na trilha:** Mundos 3, 5–7 e 10.

**Pergunta de estudo:** Qual a diferença entre trocar um algoritmo, traduzir uma interface e interromper chamadas após falhas?

#### V02 — Design Patterns // Dicionário do Programador

Fonte: [Código Fonte TV — assistir](https://www.youtube.com/watch?v=J-lHpiu-Twk). Duração: 8:22.

**Assunto:** Conceito, história, três famílias e visão geral dos 23 padrões GoF.

**Resumo:** Introduz padrões como soluções recorrentes de projeto, relaciona o assunto à orientação a objetos e apresenta o catálogo GoF em três famílias. Passa rapidamente pelas intenções dos padrões e discute sua relação com manutenção, comunicação entre desenvolvedores e refatoração. Também alerta que forçar uma solução a se encaixar num padrão pode aumentar a complexidade. Serve como visão geral; não substitui a prática de cada padrão.

**Trechos para localizar os temas:** [0:26](https://www.youtube.com/watch?v=J-lHpiu-Twk&t=26s), [2:00](https://www.youtube.com/watch?v=J-lHpiu-Twk&t=120s), [3:00](https://www.youtube.com/watch?v=J-lHpiu-Twk&t=180s), [4:30](https://www.youtube.com/watch?v=J-lHpiu-Twk&t=270s), [6:30](https://www.youtube.com/watch?v=J-lHpiu-Twk&t=390s). Os tempos são pontos de entrada aproximados dos trechos consultados; não são capítulos oficiais nem delimitações exatas.

**Na trilha:** Mundo 3; consulta no Mundo 8.

**Pergunta de estudo:** Qual problema concreto uma abstração resolve, e quando seu custo supera o benefício?

#### V03 — Padrão de Projeto Proxy: Melhore a Arquitetura do Seu Código Usando Orientação a Objetos!

Fonte: [Renato Augusto — assistir](https://www.youtube.com/watch?v=el1MtIPXTqo). Duração: 19:14.

**Assunto:** Proxy e controle de acesso a uma operação.

**Resumo:** Mostra um objeto intermediário que representa outro e intercepta suas chamadas. O exemplo consultado usa um gerador de relatórios e uma camada de cache, preservando uma operação comum por interface. Discute como separar esse controle do controller e do serviço original e cita outras aplicações, como verificações de acesso e carregamento tardio. A validade do cache continua exigindo uma política específica.

**Trechos para localizar os temas:** [1:00](https://www.youtube.com/watch?v=el1MtIPXTqo&t=60s), [3:00](https://www.youtube.com/watch?v=el1MtIPXTqo&t=180s), [9:00](https://www.youtube.com/watch?v=el1MtIPXTqo&t=540s), [17:00](https://www.youtube.com/watch?v=el1MtIPXTqo&t=1020s). Os tempos são pontos de entrada aproximados dos trechos consultados; não são capítulos oficiais nem delimitações exatas.

**Na trilha:** Mundo 6.

**Pergunta de estudo:** O que invalida o resultado guardado e como conferir que a origem não foi chamada desnecessariamente?

#### V04 — Padrão de Projeto Singleton: Multithreading & Testes Unitários Expõem os Riscos deste Design Pattern

Fonte: [Renato Augusto — assistir](https://www.youtube.com/watch?v=E8ey3HjSthg). Duração: 21:52.

**Assunto:** Singleton, compartilhamento de instância e riscos de isolamento.

**Resumo:** Explica o controle de instância com um exemplo de logger e a estrutura de acesso estático. A descrição do autor destaca dificuldades com multithreading e testes; os trechos consultados também relacionam a discussão ao gerenciamento de dependências por frameworks. O assunto exige distinguir uma instância compartilhada de uma colaboração explicitamente recebida e considerar o escopo em que a unicidade é pretendida.

**Trechos para localizar os temas:** [1:00](https://www.youtube.com/watch?v=E8ey3HjSthg&t=60s), [3:00](https://www.youtube.com/watch?v=E8ey3HjSthg&t=180s), [10:00](https://www.youtube.com/watch?v=E8ey3HjSthg&t=600s), [19:00](https://www.youtube.com/watch?v=E8ey3HjSthg&t=1140s). Os tempos são pontos de entrada aproximados dos trechos consultados; não são capítulos oficiais nem delimitações exatas.

**Na trilha:** Mundo 4, depois do Mundo 3; revisitar no 10.

**Pergunta de estudo:** Se um teste altera a instância compartilhada, como garantir que o teste seguinte começa isolado?

#### V05 — Padrão de Projeto Decorator: O Design Pattern que Flexibiliza seu Código com Orientação a Objetos!

Fonte: [Renato Augusto — assistir](https://www.youtube.com/watch?v=7B60j9EGrrU). Duração: 25:04.

**Assunto:** Decorator e composição de comportamentos.

**Resumo:** Explica como envolver objetos para adicionar funcionalidades sem reescrever o componente base. Usa a analogia de roupas adicionadas a uma pessoa e aplica a ideia ao processamento de imagens, com operações como redimensionamento e marca d’água. Os envoltórios recebem o componente anterior e conservam uma operação comum. A seleção dos envoltórios e sua ordem determinam qual combinação o cliente utiliza.

**Trechos para localizar os temas:** [1:00](https://www.youtube.com/watch?v=7B60j9EGrrU&t=60s), [3:00](https://www.youtube.com/watch?v=7B60j9EGrrU&t=180s), [12:00](https://www.youtube.com/watch?v=7B60j9EGrrU&t=720s), [23:00](https://www.youtube.com/watch?v=7B60j9EGrrU&t=1380s). Os tempos são pontos de entrada aproximados dos trechos consultados; não são capítulos oficiais nem delimitações exatas.

**Na trilha:** Mundo 6.

**Pergunta de estudo:** O resultado muda se as operações forem aplicadas em outra ordem?

#### V06 — Padrão de Projeto Template Method: Como Eliminar Códigos Duplicados Usando Orientação a Objetos!

Fonte: [Renato Augusto — assistir](https://www.youtube.com/watch?v=j5fGTi8ObK4). Duração: 16:52.

**Assunto:** Template Method, sequência comum e etapas variáveis.

**Resumo:** Parte de processamento de documentos em formatos diferentes, como DOC, CSV e PDF. Identifica passos repetidos e organiza uma sequência comum numa classe-base, deixando etapas específicas para subclasses. A discussão mostra a redução de duplicação e chama atenção para o custo da herança: quem mantém o código precisa compreender a relação entre os métodos da base e as implementações específicas.

**Trechos para localizar os temas:** [1:00](https://www.youtube.com/watch?v=j5fGTi8ObK4&t=60s), [3:00](https://www.youtube.com/watch?v=j5fGTi8ObK4&t=180s), [8:00](https://www.youtube.com/watch?v=j5fGTi8ObK4&t=480s), [14:00](https://www.youtube.com/watch?v=j5fGTi8ObK4&t=840s). Os tempos são pontos de entrada aproximados dos trechos consultados; não são capítulos oficiais nem delimitações exatas.

**Na trilha:** Mundo 7.

**Pergunta de estudo:** Quais etapas realmente têm ordem fixa e quais precisam variar?

#### V07 — SOLID, Clean Code e Design Patterns: Pare de Buscar o Código Perfeito!

Fonte: [Renato Augusto — assistir](https://www.youtube.com/watch?v=yZRd_EWUs1g). Duração: 8:22.

**Assunto:** SOLID, Clean Code e padrões como ferramentas de decisão.

**Resumo:** Discute a insegurança causada pela busca de um código ideal e pela necessidade de aprovação externa. Trata princípios e padrões como ferramentas com benefícios e desvantagens, e usa exemplos de custos de abstrações para reforçar a importância do contexto. O foco é avaliar escolhas e evoluir com a prática, evitando transformar nomes de técnicas em critérios absolutos de qualidade.

**Trechos para localizar os temas:** [1:00](https://www.youtube.com/watch?v=yZRd_EWUs1g&t=60s), [3:00](https://www.youtube.com/watch?v=yZRd_EWUs1g&t=180s), [4:00](https://www.youtube.com/watch?v=yZRd_EWUs1g&t=240s). Os tempos são pontos de entrada aproximados dos trechos consultados; não são capítulos oficiais nem delimitações exatas.

**Na trilha:** Mundo 3; revisitar no 9.

**Pergunta de estudo:** Qual evidência mostraria que sua escolha melhorou a manutenção do caso concreto?

#### V08 — Padrão de Projeto Observer: Como Criar Código Reativo e Escalável Usando Orientação a Objetos!

Fonte: [Renato Augusto — assistir](https://www.youtube.com/watch?v=mv9JxI85Ac8). Duração: 20:53.

**Assunto:** Observer, inscrição e reação a mudanças.

**Resumo:** Apresenta a relação entre uma fonte de mudanças e interessados que reagem às notificações. Contrasta notificar observadores com espalhar verificações pelo código. Um exemplo consultado acompanha mudanças de preço do Bitcoin e diferentes reações, como notificação, atualização e registro. O tema também é relacionado a mecanismos de eventos em frameworks. Garantias de execução, assincronia e falhas precisam ser definidas à parte em cada implementação.

**Trechos para localizar os temas:** [1:00](https://www.youtube.com/watch?v=mv9JxI85Ac8&t=60s), [3:00](https://www.youtube.com/watch?v=mv9JxI85Ac8&t=180s), [8:00](https://www.youtube.com/watch?v=mv9JxI85Ac8&t=480s). Os tempos são pontos de entrada aproximados dos trechos consultados; não são capítulos oficiais nem delimitações exatas.

**Na trilha:** Mundo 7.

**Pergunta de estudo:** Como registrar e remover um interessado, e o que ocorre se ele falhar?

#### V09 — Padrão de Projeto Facade: O Design Pattern Que Simplifica Código Complexo com Orientação a Objetos!

Fonte: [Renato Augusto — assistir](https://www.youtube.com/watch?v=4Aq9UHQ5f5Y). Duração: 11:43.

**Assunto:** Facade e coordenação de um fluxo de compra.

**Resumo:** Usa um pedido de compra para mostrar como um cliente pode depender de uma operação simples em vez de conhecer todos os serviços e a ordem de chamadas. O exemplo envolve processamento de pagamento, confirmação, estoque e entrega. O fluxo é concentrado numa fachada e a discussão diferencia coordenar essas atividades de implementar dentro dela todas as regras específicas, relacionando o tema à responsabilidade única.

**Trechos para localizar os temas:** [1:00](https://www.youtube.com/watch?v=4Aq9UHQ5f5Y&t=60s), [3:00](https://www.youtube.com/watch?v=4Aq9UHQ5f5Y&t=180s), [5:00](https://www.youtube.com/watch?v=4Aq9UHQ5f5Y&t=300s), [8:00](https://www.youtube.com/watch?v=4Aq9UHQ5f5Y&t=480s). Os tempos são pontos de entrada aproximados dos trechos consultados; não são capítulos oficiais nem delimitações exatas.

**Na trilha:** Mundo 6.

**Pergunta de estudo:** Quais regras continuam nos serviços e qual política trata a falha no meio do fluxo?

#### V10 — Padrão de Projeto State: Domine o Design Pattern de Transições de Estado com Orientação a Objetos!

Fonte: [Renato Augusto — assistir](https://www.youtube.com/watch?v=OrCgWzpNszk). Duração: 25:57.

**Assunto:** State e comportamento conforme o estado atual.

**Resumo:** Discute estados e regras de transição com analogias de documentos e um exemplo de pedido. Em vez de apenas consultar uma string de estado, utiliza objetos que representam a situação atual e implementam as operações permitidas. Os trechos consultados mostram a evolução do pedido por etapas de preparação e entrega e a rejeição de ações que não fazem sentido naquela etapa.

**Trechos para localizar os temas:** [1:00](https://www.youtube.com/watch?v=OrCgWzpNszk&t=60s), [3:00](https://www.youtube.com/watch?v=OrCgWzpNszk&t=180s), [12:00](https://www.youtube.com/watch?v=OrCgWzpNszk&t=720s), [23:00](https://www.youtube.com/watch?v=OrCgWzpNszk&t=1380s). Os tempos são pontos de entrada aproximados dos trechos consultados; não são capítulos oficiais nem delimitações exatas.

**Na trilha:** Mundo 7.

**Pergunta de estudo:** Como o mesmo método responde de maneira diferente conforme o estado, e quem autoriza a transição?

#### V11 — Padrão de Projeto Adapter: Melhore sua Orientação a Objetos e Testes Unitários! Design Pattern (GOF)

Fonte: [Renato Augusto — assistir](https://www.youtube.com/watch?v=Fg1kEjaaBrs). Duração: 18:30.

**Assunto:** Adapter, interfaces incompatíveis e testes.

**Resumo:** Introduz adaptação com analogias de conexão e demonstra o assunto num gerador de relatório de vendas. O código usa bibliotecas de PDF com operações diferentes e as envolve por um contrato comum. Isso permite trocar a biblioteca sem espalhar seus detalhes no consumidor e facilita verificar a colaboração através de substitutos. Os exemplos do autor usam PHP; a trilha aplica a mesma intenção em Python.

**Trechos para localizar os temas:** [1:00](https://www.youtube.com/watch?v=Fg1kEjaaBrs&t=60s), [3:00](https://www.youtube.com/watch?v=Fg1kEjaaBrs&t=180s), [9:00](https://www.youtube.com/watch?v=Fg1kEjaaBrs&t=540s), [16:00](https://www.youtube.com/watch?v=Fg1kEjaaBrs&t=960s). Os tempos são pontos de entrada aproximados dos trechos consultados; não são capítulos oficiais nem delimitações exatas.

**Na trilha:** Mundo 6.

**Pergunta de estudo:** Que tradução o adapter realiza e qual teste a confirma sem gerar um PDF real?

#### V12 — Padrão de Projeto Simple Factory: O Design Pattern Mais Fácil Explicado!

Fonte: [Renato Augusto — assistir](https://www.youtube.com/watch?v=3-ESljj0jgI). Duração: 13:32.

**Assunto:** Simple Factory e seleção centralizada de objetos.

**Resumo:** Explica a centralização da criação através de alternativas de notificação, como e-mail, SMS e Slack. O código consumidor deixa de repetir as decisões de construção e passa a receber uma implementação com contrato comum. Relaciona a técnica a Strategy e diferencia o assunto das outras fábricas. O benefício central mostrado é concentrar a seleção; uma nova alternativa ainda pode exigir alterar a própria fábrica.

**Trechos para localizar os temas:** [1:00](https://www.youtube.com/watch?v=3-ESljj0jgI&t=60s), [3:00](https://www.youtube.com/watch?v=3-ESljj0jgI&t=180s), [6:00](https://www.youtube.com/watch?v=3-ESljj0jgI&t=360s), [11:00](https://www.youtube.com/watch?v=3-ESljj0jgI&t=660s). Os tempos são pontos de entrada aproximados dos trechos consultados; não são capítulos oficiais nem delimitações exatas.

**Na trilha:** Mundo 4.

**Pergunta de estudo:** Quais lugares precisam mudar para adicionar outra notificação, e onde permanece a decisão?

#### V13 — Padrão de Projeto Strategy: Tudo o Que Você Precisa Saber Sobre Esse Design Pattern (GOF)

Fonte: [Renato Augusto — assistir](https://www.youtube.com/watch?v=DzlXwgsc_AU). Duração: 22:12.

**Assunto:** Strategy e alternativas de algoritmo.

**Resumo:** Parte de um exemplo didático de cálculo de impostos para separar algoritmos antes reunidos numa decisão central. As alternativas são movidas para implementações com uma operação comum de cálculo e podem ser selecionadas em colaboração com uma fábrica. A discussão relaciona a estrutura à responsabilidade única e à extensão do sistema. A trilha usa fretes fictícios para praticar essa intenção sem depender de regras tributárias.

**Trechos para localizar os temas:** [1:00](https://www.youtube.com/watch?v=DzlXwgsc_AU&t=60s), [3:00](https://www.youtube.com/watch?v=DzlXwgsc_AU&t=180s), [11:00](https://www.youtube.com/watch?v=DzlXwgsc_AU&t=660s), [20:00](https://www.youtube.com/watch?v=DzlXwgsc_AU&t=1200s). Os tempos são pontos de entrada aproximados dos trechos consultados; não são capítulos oficiais nem delimitações exatas.

**Na trilha:** Mundo 5.

**Pergunta de estudo:** Adicionar um algoritmo altera seu consumidor ou apenas a seleção e a nova implementação?

### Cuidados de interpretação

- Simple Factory é uma técnica de criação e não uma das 23 entradas GoF.
- Uma máquina de estados não é automaticamente uma implementação do padrão GoF State.
- Observer pode ser local e síncrono. Mensageria distribuída envolve outras garantias.
- Retry e circuit breaker têm propósitos diferentes e ficam no módulo de resiliência.
- Os exemplos tributários do vídeo de Strategy são tratados como exemplos de programação. Os exercícios usam regras fictícias de frete.
- As explicações e exercícios da trilha são autorais; não atribuem aos vídeos os exemplos de código em Python.

Continue na [trilha de estudo](#trilha) e no [caderno de exercícios](#gabarito).

---

<a id="trilha"></a>

## Parte 2 — Trilha do zero ao avançado

Material autoral de estudo • preparado em 14/10/2026 • linguagem escolhida: Python.

### Como usar este caderno

Comece pelo Mundo 0. Faça os exercícios antes de consultar o [gabarito comentado](#gabarito). Os [vídeos e o registro de acesso](#videos) complementam a trilha. O [laboratório executável](04-exemplos/laboratorio_patterns.py) reúne exemplos das etapas intermediárias; não é necessário entendê-lo no primeiro dia.

Este caderno não é uma transcrição dos vídeos. As explicações, os exemplos, o projeto e os desafios foram criados para ensinar os assuntos. Consulte o arquivo de fontes para distinguir conteúdo verificado em legendas de descrições dos autores.

**Objetivo final:** ler um problema, identificar o que varia, escolher uma solução simples, implementar e testar; aplicar um padrão quando ele trouxer um benefício concreto. Conhecer nomes é apenas uma parte do trabalho.

### Seu jogo: Oficina dos Padrões

Você vai construir a **Loja da Guilda**, uma loja fictícia de itens de aventura. Ela começa calculando preços e termina com fretes, pagamento simulado, notificações, estados do pedido e tratamento de falhas. Não usaremos cobrança real, serviços pagos ou dados de clientes.

Cada mundo tem seis missões. Registre XP somente uma vez por missão concluída:

| Missão | Evidência necessária | XP |
|---|---|---:|
| Explicar | Explicar o conceito com suas palavras e uma analogia | 20 |
| Prever | Prever a saída de um exemplo antes de executá-lo | 20 |
| Construir | Implementar o exercício principal sem copiar a solução | 40 |
| Verificar | Conferir três casos: comum, limite e erro | 20 |
| Chefe | Resolver a mudança proposta e justificar a solução | 50 |
| Revisitar | Refazer uma parte de memória após sete dias | 10 |

São **160 XP por mundo**, até **1.920 XP**. Errar não tira pontos. Repetir a mesma tarefa não multiplica XP. A pontuação registra prática; não certifica domínio profissional.

| Faixa | Insígnia |
|---|---|
| 0–319 XP | Aprendiz da oficina |
| 320–639 XP | Explorador de objetos |
| 640–959 XP | Construtor de contratos |
| 960–1.279 XP | Investigador de padrões |
| 1.280–1.599 XP | Guardião dos testes |
| 1.600–1.920 XP | Projetista da guilda |

**Portão de avanço:** conclua Construir, Verificar e Chefe e acerte pelo menos quatro de cinco perguntas de revisão. Se não conseguir, revise apenas a dificuldade e tente um exemplo diferente. XP acumulado não substitui esse portão.

#### Ritmo sugerido

Estimativa didática: **128 horas**, aproximadamente 22 semanas de 6 horas ou 32 semanas de 4 horas. Ajuste pelo seu ritmo; os tempos não são promessas.

Uma sessão de 60 minutos: 10 min de recuperação de memória, 15 min de explicação ou vídeo, 25 min de código, 10 min para verificar e registrar uma descoberta. Faça três sessões de construção e uma de revisão por semana; acrescente sessões conforme a disponibilidade.

Revise depois de 1, 3, 7 e 14 dias. Feche o material e responda primeiro: “qual problema havia, o que varia, como resolvi e qual custo introduzi?”.

| Mundo | Tema | Horas | Desbloqueio |
|---|---|---:|---|
| 0 | Preparação e primeiro programa | 2 | Executar e alterar um arquivo |
| 1 | Lógica, funções e coleções | 16 | Calcular e validar entradas |
| 2 | Objetos, composição e contratos | 14 | Trocar uma implementação |
| 3 | Design Patterns, SOLID e testes | 8 | Identificar um problema de manutenção |
| 4 | Simple Factory e os padrões de criação | 10 | Centralizar criação com justificativa |
| 5 | Strategy | 8 | Adicionar um frete sem mudar o consumidor |
| 6 | Adapter, Facade, Decorator e Proxy | 12 | Integrar e envolver componentes |
| 7 | Observer, State e Template Method | 10 | Modelar eventos e transições |
| 8 | Os demais padrões GoF | 8 | Reconhecer todos os 23 e suas diferenças |
| 9 | Refatoração e decisão de projeto | 6 | Simplificar sem alterar comportamento |
| 10 | Retry, circuit breaker e concorrência | 10 | Simular falhas com limites |
| 11 | Projeto final e defesa das escolhas | 14 | Demonstrar comportamento e testes |

```mermaid
flowchart TD
    A[Executar Python] --> B[Lógica e funções]
    B --> C[Objetos e composição]
    C --> D[Contratos e testes]
    D --> E[Criação e Strategy]
    E --> F[Integração e padrões estruturais]
    F --> G[Eventos, estados e algoritmos]
    G --> H[Catálogo completo e refatoração]
    H --> I[Resiliência e projeto final]
```

Os diagramas Mermaid aparecem em leitores compatíveis. Também há esquemas em texto para estudar sem um renderizador.

### Mundo 0 — fazer o computador seguir uma instrução

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

### Mundo 1 — lógica antes de classes

#### 1.1 Valores, decisões e repetições

Use inteiros para contagens, texto para nomes e booleanos para decisões. Para preços nos exercícios, use **centavos inteiros**: 3.500 representa R$ 35,00. Isso evita ensinar arredondamento monetário com `float` logo no começo. Em sistemas reais, moeda, arredondamento e precisão precisam de regras explícitas.

```python
subtotal_centavos = 7000
if subtotal_centavos >= 10000:
    frete_centavos = 0
else:
    frete_centavos = 1200
print(subtotal_centavos + frete_centavos)  # 8200
```

`>=` pergunta se o valor é maior ou igual. O bloco indentado pertence à decisão. Em Python, a indentação faz parte da estrutura. `==` compara valores; `=` faz uma atribuição.

```text
Subtotal >= 10.000?
       ├── sim → frete 0
       └── não → frete 1.200
```

Uma lista guarda uma sequência. Um laço executa uma ação para cada elemento:

```python
precos = [3500, 2000, 1500]
subtotal = 0
for preco in precos:
    subtotal = subtotal + preco
print(subtotal)  # 7000
```

Na primeira passagem, subtotal vira 3.500; na segunda, 5.500; na terceira, 7.000. Depois de entender o percurso, compare com `sum(precos)`.

#### 1.2 Funções: dar nome a uma operação

Uma função recebe dados, executa uma operação e pode devolver um resultado. `return` devolve ao chamador; `print` só mostra na tela. Separar cálculo de exibição facilita reaproveitar e verificar o cálculo.

```python
def calcular_total(preco_centavos, quantidade):
    if preco_centavos < 0:
        raise ValueError("Preço não pode ser negativo")
    if quantidade <= 0:
        raise ValueError("Quantidade deve ser positiva")
    return preco_centavos * quantidade

print(calcular_total(3500, 2))  # 7000
```

`def` define a função. Os nomes entre parênteses são parâmetros. Os valores da chamada são argumentos. `raise` sinaliza que não é possível concluir a operação nas condições recebidas; não é uma mensagem de sucesso. Neste estágio, considere entradas inteiras; validação de tipo será um desafio posterior.

#### 1.3 Dicionários e mutabilidade

```python
produto = {"nome": "Poção", "preco_centavos": 3500}
print(produto["nome"])
produto["preco_centavos"] = 4000
```

Um dicionário associa chaves a valores. Listas e dicionários podem mudar. Se dois nomes apontam para a mesma lista, uma alteração aparece por ambos. Faça esse experimento antes de estudar Prototype:

```python
a = ["espada"]
b = a
b.append("escudo")
print(a)  # ['espada', 'escudo']
```

**Exercícios:** E01–E05 do caderno de exercícios. **Chefe:** carrinho com três produtos, quantidades positivas, subtotal e frete grátis a partir de 10.000 centavos. Dê nome às funções e mantenha o cálculo independente de `print`.

**Verificação:** total comum, subtotal exatamente 10.000, quantidade inválida. **Revisão:** `return` versus `print`; `=` versus `==`; função versus chamada; lista versus dicionário; erro de entrada versus resultado válido.

Referência para aprofundamento: [tutorial oficial de Python](https://docs.python.org/3.14/tutorial/).

### Mundo 2 — objetos, composição e contratos

#### 2.1 Uma classe reúne estado e comportamento

Na loja, cada pedido tem seus próprios itens e operações. A classe descreve a estrutura; cada instância é um pedido específico. `self` se refere à instância que recebe a chamada. `__init__` inicializa seus dados.

```python
class Pedido:
    def __init__(self):
        self._itens = []

    def adicionar(self, preco_centavos, quantidade):
        if preco_centavos < 0 or quantidade <= 0:
            raise ValueError("Item inválido")
        self._itens.append((preco_centavos, quantidade))

    def subtotal(self):
        return sum(preco * quantidade for preco, quantidade in self._itens)

p1 = Pedido()
p2 = Pedido()
p1.adicionar(3500, 2)
print(p1.subtotal(), p2.subtotal())  # 7000 0
```

O `_` em `_itens` indica uma convenção de uso interno; não é uma barreira de acesso. Encapsular é organizar as operações para preservar regras: por exemplo, adicionar através de um método que valida. Não basta renomear um atributo.

**Armadilha:** colocar `_itens = []` diretamente no corpo da classe faria a lista ser compartilhada se as instâncias não a substituíssem. Inicializá-la em `__init__` cria uma lista por pedido.

#### 2.2 Composição e herança

Composição significa que um objeto **usa ou contém** outro. Herança estabelece que uma classe **é um tipo de** outra e deve respeitar seu contrato. Não herde apenas para copiar algumas linhas.

```text
Composição: Loja → usa → CalculadoraDeFrete
Herança:    FreteExpresso → é uma implementação de → ContratoDeFrete
```

Se você precisa trocar o cálculo de frete, receber um objeto calculador é uma opção flexível. Se precisa um esqueleto fixo de importação com etapas redefiníveis, herança pode fazer sentido. A decisão depende da relação e das mudanças esperadas.

#### 2.3 Polimorfismo e duck typing

Polimorfismo permite usar implementações diferentes através de uma operação comum:

```python
class FreteNormal:
    def calcular(self, peso):
        return 1000 + 200 * peso

class FreteExpresso:
    def calcular(self, peso):
        return 2000 + 400 * peso

def total_com_frete(subtotal, peso, frete):
    return subtotal + frete.calcular(peso)

print(total_com_frete(7000, 2, FreteNormal()))  # 8400
```

Essa função não precisa conhecer a classe concreta: precisa que o objeto forneça `calcular(peso)` e devolva um valor compatível. Esse estilo é chamado de duck typing. Ter o mesmo nome de método não basta: unidades, erros e efeitos também fazem parte do contrato.

Mais adiante, `Protocol` permite descrever estruturalmente operações para verificadores de tipos; `ABC` permite definir métodos abstratos e impedir a instanciação de uma classe incompleta. Anotações de tipo e `Protocol` não validam automaticamente os valores de entrada durante a execução. Veja [typing](https://docs.python.org/3.14/library/typing.html#typing.Protocol) e [abc](https://docs.python.org/3.14/library/abc.html).

**Exercício:** E06. **Chefe:** trocar o frete por um objeto falso que devolve sempre 500, sem mudar `total_com_frete`. **Revisão:** classe versus instância; atributo de classe versus atributo da instância; papel de `self`; composição versus herança; quais regras tornam dois objetos substituíveis?

### Mundo 3 — por que os padrões existem

Um padrão descreve uma solução recorrente para um problema em determinado contexto. Ele orienta a estrutura e as responsabilidades; não é um trecho universal de código para copiar. O catálogo GoF reúne 23 padrões de criação, estrutura e comportamento. Simple Factory é uma técnica de criação conhecida, mas não é um dos 23 padrões desse catálogo.

**Exemplo do problema:** o checkout verifica o tipo do frete, cria seu objeto, calcula o preço, chama o pagamento, salva relatório e envia mensagens. Cada mudança tem chance de afetar etapas que deveriam ser independentes. Primeiro identifique as responsabilidades e o comportamento esperado; depois avalie o padrão.

#### SOLID em linguagem concreta

| Princípio | Pergunta útil na loja | Aplicação possível |
|---|---|---|
| S — responsabilidade única | Que mudança de negócio faz este componente mudar? | Separar cálculo de preço da entrega de mensagens |
| O — aberto/fechado | Posso acrescentar uma alternativa sem reescrever seu consumidor? | Outra estratégia de frete respeita `calcular` |
| L — substituição | Esta alternativa cumpre as mesmas promessas? | Um frete não passa a devolver texto ou um valor negativo |
| I — segregação de interfaces | O cliente depende de operações que não usa? | Um leitor de catálogo não precisa poder apagar produtos |
| D — inversão de dependência | A regra central depende de um detalhe externo? | Checkout recebe um cobrador com contrato definido |

Injeção de dependência é fornecer uma colaboração de fora. Inversão de dependência é uma decisão sobre a direção das dependências entre regras e detalhes. É possível injetar uma classe concreta e continuar fortemente acoplado a ela. Nenhum princípio exige criar uma interface para cada função.

#### Um teste verifica uma promessa

```python
import unittest

def calcular_total(preco, quantidade):
    if preco < 0 or quantidade <= 0:
        raise ValueError("Entrada inválida")
    return preco * quantidade

class TesteTotal(unittest.TestCase):
    def test_duas_unidades(self):
        self.assertEqual(calcular_total(3500, 2), 7000)

    def test_quantidade_invalida(self):
        with self.assertRaises(ValueError):
            calcular_total(3500, 0)

if __name__ == "__main__":
    unittest.main()
```

Salve esse bloco como `test_total.py` e rode `python -m unittest test_total.py`. O primeiro teste confere uma saída; o segundo confere um erro esperado. Testes de caracterização registram o comportamento de um código existente antes de refatorar. Um comportamento observado pode ser um bug: decida se deve preservá-lo ou alterá-lo como uma mudança separada.

**Vídeos agora:** [Dicionário do Programador](https://www.youtube.com/watch?v=J-lHpiu-Twk) e [SOLID, Clean Code e Design Patterns](https://www.youtube.com/watch?v=yZRd_EWUs1g).

**Exercício:** E07. **Chefe:** escrever três testes para o carrinho antes de reorganizá-lo. **Revisão:** contexto de um padrão; três famílias GoF; custo de uma abstração; contrato; diferença entre refatorar e mudar comportamento.

### Mundo 4 — separar criação de utilização

#### 4.1 Simple Factory

**Problema:** vários lugares precisam decidir qual calculador de frete criar. Cada um repete decisões de construção. **Ideia:** centralizar a seleção e a construção. Analogia: um balcão entrega a ferramenta pedida; quem usa não precisa montá-la.

```python
class FreteNormal:
    def calcular(self, peso):
        return 1000 + 200 * peso

class FreteExpresso:
    def calcular(self, peso):
        return 2000 + 400 * peso

def criar_frete(tipo):
    if tipo == "normal":
        return FreteNormal()
    if tipo == "expresso":
        return FreteExpresso()
    raise ValueError("Tipo de frete desconhecido")

frete = criar_frete("normal")
print(frete.calcular(2))  # 1400
```

```text
tipo normal ── criar_frete ── FreteNormal ── calcular(2)
tipo expresso ─ criar_frete ── FreteExpresso ─ calcular(2)
```

O `if` foi concentrado na criação. Acrescentar um tipo ainda exige editar essa fábrica. Isso não torna a técnica inútil: o benefício pode ser simplesmente reduzir duplicação. Para dois objetos triviais usados uma vez, criá-los diretamente pode ser melhor.

#### 4.2 Factory Method é outra estrutura

No Factory Method, uma operação do criador usa um método de criação que subclasses podem redefinir. Uma função chamada `factory` não caracteriza, sozinha, esse padrão.

```python
class Entrega:
    def criar_frete(self):
        raise NotImplementedError

    def cotar(self, peso):
        return self.criar_frete().calcular(peso)

class EntregaNormal(Entrega):
    def criar_frete(self):
        return FreteNormal()

print(EntregaNormal().cotar(2))  # 1400
```

A operação `cotar` permanece no criador; `EntregaNormal` decide o produto. Custo: hierarquia adicional e mais indireção. Se a necessidade é apenas selecionar por uma string, Simple Factory pode bastar.

#### 4.3 Os outros três padrões de criação

**Abstract Factory:** cria famílias de produtos compatíveis. Uma interface `FabricaTema` cria botão e menu; `TemaClaro` devolve ambos claros e `TemaEscuro` ambos escuros. O cliente pede a família, evitando misturar peças incompatíveis. Exercício: fábrica de equipamento “gelo” cria arma e armadura do mesmo elemento. Chefe: impedir uma combinação inconsistente sem espalhar condicionais. Custo: adicionar um novo tipo de produto pode exigir alterar todas as fábricas.

**Builder:** constrói um objeto em etapas, principalmente quando há configurações e validações complexas. Exemplo: `RelatorioBuilder.adicionar_titulo(...).adicionar_linha(...).construir()`. O builder guarda o trabalho em andamento; `construir` valida e entrega o resultado. Exercício: montar um relatório sem permitir finalizar sem título. Chefe: gerar duas versões sem compartilhar indevidamente listas internas. Para três argumentos claros, um construtor costuma ser suficiente.

**Prototype:** cria a partir de um objeto existente. Exemplo: copiar uma configuração-base de personagem e ajustar seu nome. Exercício: compare `copy.copy` e `copy.deepcopy` numa ficha com lista de itens. Chefe: alterar a cópia sem mudar o original. Custo: cópias profundas podem ser caras e inadequadas para conexões, arquivos ou recursos externos. A política de cópia é parte da solução.

**Singleton:** controla a existência de uma única instância num escopo definido e oferece acesso a ela. Uma instância única num processo não significa uma instância única em toda a aplicação distribuída. Estado compartilhado pode vazar entre testes e exigir sincronização. Exercício: simule dois consumidores alterando uma configuração global e observe a interferência. Chefe: substituir o acesso global por dependências fornecidas explicitamente. Estude para reconhecer os custos; não o use como ponto de partida obrigatório.

**Vídeos:** [Simple Factory](https://www.youtube.com/watch?v=3-ESljj0jgI) e, depois, [riscos do Singleton](https://www.youtube.com/watch?v=E8ey3HjSthg).

**Exercícios:** E08–E09. **Chefe do mundo:** adicionar “retirada” com custo zero e explicar onde houve mudança. **Revisão:** quem decide a criação em Simple Factory? E em Factory Method? O que é uma família? O que fica no Builder antes de construir? Qual o escopo de uma instância única?

### Mundo 5 — Strategy: trocar como uma tarefa acontece

**Problema:** diferentes algoritmos de frete fazem o consumidor crescer com decisões e detalhes. **O que varia:** o algoritmo. **Ideia:** receber uma estratégia que cumpra um contrato comum.

```python
class Carrinho:
    def __init__(self, frete):
        self.frete = frete

    def total(self, subtotal, peso):
        return subtotal + self.frete.calcular(peso)

carrinho = Carrinho(FreteNormal())
print(carrinho.total(7000, 2))  # 8400
carrinho.frete = FreteExpresso()
print(carrinho.total(7000, 2))  # 9800
```

Use as classes de frete do Mundo 4. O carrinho coordena subtotal e frete; a estratégia conhece o cálculo específico. A fábrica pode escolher **qual objeto criar** e Strategy permite usar **qual algoritmo executar**. São responsabilidades diferentes e podem colaborar.

```mermaid
flowchart LR
    C[Carrinho] --> I[calcular peso]
    N[FreteNormal] -. cumpre .-> I
    E[FreteExpresso] -. cumpre .-> I
    R[Retirada] -. cumpre .-> I
```

**Python também permite funções:** se as estratégias não têm estado, `total(subtotal, peso, calcular_frete)` pode chamar uma função recebida. Não é preciso uma classe para cada cálculo. Escolha objetos quando estado ou várias operações fizerem parte da colaboração.

**Use quando:** alternativas mudam independentemente, precisam de testes separados ou são escolhidas durante a execução. **Custo:** mais componentes e uma decisão de seleção em algum lugar. Para uma decisão curta e estável, um `if` pode ser a melhor solução.

**Vídeo:** [Strategy](https://www.youtube.com/watch?v=DzlXwgsc_AU). **Exercício:** E10. **Chefe:** acrescentar frete de bicicleta sem editar `Carrinho.total`. Confira peso zero, peso 2 e entrada negativa, definindo claramente a regra para peso zero. **Revisão:** onde fica a seleção? O que permanece no consumidor? Qual contrato todas as estratégias respeitam? Como uma função poderia cumprir esse papel? Qual o custo?

### Mundo 6 — integrar, simplificar, envolver e controlar

#### 6.1 Adapter: traduzir uma interface

**Problema:** a loja espera `cobrar(centavos)`, mas um componente existente oferece `pagar(valor_em_reais)`. **Ideia:** envolver esse componente e traduzir a chamada. Analogia: adaptador de tomada.

```python
from decimal import Decimal

class ProvedorLegado:
    def pagar(self, reais):
        return f"SIMULADO: R$ {reais:.2f}"

class AdapterPagamento:
    def __init__(self, legado):
        self.legado = legado

    def cobrar(self, centavos):
        if centavos <= 0:
            raise ValueError("Valor inválido")
        reais = Decimal(centavos) / Decimal(100)
        return self.legado.pagar(reais)

print(AdapterPagamento(ProvedorLegado()).cobrar(8400))
```

```text
Checkout → cobrar(8400) → Adapter → pagar(84.00) → legado
```

Tradução também pode incluir unidade, formato de resposta e exceções. Custo: uma camada para manter e testar. Um fake substitui a dependência em um teste; um adapter integra interfaces diferentes. Nem todo fake é um adapter.

#### 6.2 Facade: uma porta de entrada para um subsistema

**Problema:** o cliente precisa conhecer a ordem de reserva, cobrança e geração de comprovante. **Ideia:** fornecer uma operação de maior nível, como `checkout.finalizar(pedido)`.

```text
Cliente → FacadeCheckout.finalizar
                    ├── estoque.reservar
                    ├── cobrador.cobrar
                    └── comprovante.gerar
```

A fachada coordena o caso de uso; regras de estoque continuam no estoque. Ela não deve acumular todos os cálculos e políticas. Facade pode reduzir o acoplamento do cliente sem eliminar a possibilidade de acesso às interfaces especializadas. Não garante atomicidade nem desfaz operações automaticamente. Chefe: simular cobrança que falha e definir o que acontece com a reserva.

#### 6.3 Decorator: acrescentar comportamento mantendo o contrato

**Problema:** várias combinações de adicionais geram muitas subclasses. **Ideia:** envolver um objeto e acrescentar comportamento, delegando o restante.

```python
class FreteComSeguro:
    def __init__(self, base):
        self.base = base

    def calcular(self, peso):
        return self.base.calcular(peso) + 500

print(FreteComSeguro(FreteNormal()).calcular(2))  # 1900
```

```text
Carrinho → calcular → ComSeguro → calcular → FreteNormal
                         +500                  1400
                    resultado final: 1900
```

O padrão Decorator não é sinônimo da sintaxe `@decorador` de Python. A sintaxe é um mecanismo da linguagem que pode ser usada para diferentes finalidades. Custo: ordem dos envoltórios pode influenciar o resultado e dificultar rastrear chamadas. Chefe: experimentar seguro fixo e taxa percentual em ordens diferentes e explicar a diferença.

#### 6.4 Proxy: controlar acesso ao objeto

**Problema:** carregar o catálogo é caro ou o acesso precisa ser controlado. **Ideia:** oferecer a mesma operação e decidir quando delegar. Um proxy pode fazer carregamento tardio, autorização ou cache.

```text
Cliente → ProxyCatalogo.buscar(id)
               ├── cache presente → devolve valor
               └── cache ausente → CatalogoReal → guarda → devolve
```

Um proxy de cache exige política de validade. Cachear um estoque mutável indefinidamente pode mostrar disponibilidade incorreta. Controle de autorização precisa ser verificado em todas as rotas relevantes. O padrão não resolve esses detalhes sozinho.

| Padrão | Intenção principal | Exemplo |
|---|---|---|
| Adapter | Compatibilizar interfaces | Centavos para API legada |
| Facade | Simplificar uso de um subsistema | Finalizar compra |
| Decorator | Acrescentar comportamento combinável | Seguro no frete |
| Proxy | Controlar acesso ao objeto | Catálogo com cache |

**Vídeos:** [Adapter](https://www.youtube.com/watch?v=Fg1kEjaaBrs), [Facade](https://www.youtube.com/watch?v=4Aq9UHQ5f5Y), [Decorator](https://www.youtube.com/watch?v=7B60j9EGrrU) e [Proxy](https://www.youtube.com/watch?v=el1MtIPXTqo).

**Exercícios:** E11–E14. **Chefe do mundo:** integrar um segundo cobrador simulado pelo mesmo contrato e oferecer seguro sem editar o frete original. **Revisão:** diferença entre as quatro intenções; o que é delegado; tradução de unidade; ordem dos decorators; validade de cache.

### Mundo 7 — eventos, estados e etapas

#### 7.1 Observer

**Problema:** ao concluir uma ação, vários interessados precisam saber dela. **Ideia:** registrar observadores e notificá-los. A fonte não precisa conhecer o detalhe de cada reação.

```python
class Eventos:
    def __init__(self):
        self._ouvintes = []

    def inscrever(self, ouvinte):
        self._ouvintes.append(ouvinte)

    def publicar(self, evento):
        for ouvinte in tuple(self._ouvintes):
            ouvinte(evento)

eventos = Eventos()
eventos.inscrever(lambda e: print("Painel recebeu:", e))
eventos.inscrever(lambda e: print("Relatório recebeu:", e))
eventos.publicar("pedido_pago")
```

```text
Evento pedido_pago ───┬── Painel
                     └── Relatório
```

Esse exemplo é **síncrono e em memória**. Se um ouvinte falhar, a exceção interrompe a publicação. Observer não implica uma fila distribuída, entrega garantida ou execução assíncrona. Antes de implementar outra política, decida como lidar com falhas, cancelamento de inscrição e ordem das notificações. Pub/sub com broker tem outras responsabilidades e garantias.

#### 7.2 Máquina de estados e State

Uma máquina de estados define estados e transições permitidas. Um mapa é suficiente para muitos fluxos simples:

```python
transicoes = {
    "novo": {"pago", "cancelado"},
    "pago": {"enviado"},
    "enviado": {"entregue"},
    "entregue": set(),
    "cancelado": set(),
}

def transicionar(atual, destino):
    if atual not in transicoes:
        raise ValueError("Estado de origem desconhecido")
    if destino not in transicoes[atual]:
        raise ValueError("Transição proibida")
    return destino
```

```mermaid
stateDiagram-v2
    [*] --> Novo
    Novo --> Pago: pagamento confirmado
    Novo --> Cancelado: cancelar
    Pago --> Enviado: despacho
    Enviado --> Entregue: recebimento
    Entregue --> [*]
    Cancelado --> [*]
```

O padrão GoF **State** vai além de uma tabela: delega o comportamento a objetos de estado. `EstadoNovo.pagar(pedido)` pode autorizar a ação e trocar o estado; `EstadoEnviado.pagar(pedido)` pode rejeitá-la. Analogia: o mesmo botão de uma máquina faz coisas diferentes conforme o modo atual.

**Strategy versus State:** Strategy troca uma política para uma tarefa; State representa uma situação interna que altera as operações permitidas. Uma máquina de estados pode existir sem implementar o padrão GoF State. Use objetos de estado quando os comportamentos de cada estado crescerem o suficiente para justificar a estrutura.

#### 7.3 Template Method

**Problema:** importar formatos distintos repete a mesma sequência geral. **Ideia:** definir o esqueleto numa classe base e deixar etapas específicas para subclasses.

```python
class Importador:
    def executar(self, texto):
        registros = self.ler(texto)
        if not registros:
            raise ValueError("Sem registros")
        return [r.strip().upper() for r in registros]

    def ler(self, texto):
        raise NotImplementedError

class ImportadorLinhas(Importador):
    def ler(self, texto):
        return texto.splitlines()

print(ImportadorLinhas().executar("espada\nescudo"))
```

`executar` fixa a sequência; `ler` varia. Chefe: tratar registros vazios e adicionar um importador por vírgulas preservando a mesma regra de validação. Custo: dependência da hierarquia e risco de subclasses quebrarem as promessas do algoritmo. Se muitas etapas variarem livremente, composição com estratégias pode ser mais adequada.

**Vídeos:** [Observer](https://www.youtube.com/watch?v=mv9JxI85Ac8), [State](https://www.youtube.com/watch?v=OrCgWzpNszk) e [Template Method](https://www.youtube.com/watch?v=j5fGTi8ObK4).

**Exercícios:** E15–E17. **Chefe do mundo:** emitir a notificação somente depois de uma transição válida para pago e rejeitar o envio de um pedido novo. **Revisão:** quem se inscreve; política de falha; máquina versus objetos State; State versus Strategy; etapa fixa versus variável.

### Mundo 8 — completar o catálogo GoF

Você já estudou cinco padrões de criação, quatro estruturais e quatro comportamentais. Abaixo estão os dez restantes. Não é necessário encaixar todos no projeto final: faça pequenos experimentos para entender suas intenções.

#### Estruturais restantes

**Bridge — duas dimensões variam independentemente.** Imagine relatórios simples ou detalhados e saídas de texto ou HTML. Em vez de quatro subclasses combinando tudo, `Relatorio` recebe um `Renderizador`. Esquema: `RelatorioDetalhado → renderizador → HTML ou Texto`. Exemplo de operação: `renderizador.titulo(nome)` e `renderizador.linha(valor)`. Missão E18: acrescentar um renderizador sem alterar os tipos de relatório. Custo: outra colaboração. Diferença para Adapter: Bridge organiza variações do projeto; Adapter compatibiliza uma interface existente.

**Composite — folhas e grupos com a mesma operação.** Uma caixa contém itens ou outras caixas; todos oferecem `preco()`. A caixa soma o preço de seus filhos, enquanto a folha devolve seu próprio preço. Esquema: `Caixa → [Poção, Caixa → [Espada, Escudo]]`. Missão E19: calcular uma caixa aninhada e uma caixa vazia. Custo: decidir quais operações fazem sentido para folhas e grupos; impedir ciclos se a estrutura for uma árvore.

**Flyweight — compartilhar dados repetidos.** Mil peças do jogo podem compartilhar o mesmo modelo visual, enquanto cada posição fica fora dele. Separe estado intrínseco, como textura, do extrínseco, como posição. Missão E20: criar uma fábrica de modelos por tipo e contar quantos modelos existem após criar cem peças. Custo: acesso indireto e risco de compartilhar estado mutável que deveria ser individual. Meça a economia antes de otimizar.

#### Comportamentais restantes

**Chain of Responsibility — passar uma solicitação entre tratadores.** Uma solicitação de desconto passa por regras que podem tratá-la ou encaminhá-la. Esquema: `cliente → regraCupom → regraFidelidade → regraPadrao`. Defina se a primeira regra que responde encerra a cadeia; essa é a política do exercício E21. Se todas precisarem executar, você pode estar modelando um pipeline de outra natureza. Custo: a ordem altera a resposta e uma solicitação pode ficar sem tratamento.

**Command — representar uma solicitação como objeto.** Um comando `AdicionarItem` guarda receptor e argumentos e oferece `executar()`. Uma fila pode guardar comandos sem conhecer seus detalhes. Missão E22: adicionar `desfazer()` e manter histórico em uma pilha. Custo: mais objetos e lógica de reversão. Desfazer uma operação externa não significa simplesmente rodar o código ao contrário: pode exigir uma compensação.

**Iterator — percorrer sem expor a representação.** O cliente usa `for item in colecao` sem saber como os itens são guardados. Em Python, `__iter__` e geradores oferecem mecanismos diretos para esse papel. Missão E23: gerador de produtos abaixo de um limite. `yield` entrega um valor e suspende a função até a próxima solicitação. Custo: o resultado pode ser consumido uma única vez, e mudanças durante a iteração precisam de política.

**Mediator — centralizar interações entre participantes.** Um formulário tem campos, botão e mensagem; o mediador coordena habilitar o botão conforme os campos mudam. Esquema: `CampoNome → Mediador ← CampoEmail; Mediador → Botao`. Missão E24: componentes notificam o mediador, que atualiza a prontidão. Custo: o mediador pode crescer demais. Diferença para Facade: o mediador coordena relações entre participantes; a fachada oferece uma interface simplificada ao cliente.

**Memento — guardar um estado para restaurar depois.** Um editor produz um retrato de seu conteúdo; o histórico conserva esse retrato sem manipular diretamente o interior do editor. Missão E25: guardar duas versões do carrinho e restaurar a primeira. Custo: memória e política de cópia. Command guarda uma ação; Memento guarda um estado. Podem ser combinados, mas não são equivalentes.

**Interpreter — avaliar uma linguagem pequena.** Nós como `Literal`, `Soma` e `Multiplicacao` representam expressões e oferecem `avaliar()`. Esquema: `Soma(Literal(2), Multiplicacao(Literal(3), Literal(4))) → 14`. Missão E26: construir a árvore diretamente, sem usar `eval`. Não é necessário criar um parser nesta missão. Custo: linguagens maiores exigem outras ferramentas; parsing e avaliação são etapas diferentes.

**Visitor — adicionar operações a uma estrutura de tipos.** Itens físicos e digitais recebem visitantes para relatório ou inspeção. Cada item tem `aceitar(visitante)` e chama a operação apropriada, como `visitar_fisico(self)`. Missão E27: relatório e contagem sobre uma coleção de tipos estáveis. Custo: adicionar um novo tipo de elemento pode exigir alterar todos os visitantes. Em Python, funções ou despacho por tipos podem ser mais simples dependendo do contexto.

#### Lista completa para consulta

| Família | Padrões GoF |
|---|---|
| Criação — 5 | Abstract Factory, Builder, Factory Method, Prototype, Singleton |
| Estrutura — 7 | Adapter, Bridge, Composite, Decorator, Facade, Flyweight, Proxy |
| Comportamento — 11 | Chain of Responsibility, Command, Interpreter, Iterator, Mediator, Memento, Observer, State, Strategy, Template Method, Visitor |

Referência do catálogo: [Design Patterns: Elements of Reusable Object-Oriented Software, na editora](https://www.oreilly.com/library/view/design-patterns-elements/0201633612/). As missões e os exemplos da loja são autorais.

**Chefe do mundo:** escolha três padrões pouco familiares, desenhe suas colaborações e resolva as missões correspondentes. Para avançar, explique o problema e uma alternativa simples para cada um dos dez restantes. **Revisão:** família versus intenção; compartilhar estado; ação versus retrato; coleção versus percurso; custo de novos tipos no Visitor.

### Mundo 9 — refatorar com critério

Refatoração altera a organização preservando o comportamento observável acordado. Adicionar uma regra nova é uma mudança funcional. Misturar ambas torna mais difícil entender por que um teste falhou.

Faça este procedimento no checkout:

1. Escreva exemplos de comportamento esperado e testes que os representem.
2. Identifique uma dificuldade concreta: duplicação de construção, regras misturadas ou detalhe externo.
3. Faça a menor extração útil. Uma função nomeada pode ser suficiente.
4. Execute os testes. Corrija antes de continuar.
5. Introduza um padrão se ele melhorar a mudança necessária.
6. Compare: quantos lugares foram editados, o que ficou mais claro e que indireção surgiu?

#### Cartão de decisão

Preencha antes de aplicar qualquer padrão:

```text
Problema observado:
Mudança que preciso suportar agora:
O que permanece estável:
O que varia:
Solução simples considerada:
Padrão candidato e motivo:
Custo e possível falha:
Teste que demonstra o benefício:
```

**Exemplo:** “Há dois provedores com nomes de métodos e unidades diferentes. Meu checkout precisa cobrar em centavos. Posso espalhar traduções ou concentrá-las em adapters. Escolho adapters porque o mesmo contrato atende o checkout e os testes. Custo: testar cada tradução; falha possível: unidade incorreta.”

**Cheiro não é sentença:** um `if` não é necessariamente um problema; repetição de duas linhas pode ser aceitável; mais classes não significam melhor projeto. Meça clareza e dificuldade de mudança no caso concreto.

**Exercício:** E28. **Chefe:** retirar uma abstração desnecessária e demonstrar que o comportamento continua correto. **Revisão:** mudança funcional; teste de caracterização; menor extração; benefício demonstrável; custo de uma indireção.

### Mundo 10 — resiliência e limites reais

Reassista [5 Design Patterns Que Todo Dev Deveria Conhecer](https://www.youtube.com/watch?v=9sI8KHEjs0M) agora: ele reúne Strategy, Observer, Adapter, máquina de estados e retry/circuit breaker. Os dois últimos assuntos não são, como conjunto, entradas do catálogo GoF; máquina de estados é um modelo, e State é um padrão que pode implementá-lo.

#### Retry: tentar de novo com uma política

Uma falha temporária pode desaparecer. Retry repete a operação de forma limitada. Defina **quantas tentativas no total**, quais erros permitem repetir e quanto esperar. Três tentativas totais significam uma inicial e até duas repetições.

```text
tentativa 1 → falhou → espera 1 s
tentativa 2 → falhou → espera 2 s
tentativa 3 → falhou → encerra com erro
```

Backoff aumenta a espera. Jitter adiciona variação aleatória para reduzir tentativas sincronizadas. Um erro permanente, como um pedido inválido, não se torna válido ao repetir. Veja a [documentação de Retry](https://learn.microsoft.com/en-us/azure/architecture/patterns/retry).

#### Circuit breaker: interromper chamadas que tendem a falhar

```mermaid
stateDiagram-v2
    [*] --> Fechado
    Fechado --> Aberto: limiar de falhas
    Aberto --> MeioAberto: prazo de recuperação
    MeioAberto --> Fechado: chamada de teste funciona
    MeioAberto --> Aberto: chamada de teste falha
```

Fechado permite chamadas; aberto rejeita temporariamente; meio aberto deixa passar uma quantidade limitada para avaliar recuperação. O circuito precisa manter estado entre chamadas dentro do escopo escolhido. Criá-lo novamente em cada chamada perderia a memória das falhas. Separe circuitos por dependências que possam falhar independentemente. Referência: [Circuit Breaker](https://learn.microsoft.com/en-us/azure/architecture/patterns/circuit-breaker).

#### Idempotência e efeitos externos

Se uma cobrança demora e o cliente não recebe a resposta, isso não prova que ela não ocorreu. Repetir pode duplicá-la. Uma chave de idempotência identifica a mesma operação lógica; a prevenção de duplicatas precisa funcionar no ponto onde o efeito é registrado. Neste curso, simule a cobrança e mantenha um registro por chave para explorar o problema.

**Concorrência:** duas execuções podem observar um estado antigo e tentar alterá-lo. “Verificar e depois modificar” não é automaticamente uma operação indivisível. Singleton, o GIL ou um dicionário não tornam toda sequência segura. Em sistemas reais, sincronização, transações e restrições de unicidade dependem do recurso usado.

**Testabilidade:** injete uma função de relógio e uma função de espera. Nos testes, avance um relógio falso e registre atrasos; não espere segundos reais. Simule: falha temporária seguida de sucesso, limite esgotado, circuito aberto, recuperação e duplicata da mesma operação.

**Exercícios:** E29–E30. **Chefe:** um serviço falso falha duas vezes e depois responde. Execute com no máximo três tentativas totais; depois simule uma indisponibilidade persistente e confira que o circuito reduz chamadas. **Revisão:** retry versus circuito; tentativas versus repetições; idempotência; escopo do circuito; relógio falso.

### Mundo 11 — a Loja da Guilda completa

#### Requisitos do projeto

Construa uma aplicação de terminal, com operações simuladas e módulos que você consiga explicar:

1. Cadastrar pelo menos três produtos, com preço em centavos.
2. Adicionar itens com quantidades inteiras positivas e calcular subtotal.
3. Cotar frete normal, expresso e retirada; oferecer seguro opcional.
4. Escolher um cobrador simulado através de um contrato; integrar um legado com Adapter.
5. Coordenar a compra através de uma operação de checkout.
6. Validar estados novo, pago, enviado, entregue e cancelado.
7. Publicar uma notificação após pagamento aceito; registrar as mensagens em memória.
8. Simular falhas transitórias num componente separado; demonstrar retry e circuit breaker.
9. Evitar efeito duplicado para a mesma chave de operação na simulação.
10. Documentar duas escolhas de padrão e uma escolha deliberada de solução simples.

```text
Terminal
   ↓
Checkout ── usa ── Pedido e regras de estado
   ├── calculador de frete (Strategy; criação opcional por Factory)
   ├── cobrador (Adapter se necessário)
   └── eventos (Observer em memória)

Seguro envolve frete (Decorator)
Falhas são simuladas em um componente com política de resiliência
```

Não use todos os 23 padrões como requisito. O desafio é escolher os que resolvem problemas concretos e manter a alternativa simples quando ela é adequada.

#### Entregas e avaliação

| Entrega | Evidência | Pontos de qualidade |
|---|---|---:|
| Comportamento | Fluxo comum e erros com resultado explícito | 30 |
| Verificação | Testes de cálculo, estado, tradução e falha | 25 |
| Projeto | Responsabilidades compreensíveis e contratos coerentes | 20 |
| Defesa | Problema, benefício, custo e alternativa por decisão | 15 |
| Uso | Instruções de execução e exemplos reproduzíveis | 10 |

Para concluir o chefe final: pelo menos 80/100 e nenhum caso de cobrança simulada duplicada, transição proibida aceita ou cálculo incorreto entre os cenários definidos. Essa rubrica é separada do XP de prática.

**Roteiro de demonstração:** carrinho de 7.000 + frete normal de 1.400 = 8.400; com seguro = 8.900; retirada = 7.000. Pagar uma vez; tentar pagar novamente com a mesma chave; tentar enviar antes de pagar; provocar falhas transitórias e persistentes. Documente o que cada teste confirma e o que não cobre.

**Mudanças surpresa:** novo cobrador com interface diferente; frete bicicleta; segundo ouvinte; falha de um ouvinte; relatório com nova saída; cache que precisa invalidar. Implemente três e apresente a justificativa.

**Revisão final:** explique Strategy versus State, Adapter versus Facade, Decorator versus Proxy, Factory Method versus Simple Factory e Observer local versus mensageria distribuída.

### Ordem recomendada dos vídeos

Esta é uma ordem pedagógica autoral, diferente da posição atual na playlist:

1. Dicionário do Programador — Mundo 3.
2. SOLID, Clean Code e Design Patterns — Mundo 3; revisitar no 9.
3. Simple Factory — Mundo 4.
4. Strategy — Mundo 5.
5. Adapter — Mundo 6.
6. Facade — Mundo 6.
7. Decorator — Mundo 6.
8. Proxy — Mundo 6, depois de discutir cache.
9. Observer — Mundo 7.
10. State — Mundo 7.
11. Template Method — Mundo 7.
12. Singleton — depois dos contratos e testes; revisitar no 10.
13. Cinco padrões — uma visão geral no Mundo 3, aprofundamento no 10.

Todos os links individuais e a posição da playlist estão em [vídeos e notas](#videos). Você pode assistir a uma visão geral cedo sem ter de entender cada trecho de código imediatamente.

### Diário de progresso

Copie uma linha por sessão:

```text
Data:
Mundo e exercício:
O que previ:
O que aconteceu:
Erro ou dificuldade:
O que consigo explicar agora:
XP novo e evidência:
Revisões previstas: +1, +3, +7 e +14 dias
```

- [ ] Mundo 0: executo e altero o programa.
- [ ] Mundo 1: decomponho cálculos e valido entradas.
- [ ] Mundo 2: uso objetos e troco colaboradores.
- [ ] Mundo 3: explico um problema de manutenção e escrevo testes.
- [ ] Mundo 4: diferencio técnicas de criação.
- [ ] Mundo 5: acrescento uma estratégia sem mudar o consumidor.
- [ ] Mundo 6: diferencio integração, simplificação, extensão e controle.
- [ ] Mundo 7: modelo eventos, estados e etapas.
- [ ] Mundo 8: reconheço os 23 padrões e suas intenções.
- [ ] Mundo 9: refatoro e retiro complexidade desnecessária.
- [ ] Mundo 10: simulo limites, falhas e recuperação.
- [ ] Mundo 11: demonstro o projeto e defendo minhas escolhas.

### Sua primeira missão — comece hoje

Digite o programa do Mundo 0. Antes de executar, escreva o resultado esperado. Depois mude `preco` para 40 e `quantidade` para 3. Explique o resultado 120. Por fim, resolva E01 sem olhar o gabarito. Esse é o primeiro passo; classes e padrões virão depois.

---

<a id="gabarito"></a>

## Parte 3 — Exercícios e gabarito

Use junto à [trilha](#trilha). As respostas são autorais. Tente primeiro, consulte a dica depois e abra o gabarito só ao terminar sua tentativa. Respostas alternativas são válidas quando respeitam o contrato e você consegue explicar seus custos.

### Missões

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

#### Dicas graduais

- E01–E07: escreva a saída esperada no papel; separe dados, cálculo e exibição; não use uma lista de classe para guardar itens de instâncias.
- E08–E11: escreva o contrato que o consumidor espera antes de criar a implementação. Dê nomes e unidades explícitos aos valores.
- E12–E17: registre chamadas numa lista para conferir ordem; defina política de erro e transições antes do código.
- E18–E27: desenhe dois ou três objetos e as setas de colaboração. A intenção importa mais que um nome de classe.
- E28–E30: tenha exemplos que falhem se o comportamento ficar incorreto; use dependências falsas para relógio, espera e serviço.

### Gabarito comentado

#### E01 — atribuir e multiplicar

```python
preco_centavos = 2500
quantidade = 4
total_centavos = preco_centavos * quantidade
print(total_centavos)  # 10000
```

Não some 2.500 + 4: quantidade indica quantas unidades custam 2.500 cada. Explique a diferença antes de avançar.

#### E02 — a fronteira importa

```python
def total_com_frete(subtotal):
    if subtotal < 0:
        raise ValueError("Subtotal inválido")
    frete = 0 if subtotal >= 10000 else 1200
    return subtotal + frete
```

Exatamente 10.000 já tem frete grátis. Usar `>` mudaria a regra nesse limite. Nesta missão, subtotal zero recebe o frete fixo; aceitar um carrinho vazio é uma decisão de negócio separada.

#### E03 — validar o contrato de entrada

```python
def subtotal(preco, quantidade):
    if type(preco) is not int or preco < 0:
        raise ValueError("Preço deve ser um inteiro não negativo")
    if type(quantidade) is not int or quantidade <= 0:
        raise ValueError("Quantidade deve ser um inteiro positivo")
    return preco * quantidade
```

Nesta missão, `type(...) is int` rejeita booleanos: em Python, `bool` é uma subclasse de `int`, mas `True` não é uma quantidade válida no nosso contrato. Preço zero é permitido; quantidade zero não.

#### E04 — acumular itens

```python
def subtotal_itens(itens):
    total = 0
    for preco, quantidade in itens:
        total += subtotal(preco, quantidade)
    return total
```

Use a função E03 no mesmo arquivo. A lista vazia não percorre o laço; o acumulador permanece zero. A versão `sum(subtotal(p, q) for p, q in itens)` é equivalente para esse contrato.

#### E05 — nomes, referências e cópias

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

#### E06 — estado por instância

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

#### E07 — três promessas distintas

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

#### E08 — centralizar seleção

Crie três classes com `calcular(peso)`. Na fábrica, selecione pelo tipo; para retirada, devolva um objeto que retorna zero. Para tipo desconhecido, lance `ValueError`. O [laboratório](04-exemplos/laboratorio_patterns.py) contém uma implementação executável com validação de peso e um dicionário de construtores.

Trocar `if` por dicionário não elimina a decisão: ela passa a estar na tabela. Isso pode melhorar a leitura, mas não torna automaticamente a fábrica extensível sem qualquer mudança.

#### E09 — cinco experimentos e uma análise

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

#### E10 — variar o cálculo

```python
class FreteBicicleta:
    def calcular(self, peso):
        if peso < 0:
            raise ValueError("Peso inválido")
        return 800 + 100 * peso
```

Passe esse objeto ao consumidor do Mundo 5. O novo algoritmo devolve 1.000 para peso 2. Se você adicionou um `if` em `Carrinho.total` para reconhecê-lo, ainda acoplou o consumidor à nova implementação.

#### E11 — tradução de unidade e operação

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

#### E12 — coordenação e falha

Uma fachada recebe colaboradores com `reservar`, `cobrar` e `confirmar`. Execute nessa ordem; registre cada chamada. Se `cobrar` lança uma exceção, `confirmar` não deve ocorrer. Defina uma compensação para a reserva, como `liberar`, e teste que ela ocorre.

Uma ordem plausível no exercício é `reservar → cobrar → confirmar`, com `liberar` após falha de cobrança. Isso não resolve atomicidade entre serviços: uma resposta perdida pode esconder uma cobrança realizada. A missão pede coordenação simulada; os limites precisam estar documentados.

#### E13 — envolver preservando o contrato

`FreteComSeguro` recebe um frete e implementa `calcular(peso)` delegando e somando 500. O consumidor não precisa saber se usa um frete básico ou decorado. Confira que o frete original continua custando 1.400 e o decorado 1.900.

Desafio de ordem: frete-base de 1.000; seguro fixo de 500; taxa de 10%. Aplicar taxa após seguro dá 1.650; seguro após taxa dá 1.600. Defina o arredondamento se usar valores que não resultem em centavos inteiros.

#### E14 — proxy com política explícita

Use um dicionário por identificador. Em `buscar`, consulte a origem apenas se a chave não estiver presente. Ofereça `invalidar(id)` e remova a chave. Registre quantas chamadas chegam à origem. No laboratório, esse exemplo usa valores textuais imutáveis.

Se forem devolvidos objetos mutáveis, o chamador poderá alterar o conteúdo cacheado. Discuta cópia, imutabilidade ou autorização de alteração como parte do contrato. Para dados reais, defina também expiração ou atualização.

#### E15 — inscrição e remoção

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

#### E16 — validar antes de alterar

O mapa de transições do Mundo 7 é suficiente. Faça `novo_estado = transicionar(atual, destino)`; só depois atribua. Uma exceção deixa o estado anterior intacto. Objetos State são uma extensão: delegue operações a uma instância do estado atual. O laboratório contém ambos os mecanismos.

#### E17 — uma sequência, duas leituras

O método base chama `ler`, limpa cada registro e rejeita registros vazios; subclasses apenas escolhem `splitlines` ou `split(',')`. A entrada `" espada , escudo "` deve gerar `['ESPADA', 'ESCUDO']` na versão por vírgulas. `"espada,,escudo"` deve gerar erro, conforme nossa política. Se cada subclasse reimplementar `executar`, a sequência deixou de estar centralizada.

#### E18 — duas dimensões em composição

`RelatorioSimples` e `RelatorioDetalhado` recebem um renderizador. Cada relatório chama operações como `titulo` e `linha`; `Texto` e `HTML` implementam essas operações. Introduzir `Markdown` exige uma nova implementação do renderizador, mantendo os relatórios. Não crie subclasses combinadas como `RelatorioDetalhadoHTML` para cada combinação.

#### E19 — operação uniforme e recursão

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

#### E20 — separar compartilhado de individual

Uma fábrica conserva `modelos[tipo]`; peças conservam posição e referência ao modelo. Alternando dois tipos por cem peças, `len(modelos) == 2`. Alterar a posição de uma peça não muda a posição de outra. Dados do modelo devem ser tratados como imutáveis nesse exercício. Não coloque a posição dentro do modelo compartilhado.

#### E21 — primeira resposta encerra

O tratador de cupom retorna o desconto quando o pedido tem cupom; caso contrário, delega para fidelidade. Fidelidade trata apenas quem atende sua regra; caso contrário, delega para desconto zero. Teste os quatro casos: nenhum, só cupom, só fidelidade, ambos. A regra “primeira aplicável vence” faz ambos usar cupom. Não some descontos se essa não for a política.

#### E22 — ações e histórico

Um comando guarda carrinho, item e informação para remover a adição correspondente. `executar` adiciona; `desfazer` reverte. O controlador guarda comandos executados em pilha e desfaz o último. Guardar somente o valor e remover a primeira ocorrência pode apagar um item anterior igual. Use a posição/identificador apropriado ou uma política que permita apenas desfazer na ordem inversa.

#### E23 — gerador

```python
def abaixo_do_limite(precos, limite):
    for preco in precos:
        if preco < limite:
            yield preco

resultado = list(abaixo_do_limite([1500, 2000, 3500, 800], 2000))
assert resultado == [1500, 800]
```

O preço 2.000 não entra porque a regra usa “abaixo”. Iterar novamente sobre o mesmo gerador já esgotado não reproduz os valores; crie um novo gerador. A lista `resultado` pode ser percorrida repetidamente.

#### E24 — coordenação

Os campos notificam `mediador.alterou()`. O mediador lê ambos e define `botao.habilitado = bool(nome.strip()) and bool(email.strip())`. Nenhum campo manipula diretamente o botão. Essa validação verifica presença, não formato ou existência do endereço de e-mail. Escreva quatro testes para as combinações vazio/preenchido.

#### E25 — retrato independente

Para itens imutáveis, guarde uma tupla em `salvar()` e crie uma lista nova em `restaurar(retrato)`. Para itens mutáveis, defina uma política de cópia adequada. O histórico conserva retratos, não deve editar internamente o carrinho. Verifique que adicionar depois do retrato não altera o retrato anterior.

#### E26 — árvore de expressão

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

#### E27 — operações externas sobre tipos estáveis

`Fisico.aceitar(v)` chama `v.visitar_fisico(self)`; `Digital.aceitar(v)` chama `v.visitar_digital(self)`. Um `VisitanteRelatorio` devolve descrições; um `VisitanteContagem` atualiza contadores por tipo. Use o mesmo conjunto de itens com os dois visitantes. Uma nova operação cria um visitante; um novo tipo de item exige que os visitantes saibam tratá-lo.

#### E28 — comportamento e complexidade

Antes, duas rotas calculam o mesmo subtotal em blocos duplicados. Extraia uma função de cálculo e preserve exemplos com zero itens, um item e múltiplos itens. Se você criou uma classe que apenas repassa o argumento para essa função e não representa outra responsabilidade, experimente removê-la. O gabarito é a preservação das promessas com uma estrutura que você consegue justificar; contar classes não mede qualidade.

#### E29 — repetir apenas falhas permitidas

Crie um serviço que conta chamadas: nas primeiras duas lança `ErroTemporario`, na terceira retorna `ok`. A função de retry captura apenas `ErroTemporario`, limita a três tentativas totais e chama uma função `esperar` com 1 e 2. Injete `atrasos.append` como espera para testar sem dormir. Uma `ValueError` deve propagar na primeira tentativa.

O [laboratório](04-exemplos/laboratorio_patterns.py) implementa essa política e valida o número de tentativas. Jitter é uma extensão: injete também uma fonte aleatória e teste os limites dos atrasos, sem exigir um número aleatório específico.

#### E30 — memória entre chamadas

Com relógio começando em zero, provoque duas falhas temporárias. O circuito abre. Uma terceira chamada é rejeitada e **não incrementa o contador de chamadas do serviço**. Avance o relógio para 10; uma chamada de teste pode passar. Sucesso fecha e zera o contador; falha reabre e reinicia o prazo.

O laboratório implementa uma simulação sequencial. Ela não é uma solução pronta para múltiplas threads/processos. Uma versão concorrente deve controlar atomicamente as chamadas de teste e o estado. Testes com relógio falso verificam a política sem exigir espera real.

### Cinco desafios finais com respostas esperadas

1. **“Um `if` prova código ruim?”** Não. Avalie tamanho, estabilidade, duplicação e mudança necessária.
2. **“Toda Factory é Factory Method?”** Não. Identifique a estrutura do criador e o método redefinível, não apenas o nome.
3. **“Observer torna tudo assíncrono?”** Não. O exemplo local é síncrono e precisa de política de exceção.
4. **“Uma máquina de estados sempre exige classes State?”** Não. Uma tabela pode bastar; objetos State distribuem comportamento.
5. **“Retry pode duplicar um pagamento?”** Pode. Uma falha na resposta não prova ausência de efeito; a operação exige política de idempotência no local apropriado.

### Registro de tentativas

| Data | Exercício | Minha previsão | Resultado | Dificuldade | Próxima revisão |
|---|---|---|---|---|---|
| | | | | | |

Ao pedir ajuda, envie o código, o resultado esperado, o resultado observado e uma frase sobre sua tentativa. Assim podemos corrigir o raciocínio e não apenas substituir sua resposta.
