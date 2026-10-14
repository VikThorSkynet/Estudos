"""Laboratório autoral da trilha Design Patterns em Python.

Python 3.10+; biblioteca padrão; execute: python laboratorio_patterns.py
O código simula serviços. O circuito é sequencial, sem segurança entre threads.
"""
from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from decimal import Decimal


def inteiro(valor, nome, minimo=0):
    if type(valor) is not int or valor < minimo:
        raise ValueError(f"{nome} deve ser inteiro e >= {minimo}")
    return valor


def subtotal(preco_centavos, quantidade):
    return inteiro(preco_centavos, "Preço") * inteiro(quantidade, "Quantidade", 1)


class FreteNormal:
    def calcular(self, peso):
        return 1000 + 200 * inteiro(peso, "Peso")


class FreteExpresso:
    def calcular(self, peso):
        return 2000 + 400 * inteiro(peso, "Peso")


class Retirada:
    def calcular(self, peso):
        inteiro(peso, "Peso")
        return 0


# Simple Factory: uma seleção centralizada, que ainda muda com novos tipos.
def criar_frete(tipo):
    construtores = {"normal": FreteNormal, "expresso": FreteExpresso, "retirada": Retirada}
    if tipo not in construtores:
        raise ValueError("Frete desconhecido")
    return construtores[tipo]()


# Strategy: o consumidor recebe uma colaboração com calcular(peso).
def total_com_frete(subtotal_centavos, peso, frete):
    inteiro(subtotal_centavos, "Subtotal")
    return subtotal_centavos + frete.calcular(peso)


# Decorator: acrescenta comportamento mantendo calcular(peso).
class FreteComSeguro:
    def __init__(self, base):
        self.base = base

    def calcular(self, peso):
        return self.base.calcular(peso) + 500


# Factory Method: a operação do criador usa um método redefinível.
class Entrega(ABC):
    @abstractmethod
    def criar_frete(self):
        pass

    def cotar(self, peso):
        return self.criar_frete().calcular(peso)


class EntregaNormal(Entrega):
    def criar_frete(self):
        return FreteNormal()


# Adapter: simulação de uma interface legada com outra unidade.
class ProvedorLegado:
    def __init__(self):
        self.valores = []

    def pagar(self, reais):
        self.valores.append(reais)
        return f"simulado-{len(self.valores)}"


class AdapterPagamento:
    def __init__(self, legado):
        self.legado = legado

    def cobrar(self, centavos):
        inteiro(centavos, "Cobrança", 1)
        return self.legado.pagar(Decimal(centavos) / Decimal(100))


# Observer: local e síncrono; interrompe na primeira exceção do ouvinte.
class Eventos:
    def __init__(self):
        self._ouvintes = []

    def inscrever(self, ouvinte):
        if ouvinte not in self._ouvintes:
            self._ouvintes.append(ouvinte)

    def remover(self, ouvinte):
        self._ouvintes.remove(ouvinte)

    def publicar(self, evento):
        for ouvinte in tuple(self._ouvintes):
            ouvinte(evento)


# Máquina de estados por tabela. Isso não é, sozinho, objetos GoF State.
TRANSICOES = {
    "novo": {"pago", "cancelado"},
    "pago": {"enviado"},
    "enviado": {"entregue"},
    "entregue": set(),
    "cancelado": set(),
}


def transicionar(atual, destino):
    if atual not in TRANSICOES or destino not in TRANSICOES[atual]:
        raise ValueError("Transição proibida")
    return destino


class Pedido:
    def __init__(self, codigo):
        self.codigo = codigo
        self._itens = []
        self.estado = "novo"

    def adicionar(self, preco, quantidade):
        if self.estado != "novo":
            raise ValueError("Pedido não pode mais receber itens")
        subtotal(preco, quantidade)
        self._itens.append((preco, quantidade))

    def subtotal(self):
        return sum(subtotal(p, q) for p, q in self._itens)

    def mudar_estado(self, destino):
        self.estado = transicionar(self.estado, destino)


