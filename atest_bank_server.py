import unittest
from bank_server import BankServer

class TestBankServer(unittest.TestCase):
    def setUp(self):
        self.server = BankServer()

    #Verifica que el mensaje de respuesta sea correcto y quese haya agregado a los diccionarios correspondientes.
    def test_create_account(self):  
        response = self.server.create_account("test_account", "password")
        self.assertEqual(response, "Cuenta creada exitosamente.")
        self.assertIn("test_account", self.server.accounts)
        self.assertIn("test_account", self.server.credentials)
        self.assertIn("test_account", self.server.transaction_history)

    def test_create_account_existing(self):
        self.server.create_account("test_account", "password")
        response = self.server.create_account("test_account", "password")
        self.assertEqual(response, "La cuenta ya existe.")

    def test_authenticate(self):
        self.server.create_account("test_account", "password")
        response = self.server.authenticate("test_account", "password")
        self.assertTrue(response)

    def test_authenticate_wrong_password(self):
        self.server.create_account("test_account", "password")
        response = self.server.authenticate("test_account", "wrong_password")
        self.assertFalse(response)

    def test_authenticate_nonexistent_account(self):
        response = self.server.authenticate("nonexistent_account", "password")
        self.assertFalse(response)

    def test_get_balance(self):
        self.server.create_account("test_account", "password")
        response = self.server.get_balance("test_account")
        self.assertEqual(response, 0)

    def test_get_balance_nonexistent_account(self):
        response = self.server.get_balance("nonexistent_account")
        self.assertEqual(response, "La cuenta no existe.")

    def test_deposit(self):
        self.server.create_account("test_account", "password")
        response = self.server.deposit("test_account", 500)
        self.assertEqual(response, "Depósito de 500 en la cuenta test_account. Nuevo saldo es 500.")
        self.assertEqual(self.server.accounts["test_account"], 500)

    def test_deposit_negative_amount(self):
        self.server.create_account("test_account", "password")
        response = self.server.deposit("test_account", -500)
        self.assertEqual(response, "La cantidad a depositar debe ser positiva.")

    def test_deposit_nonexistent_account(self):
        response = self.server.deposit("nonexistent_account", 500)
        self.assertEqual(response, "La cuenta no existe.")

    def test_withdraw(self):
        self.server.create_account("test_account", "password")
        self.server.deposit("test_account", 500)
        response = self.server.withdraw("test_account", 200)
        self.assertEqual(response, "Retiro de 200 de la cuenta test_account. Nuevo saldo es 300.")
        self.assertEqual(self.server.accounts["test_account"], 300)

    def test_withdraw_insufficient_funds(self):
        self.server.create_account("test_account", "password")
        response = self.server.withdraw("test_account", 200)
        self.assertEqual(response, "Fondos insuficientes.")

    def test_withdraw_negative_amount(self):
        self.server.create_account("test_account", "password")
        response = self.server.withdraw("test_account", -200)
        self.assertEqual(response, "La cantidad a retirar debe ser positiva.")

    def test_withdraw_nonexistent_account(self):
        response = self.server.withdraw("nonexistent_account", 200)
        self.assertEqual(response, "La cuenta no existe.")

    def test_transfer(self):
        self.server.create_account("from_account", "password")
        self.server.create_account("to_account", "password")
        self.server.deposit("from_account", 500)
        response = self.server.transfer("from_account", "to_account", 300)
        self.assertEqual(response, "Transferencia de 300 desde la cuenta from_account a la cuenta to_account. Nuevos saldos: from_account: 200, to_account: 300.")
        self.assertEqual(self.server.accounts["from_account"], 200)
        self.assertEqual(self.server.accounts["to_account"], 300)

    def test_transfer_insufficient_funds(self):
        self.server.create_account("from_account", "password")
        self.server.create_account("to_account", "password")
        response = self.server.transfer("from_account", "to_account", 300)
        self.assertEqual(response, "Fondos insuficientes.")

    def test_transfer_nonexistent_account(self):
        self.server.create_account("from_account", "password")
        response = self.server.transfer("from_account", "nonexistent_account", 300)
        self.assertEqual(response, "Una o ambas cuentas no existen.")

    def test_get_transaction_history(self):
        self.server.create_account("test_account", "password")
        self.server.deposit("test_account", 1000)
        self.server.withdraw("test_account", 200)
        response = self.server.get_transaction_history("test_account")
        self.assertEqual(response, ["Depósito: 1000", "Retiro: 200"])

    def test_get_transaction_history_nonexistent_account(self):
        response = self.server.get_transaction_history("nonexistent_account")
        self.assertEqual(response, "La cuenta no existe.")

    def test_get_notifications(self):   #verfica que no haya notificaciones en una nueva cuenta
        self.server.create_account("test_account", "password")
        self.server.notifications["test_account"].put("Test notification")
        response = self.server.get_notifications("test_account")
        self.assertEqual(response, ["Test notification"])

    def test_get_notifications_empty(self): #verfica que no haya notificaciones en una nueva cuenta
        self.server.create_account("test_account", "password")
        response = self.server.get_notifications("test_account")
        self.assertEqual(response, [])

    def test_get_notifications_nonexistent_account(self):
        response = self.server.get_notifications("nonexistent_account")
        self.assertEqual(response, [])

if __name__ == '__main__':
    unittest.main()

