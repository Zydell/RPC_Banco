import unittest
from unittest.mock import patch     #Herramientas para crear objetos simulados (mocks).
from bank_client import BankClient, main_menu, user_menu

class TestBankClient(unittest.TestCase):

    @patch('xmlrpc.client.ServerProxy') #Verifica que login devuelve True.
    def test_login_success(self, mock_server_proxy):
        client = BankClient('http://localhost:8000')
        mock_server_proxy().authenticate.return_value = True
        self.assertTrue(client.login('test_account', 'test_password', notifications_enabled=False))
        
    @patch('xmlrpc.client.ServerProxy') #Verifica que login devuelve False.
    def test_login_failure(self, mock_server_proxy):
        client = BankClient('http://localhost:8000')
        mock_server_proxy().authenticate.return_value = False
        self.assertFalse(client.login('test_account', 'wrong_password'))

    @patch('xmlrpc.client.ServerProxy') #Verifica que el mensaje devuelto por create_account es el esperado.
    def test_create_account(self, mock_server_proxy):
        client = BankClient('http://localhost:8000')
        mock_server_proxy().create_account.return_value = "Cuenta creada exitosamente."
        self.assertEqual(client.create_account('test_account', 'test_password'), "Cuenta creada exitosamente.")

    def mock_input(self, inputs):   #simular la entrada del usuario en pruebas de menús
        # Crea una función de entrada que devuelve valores del iterador
        it = iter(inputs)
        return lambda _: next(it)

    # Verifica que los mensajes sean los correctos
    @patch('xmlrpc.client.ServerProxy')
    def test_main_menu_create_account(self, mock_server_proxy):
        client = BankClient('http://localhost:8000')
        mock_server_proxy().create_account.return_value = "Cuenta creada exitosamente."
        with patch('builtins.print') as mock_print:
            main_menu(client, self.mock_input(['2', 'test_account', 'test_password', '3']))
            mock_print.assert_any_call("Cuenta creada exitosamente.")

    @patch('xmlrpc.client.ServerProxy')
    def test_main_menu_login_and_logout(self, mock_server_proxy):
        client = BankClient('http://localhost:8000')
        mock_server_proxy().authenticate.return_value = True
        with patch('builtins.print') as mock_print:
            main_menu(client, self.mock_input(['1', 'test_account', 'test_password', '6', '3']))
            mock_print.assert_any_call("Ingreso exitoso.")
            mock_print.assert_any_call("Sesión cerrada.")

    @patch('xmlrpc.client.ServerProxy')
    def test_user_menu_deposit(self, mock_server_proxy):
        client = BankClient('http://localhost:8000')
        client.current_account = 'test_account'
        mock_server_proxy().deposit.return_value = "Depósito exitoso."
        with patch('builtins.print') as mock_print:
            user_menu(client, self.mock_input(['2', '100', '6']))
            mock_print.assert_any_call("Depósito exitoso.")

    @patch('xmlrpc.client.ServerProxy')
    def test_user_menu_withdraw(self, mock_server_proxy):
        client = BankClient('http://localhost:8000')
        client.current_account = 'test_account'
        mock_server_proxy().withdraw.return_value = "Retiro exitoso."
        with patch('builtins.print') as mock_print:
            user_menu(client, self.mock_input(['3', '100', '6']))
            mock_print.assert_any_call("Retiro exitoso.")

    @patch('xmlrpc.client.ServerProxy')
    def test_user_menu_transfer(self, mock_server_proxy):
        client = BankClient('http://localhost:8000')
        client.current_account = 'test_account'
        mock_server_proxy().transfer.return_value = "Transferencia exitosa."
        with patch('builtins.print') as mock_print:
            user_menu(client, self.mock_input(['4', 'another_account', '50', '6']))
            mock_print.assert_any_call("Transferencia exitosa.")

    @patch('xmlrpc.client.ServerProxy')
    def test_user_menu_transaction_history(self, mock_server_proxy):
        client = BankClient('http://localhost:8000')
        client.current_account = 'test_account'
        mock_server_proxy().get_transaction_history.return_value = ["Transacción 1", "Transacción 2"]
        with patch('builtins.print') as mock_print:
            user_menu(client, self.mock_input(['5', '6']))
            mock_print.assert_any_call("Historial de transacciones:")
            mock_print.assert_any_call("Transacción 1")
            mock_print.assert_any_call("Transacción 2")

if __name__ == '__main__':
    unittest.main()
