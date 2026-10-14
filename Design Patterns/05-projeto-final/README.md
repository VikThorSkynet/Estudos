# Projeto final —  a Loja da Guilda completa

### Requisitos do projeto

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

### Entregas e avaliação

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


## Onde guardar sua implementação

Crie `minha-loja/` nesta pasta para suas próprias soluções. Comece por produtos e carrinho; depois adicione fretes, cobradores simulados, estados e eventos. Faça uma mudança por vez e verifique o comportamento antes da próxima.

Consulte o [laboratório](../04-exemplos/README.md) para experimentar ideias, sem precisar repetir a mesma organização. Registre as decisões e os testes no README da sua implementação.

Use o [diário de progresso](../07-progresso/PROGRESSO.md) para acompanhar as entregas.
