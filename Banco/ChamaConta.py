from Banco.Conta import Conta

conta1 = Conta(1, 123, 'Joao', 0)
conta2 = Conta(3, 456, 'Maria', 0)

conta1.depositar(200)
conta2.depositar(300)
print(conta1.saldo)
print(conta2.saldo)