# State por objetos: exemplo separado da tabela para comparar estruturas.
class EstadoPedido:
    nome = "indefinido"

    def pagar(self, pedido):
        raise ValueError("Não é possível pagar neste estado")

    def enviar(self, pedido):
        raise ValueError("Não é possível enviar neste estado")


class Novo(EstadoPedido):
    nome = "novo"

    def pagar(self, pedido):
        pedido.estado = Pago()


class Pago(EstadoPedido):
    nome = "pago"

    def enviar(self, pedido):
        pedido.estado = Enviado()


class Enviado(EstadoPedido):
    nome = "enviado"


class PedidoComState:
    def __init__(self):
        self.estado = Novo()

    def pagar(self):
        self.estado.pagar(self)

    def enviar(self):
        self.estado.enviar(self)


@dataclass(frozen=True)
class EventoPago:
    codigo: str
    total_centavos: int


# Facade: coordena um caso de uso. Sem garantias distribuídas ou persistência.
class Checkout:
    def __init__(self, cobrador, eventos):
        self.cobrador = cobrador
        self.eventos = eventos

    def finalizar(self, pedido, peso, frete):
        if pedido.estado != "novo" or not pedido._itens:
            raise ValueError("Pedido não está pronto para pagamento")
        total = total_com_frete(pedido.subtotal(), peso, frete)
        recibo = self.cobrador.cobrar(total)
        pedido.mudar_estado("pago")
        # Falha do ouvinte ocorre depois do efeito e da mudança de estado.
        self.eventos.publicar(EventoPago(pedido.codigo, total))
        return recibo, total


# Proxy: valores imutáveis; invalidação explícita, sem prazo automático.
class CatalogoReal:
    def __init__(self):
        self.chamadas = 0

    def buscar(self, codigo):
        self.chamadas += 1
        return f"Item {codigo}"


class ProxyCatalogo:
    def __init__(self, origem):
        self.origem = origem
        self.cache = {}

    def buscar(self, codigo):
        if codigo not in self.cache:
            self.cache[codigo] = self.origem.buscar(codigo)
        return self.cache[codigo]

    def invalidar(self, codigo):
        self.cache.pop(codigo, None)


# Template Method: sequência estável; leitura específica em subclasses.
class Importador(ABC):
    def executar(self, texto):
        registros = [r.strip() for r in self.ler(texto)]
        if not registros or any(not r for r in registros):
            raise ValueError("Registros vazios")
        return [r.upper() for r in registros]

    @abstractmethod
    def ler(self, texto):
        pass


class ImportadorLinhas(Importador):
    def ler(self, texto):
        return texto.splitlines()


class ImportadorVirgulas(Importador):
    def ler(self, texto):
        return texto.split(",")


class ErroTemporario(Exception):
    pass


class CircuitoAberto(Exception):
    pass


def com_retry(operacao, esperar, tentativas=3):
    inteiro(tentativas, "Tentativas", 1)
    for indice in range(tentativas):
        try:
            return operacao()
        except ErroTemporario:
            if indice == tentativas - 1:
                raise
            esperar(2 ** indice)


# Política didática: falhas temporárias consecutivas; teste único sequencial.
class CircuitBreaker:
    def __init__(self, relogio, limiar=2, pausa=10):
        inteiro(limiar, "Limiar", 1)
        inteiro(pausa, "Pausa", 1)
        self.relogio = relogio
        self.limiar = limiar
        self.pausa = pausa
        self.estado = "fechado"
        self.falhas = 0
        self.aberto_em = None

    def chamar(self, operacao):
        if self.estado == "aberto":
            if self.relogio() - self.aberto_em < self.pausa:
                raise CircuitoAberto("Chamada bloqueada temporariamente")
            self.estado = "meio_aberto"
        em_teste = self.estado == "meio_aberto"
        try:
            resultado = operacao()
        except ErroTemporario:
            self.falhas += 1
            if em_teste or self.falhas >= self.limiar:
                self.estado = "aberto"
                self.aberto_em = self.relogio()
            raise
        except Exception:
            # Outros erros propagam; não contam como indisponibilidade aqui.
            # Em meio aberto, o circuito volta a aguardar uma nova avaliação.
            if em_teste:
                self.estado = "aberto"
                self.aberto_em = self.relogio()
            else:
                self.falhas = 0
            raise
        self.estado = "fechado"
        self.falhas = 0
        self.aberto_em = None
        return resultado


