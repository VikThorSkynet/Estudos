import sys
from pathlib import Path
import unittest
from decimal import Decimal

sys.path.insert(0, str(Path(__file__).resolve().parent))
import laboratorio_patterns as p


class LaboratorioTests(unittest.TestCase):
    def test_subtotal_contract(self):
        self.assertEqual(p.subtotal(3500, 2), 7000)
        self.assertEqual(p.subtotal(0, 2), 0)
        for preco, quantidade in [(3500, 0), (-1, 2), (3500, 1.5), (True, 2)]:
            with self.subTest(preco=preco, quantidade=quantidade):
                with self.assertRaises(ValueError):
                    p.subtotal(preco, quantidade)

    def test_factory_strategy_decorator(self):
        self.assertEqual(p.total_com_frete(7000, 2, p.criar_frete('normal')), 8400)
        self.assertEqual(p.total_com_frete(7000, 2, p.criar_frete('expresso')), 9800)
        self.assertEqual(p.total_com_frete(7000, 2, p.criar_frete('retirada')), 7000)
        self.assertEqual(p.FreteComSeguro(p.FreteNormal()).calcular(2), 1900)
        with self.assertRaises(ValueError):
            p.criar_frete('desconhecido')
        with self.assertRaises(ValueError):
            p.Retirada().calcular(-1)

    def test_factory_method(self):
        self.assertEqual(p.EntregaNormal().cotar(2), 1400)
        with self.assertRaises(TypeError):
            p.Entrega()

    def test_adapter_units(self):
        legado = p.ProvedorLegado()
        p.AdapterPagamento(legado).cobrar(12345)
        self.assertEqual(legado.valores, [Decimal('123.45')])

    def test_instance_isolation(self):
        a, b = p.Pedido('a'), p.Pedido('b')
        a.adicionar(100, 2)
        self.assertEqual(a.subtotal(), 200)
        self.assertEqual(b.subtotal(), 0)
        with self.assertRaises(ValueError):
            a.adicionar(100, 0)
        self.assertEqual(a.subtotal(), 200)

    def test_checkout_and_repeat_blocked(self):
        legado, eventos, notices = p.ProvedorLegado(), p.Eventos(), []
        eventos.inscrever(notices.append)
        pedido = p.Pedido('P-1')
        pedido.adicionar(3500, 2)
        checkout = p.Checkout(p.AdapterPagamento(legado), eventos)
        self.assertEqual(checkout.finalizar(pedido, 2, p.FreteNormal())[1], 8400)
        self.assertEqual(notices, [p.EventoPago('P-1', 8400)])
        self.assertEqual(pedido.estado, 'pago')
        with self.assertRaises(ValueError):
            checkout.finalizar(pedido, 2, p.FreteNormal())
        self.assertEqual(len(legado.valores), 1)
        with self.assertRaises(ValueError):
            pedido.adicionar(100, 1)

    def test_checkout_payment_failure_no_event(self):
        class Falha:
            def cobrar(self, valor):
                raise p.ErroTemporario()
        pedido, eventos, notices = p.Pedido('P-2'), p.Eventos(), []
        pedido.adicionar(100, 1)
        eventos.inscrever(notices.append)
        with self.assertRaises(p.ErroTemporario):
            p.Checkout(Falha(), eventos).finalizar(pedido, 0, p.Retirada())
        self.assertEqual(pedido.estado, 'novo')
        self.assertEqual(notices, [])

    def test_observer_failure_does_not_undo_payment(self):
        def fail(evento):
            raise ValueError('Ouvinte falhou')
        pedido, eventos, legado = p.Pedido('P-3'), p.Eventos(), p.ProvedorLegado()
        pedido.adicionar(100, 1)
        eventos.inscrever(fail)
        with self.assertRaises(ValueError):
            p.Checkout(p.AdapterPagamento(legado), eventos).finalizar(pedido, 0, p.Retirada())
        self.assertEqual(pedido.estado, 'pago')
        self.assertEqual(len(legado.valores), 1)

    def test_state_table_rejects_without_mutation(self):
        pedido = p.Pedido('state')
        with self.assertRaises(ValueError):
            pedido.mudar_estado('enviado')
        self.assertEqual(pedido.estado, 'novo')
        for state in ['pago', 'enviado', 'entregue']:
            pedido.mudar_estado(state)
        with self.assertRaises(ValueError):
            pedido.mudar_estado('pago')

    def test_state_objects(self):
        pedido = p.PedidoComState()
        with self.assertRaises(ValueError):
            pedido.enviar()
        pedido.pagar()
        pedido.enviar()
        self.assertEqual(pedido.estado.nome, 'enviado')
        with self.assertRaises(ValueError):
            pedido.pagar()

    def test_observer_remove_and_duplicate(self):
        eventos, a, b = p.Eventos(), [], []
        one, two = a.append, b.append
        eventos.inscrever(one)
        eventos.inscrever(one)
        eventos.inscrever(two)
        eventos.publicar('primeiro')
        eventos.remover(one)
        eventos.publicar('segundo')
        self.assertEqual(a, ['primeiro'])
        self.assertEqual(b, ['primeiro', 'segundo'])

    def test_proxy_invalidation(self):
        real = p.CatalogoReal()
        proxy = p.ProxyCatalogo(real)
        self.assertEqual(proxy.buscar('A'), proxy.buscar('A'))
        self.assertEqual(real.chamadas, 1)
        proxy.invalidar('A')
        proxy.buscar('A')
        self.assertEqual(real.chamadas, 2)

    def test_template_method(self):
        self.assertEqual(p.ImportadorLinhas().executar(' espada\nescudo '), ['ESPADA', 'ESCUDO'])
        self.assertEqual(p.ImportadorVirgulas().executar(' espada,escudo '), ['ESPADA', 'ESCUDO'])
        for texto in ['', 'espada,,escudo']:
            with self.assertRaises(ValueError):
                p.ImportadorVirgulas().executar(texto)

    def test_retry_success_delays(self):
        calls, delays = [], []
        def operation():
            calls.append(1)
            if len(calls) < 3:
                raise p.ErroTemporario()
            return 'ok'
        self.assertEqual(p.com_retry(operation, delays.append), 'ok')
        self.assertEqual(len(calls), 3)
        self.assertEqual(delays, [1, 2])

    def test_retry_exhaustion(self):
        calls, delays = [], []
        def operation():
            calls.append(1)
            raise p.ErroTemporario()
        with self.assertRaises(p.ErroTemporario):
            p.com_retry(operation, delays.append)
        self.assertEqual(len(calls), 3)
        self.assertEqual(delays, [1, 2])

    def test_retry_permanent_error_and_bad_configuration(self):
        calls, delays = [], []
        def operation():
            calls.append(1)
            raise ValueError()
        with self.assertRaises(ValueError):
            p.com_retry(operation, delays.append)
        self.assertEqual(len(calls), 1)
        self.assertEqual(delays, [])
        with self.assertRaises(ValueError):
            p.com_retry(lambda: 1, delays.append, 0)

    def test_circuit_open_recovery(self):
        clock, calls = p.RelogioFalso(), []
        cb = p.CircuitBreaker(clock)
        def fail():
            calls.append(1)
            raise p.ErroTemporario()
        for _ in range(2):
            with self.assertRaises(p.ErroTemporario):
                cb.chamar(fail)
        with self.assertRaises(p.CircuitoAberto):
            cb.chamar(fail)
        self.assertEqual(len(calls), 2)
        clock.avancar(9)
        with self.assertRaises(p.CircuitoAberto):
            cb.chamar(fail)
        clock.avancar(1)
        self.assertEqual(cb.chamar(lambda: 'ok'), 'ok')
        self.assertEqual(cb.estado, 'fechado')
        self.assertEqual(cb.falhas, 0)

    def test_half_open_failure_reopens(self):
        clock = p.RelogioFalso()
        cb = p.CircuitBreaker(clock)
        def fail():
            raise p.ErroTemporario()
        for _ in range(2):
            with self.assertRaises(p.ErroTemporario):
                cb.chamar(fail)
        clock.avancar(10)
        with self.assertRaises(p.ErroTemporario):
            cb.chamar(fail)
        self.assertEqual(cb.estado, 'aberto')
        self.assertEqual(cb.aberto_em, 10)
        with self.assertRaises(p.CircuitoAberto):
            cb.chamar(lambda: 'ok')

    def test_idempotent_effect_and_conflict(self):
        cobrador = p.CobradorIdempotenteSimulado()
        self.assertEqual(cobrador.cobrar('one', 8400), cobrador.cobrar('one', 8400))
        self.assertEqual(cobrador.efeitos, [8400])
        with self.assertRaises(ValueError):
            cobrador.cobrar('one', 8500)
        self.assertEqual(cobrador.efeitos, [8400])


if __name__ == '__main__':
    unittest.main()
