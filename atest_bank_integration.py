import unittest
from bank_client import BankClient
from bank_server import BankServer
import threading
import time
from xmlrpc.server import SimpleXMLRPCServer

class TestBankIntegration(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.server = BankServer()
        cls.server_thread = threading.Thread(target=cls.run_server)
        cls.server_thread.start()
        time.sleep(1)  # Esperar un momento para que el servidor se inicie

    @classmethod
    def tearDownClass(cls):
        cls.stop_server()
        cls.server_thread.join()

    @classmethod
    def run_server(cls):
        cls.rpc_server = SimpleXMLRPCServer(('localhost', 8000), allow_none=True)
        cls.rpc_server.register_instance(cls.server)
        cls.rpc_server.serve_forever()

    @classmethod
    def stop_server(cls):
        cls.rpc_server.shutdown()

    def setUp(self):
        self.client = BankClient('http://localhost:8000')
        self.reset_server_state()

    def reset_server_state(self):
        self.server.accounts.clear()
        self.server.credentials.clear()
        self.server.transaction_history.clear()
        self.server.notifications.clear()

    def test_create_account_and_login(self):
        print("Iniciando test_create_account_and_login")
        response = self.client.create_account("test_account", "password")
        self.assertEqual(response, "Cuenta creada exitosamente.")
        login = self.client.login("test_account", "password", notifications_enabled=False)
        self.assertTrue(login)
        self.client.logout()

    def test_deposit_and_balance(self):
        print("Iniciando test_deposit_and_balance")
        self.client.create_account("test_account", "password")
        self.client.login("test_account", "password", notifications_enabled=False)
        self.client.deposit(200)
        balance = self.client.get_balance()
        self.assertEqual(balance, 200)
        self.client.logout()

    def test_withdraw_and_balance(self):
        print("Iniciando test_withdraw_and_balance")
        self.client.create_account("test_account", "password")
        self.client.login("test_account", "password", notifications_enabled=False)
        self.client.deposit(300)
        self.client.withdraw(150)
        balance = self.client.get_balance()
        self.assertEqual(balance, 150)  # Saldo esperado después del retiro
        self.client.logout()

    def test_transfer_and_balance(self):
        print("Iniciando test_transfer_and_balance")
        self.client.create_account("account1", "password")
        self.client.create_account("account2", "password")
        self.client.login("account1", "password", notifications_enabled=False)
        self.client.deposit(300)
        self.client.transfer("account2", 100)
        balance1 = self.client.get_balance()
        self.client.logout()
        
        self.client.login("account2", "password", notifications_enabled=False)
        balance2 = self.client.get_balance()
        self.client.logout()
        
        self.assertEqual(balance1, 200)
        self.assertEqual(balance2, 100)

    def test_notifications(self):
        print("Iniciando test_notifications")
        self.client.create_account("account1", "password")
        self.client.create_account("account2", "password")
        self.client.login("account1", "password", notifications_enabled=True)
        self.client.deposit(300)
        self.client.transfer("account2", 100)
        self.client.logout()

        self.client.login("account2", "password", notifications_enabled=True)
        time.sleep(6)  # Esperar para asegurarse de que las notificaciones sean recibidas
        notifications = self.client.get_notifications()
        #print(f"Notificaciones recibidas: {notifications}")
        for notification in notifications:
                print(f"Notificación: {notification}")
        #self.assertIn("Transferencia recibida de account1: 100", notifications)
        self.client.logout()


if __name__ == '__main__':
    unittest.main()