class RelogioFalso:
    def __init__(self):
        self.agora = 0

    def __call__(self):
        return self.agora

    def avancar(self, segundos):
        self.agora += inteiro(segundos, "Avanço")


class CobradorIdempotenteSimulado:
    """Registro em memória. Sem persistência nem atomicidade concorrente."""
    def __init__(self):
        self.registros = {}
        self.efeitos = []

    def cobrar(self, chave, centavos):
        if not isinstance(chave, str) or not chave.strip():
            raise ValueError("Chave obrigatória")
        inteiro(centavos, "Cobrança", 1)
        if chave in self.registros:
            valor, recibo = self.registros[chave]
            if valor != centavos:
                raise ValueError("Mesma chave com outro valor")
            return recibo
        recibo = f"simulado-{len(self.efeitos) + 1}"
        self.efeitos.append(centavos)
        self.registros[chave] = (centavos, recibo)
        return recibo


def demonstrar():
    print("Loja da Guilda — exemplos simulados")
    print("Subtotal:", subtotal(3500, 2))
    print("Normal:", total_com_frete(7000, 2, criar_frete("normal")))
    print("Com seguro:", total_com_frete(7000, 2, FreteComSeguro(FreteNormal())))
    print("Retirada:", total_com_frete(7000, 2, Retirada()))
    print("Factory Method:", EntregaNormal().cotar(2))
    notificacoes = []
    eventos = Eventos()
    eventos.inscrever(notificacoes.append)
    legado = ProvedorLegado()
    pedido = Pedido("P-001")
    pedido.adicionar(3500, 2)
    checkout = Checkout(AdapterPagamento(legado), eventos)
    print("Checkout:", checkout.finalizar(pedido, 2, FreteNormal()))
    print("Estado:", pedido.estado)
    print("Notificação:", notificacoes[0])
    print("Valor no legado:", legado.valores[0])
    p = PedidoComState()
    p.pagar()
    p.enviar()
    print("Objetos State:", p.estado.nome)
    origem = CatalogoReal()
    proxy = ProxyCatalogo(origem)
    proxy.buscar("A")
    proxy.buscar("A")
    print("Chamadas à origem após duas buscas:", origem.chamadas)
    print("Template Method:", ImportadorVirgulas().executar("espada, escudo"))
    chamadas = []
    atrasos = []

    def instavel():
        chamadas.append(1)
        if len(chamadas) < 3:
            raise ErroTemporario("Falha simulada")
        return "ok"

    print("Retry:", com_retry(instavel, atrasos.append), "atrasos:", atrasos)
    relogio = RelogioFalso()
    circuito = CircuitBreaker(relogio)

    def indisponivel():
        raise ErroTemporario("Indisponível")

    for _ in range(2):
        try:
            circuito.chamar(indisponivel)
        except ErroTemporario:
            pass
    print("Circuit breaker:", circuito.estado)
    try:
        circuito.chamar(lambda: "não deve executar")
    except CircuitoAberto:
        print("Chamada bloqueada antes de chegar ao serviço")
    relogio.avancar(10)
    print("Recuperação:", circuito.chamar(lambda: "ok"), circuito.estado)
    cobrador = CobradorIdempotenteSimulado()
    primeiro = cobrador.cobrar("op-1", 8400)
    segundo = cobrador.cobrar("op-1", 8400)
    print("Idempotência:", primeiro, segundo, "efeitos:", len(cobrador.efeitos))


if __name__ == "__main__":
    demonstrar()
