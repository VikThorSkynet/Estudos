# Como executar o laboratório

Estude primeiro lógica, funções, objetos e testes nos Mundos 0–3 da [trilha](../02-trilha/trilha.md). Depois execute estes exemplos para observar as colaborações entre padrões.

## Execute a demonstração

Na raiz do repositório:

```text
python "Design Patterns/04-exemplos/laboratorio_patterns.py"
```

Resultados de referência: subtotal 7.000 centavos, total com frete normal 8.400, com seguro 8.900 e com retirada 7.000. A demonstração também mostra estado do pedido, notificação, cache, retry, circuito e cobrança simulada idempotente.

## Execute os testes

```text
python -m unittest discover -s "Design Patterns/04-exemplos" -p "test_*.py" -v
```

Os 19 testes verificam cálculo e validação, criação, tradução de centavos para reais, independência de pedidos, pagamento e falhas, transições, ouvintes, cache, importação, tentativas, circuito e idempotência simulada. Na preparação, passaram em Python 3.14. Não há dependências externas para instalar.

## O que ler no código

| Assunto | Símbolo principal |
|---|---|
| Validação e função | `inteiro`, `subtotal` |
| Simple Factory | `criar_frete` |
| Strategy | `total_com_frete`, classes de frete |
| Decorator | `FreteComSeguro` |
| Factory Method | `Entrega`, `EntregaNormal` |
| Adapter | `AdapterPagamento` |
| Observer | `Eventos` |
| Máquina de estados por tabela | `TRANSICOES`, `transicionar`, `Pedido` |
| State por objetos | `EstadoPedido`, `PedidoComState` |
| Facade | `Checkout` |
| Proxy | `ProxyCatalogo` |
| Template Method | `Importador` |
| Retry | `com_retry` |
| Circuit breaker | `CircuitBreaker`, `RelogioFalso` |
| Idempotência simulada | `CobradorIdempotenteSimulado` |

## Limites dos exemplos

Os serviços são simulados e os dados ficam em memória. O circuito e o registro de idempotência trabalham sequencialmente; não garantem atomicidade entre threads/processos nem persistência. O cache tem invalidação explícita e não expira sozinho.

Observer é local e síncrono. Se um ouvinte falhar depois do pagamento simulado, o estado pago e o efeito permanecem; o exemplo não desfaz a cobrança automaticamente. O teste correspondente explicita esse comportamento.

Esse laboratório não é o projeto final pronto. Construa sua versão seguindo os [requisitos do projeto](../05-projeto-final/README.md).

## Uma mudança para praticar

Crie um frete bicicleta de 800 + 100 × peso. Use-o no consumidor sem alterar `total_com_frete`. Preveja o total para subtotal 7.000 e peso 2: 8.000. Escreva um teste que confirme essa promessa.
