import pytest
import threading
from bank_client import BankClient, main
from bank_server import run_server
import time
import logging
from unittest.mock import patch

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
logger = logging.getLogger(__name__)

def start_server():
    run_server()

@pytest.fixture(scope="module")
def server():
    logger.info("Iniciando el servidor...")
    server_thread = threading.Thread(target=start_server)
    server_thread.daemon = True
    server_thread.start()
    time.sleep(1)
    logger.info("Servidor iniciado.")
    yield
    logger.info("Deteniendo el servidor...")
    server_thread.join(0.1)

@pytest.fixture(scope="module")
def client():
    logger.info("Creando cliente para conectarse al servidor...")
    return BankClient('http://localhost:8000')

def test_create_account(client, server):
    logger.info("Test: Crear cuenta")
    response = client.create_account('testuser', 'password')
    assert response == "Cuenta creada exitosamente."

def test_authenticate_valid(client, server):
    logger.info("Test: Autenticar usuario válido")
    assert client.login('testuser', 'password')

def test_authenticate_invalid(client, server):
    logger.info("Test: Autenticar usuario inválido")
    assert not client.login('testuser', 'wrongpassword')

def test_deposit(client, server):
    logger.info("Test: Depositar")
    client.login('testuser', 'password')
    response = client.deposit(100)
    assert response == "Depósito de 100 en la cuenta testuser. Nuevo saldo es 100."

def test_withdraw(client, server):
    logger.info("Test: Retirar")
    client.login('testuser', 'password')
    response = client.withdraw(50)
    assert response == "Retiro de 50 de la cuenta testuser. Nuevo saldo es 50."

def test_transaction_history(client, server):
    logger.info("Test: Historial de transacciones")
    client.login('testuser', 'password')
    transactions = client.get_transaction_history()
    assert transactions == ["Depósito: 100", "Retiro: 50"]

def test_all_operations(client, server):
    test_create_account(client, server)
    test_authenticate_valid(client, server)
    test_deposit(client, server)
    test_withdraw(client, server)
    test_transaction_history(client, server)

if __name__ == "__main__":
    pytest.main()










"""
def test_create_duplicate_account(client):
    logger.info("Test: Crear cuenta duplicada")
    with patch('builtins.input', side_effect=["2", "testuser", "password", "3"]):
        from bank_client import main_menu
        main_menu(client)
    response = client.create_account("testuser", "password")
    logger.info(f"Respuesta: {response}")
    assert response == "La cuenta ya existe."

def test_authenticate(client):
    logger.info("Test: Autenticar usuario")
    with patch('builtins.input', side_effect=["1", "testuser", "password", "6"]):
        from bank_client import main_menu
        main_menu(client)
    response = client.authenticate("testuser", "password")
    logger.info(f"Respuesta: {response}")
    assert response

def test_authenticate_invalid(client):
    logger.info("Test: Autenticar usuario con contraseña incorrecta")
    with patch('builtins.input', side_effect=["1", "testuser", "wrongpassword", "3"]):
        from bank_client import main_menu
        main_menu(client)
    response = client.authenticate("testuser", "wrongpassword")
    logger.info(f"Respuesta: {response}")
    assert not response

def test_get_balance(client):
    logger.info("Test: Obtener balance")
    with patch('builtins.input', side_effect=["1", "testuser", "password", "1", "6"]):
        from bank_client import main_menu
        main_menu(client)
    response = client.get_balance()
    logger.info(f"Respuesta: {response}")
    assert response == 0

def test_deposit(client):
    logger.info("Test: Depositar")
    with patch('builtins.input', side_effect=["1", "testuser", "password", "2", "100", "6"]):
        from bank_client import main_menu
        main_menu(client)
    response = client.deposit(100)
    logger.info(f"Respuesta: {response}")
    assert response == "Depósito de 100 en la cuenta testuser. Nuevo saldo es 100."

def test_withdraw(client):
    logger.info("Test: Retirar")
    with patch('builtins.input', side_effect=["1", "testuser", "password", "3", "50", "6"]):
        from bank_client import main_menu
        main_menu(client)
    response = client.withdraw(50)
    logger.info(f"Respuesta: {response}")
    assert response == "Retiro de 50 de la cuenta testuser. Nuevo saldo es 50."

def test_withdraw_insufficient_funds(client):
    logger.info("Test: Retirar con fondos insuficientes")
    with patch('builtins.input', side_effect=["1", "testuser", "password", "3", "100", "6"]):
        from bank_client import main_menu
        main_menu(client)
    response = client.withdraw(100)
    logger.info(f"Respuesta: {response}")
    assert response == "Fondos insuficientes."

def test_transfer(client):
    logger.info("Test: Transferir fondos")
    with patch('builtins.input', side_effect=["2", "targetuser", "password", "3", "1", "testuser", "password", "4", "targetuser", "25", "6"]):
        from bank_client import main_menu
        main_menu(client)
    response = client.transfer("targetuser", 25)
    logger.info(f"Respuesta: {response}")
    assert response == ("Transferencia de 25 desde la cuenta testuser "
                        "a la cuenta targetuser. Nuevos saldos: testuser: 25, targetuser: 25.")

def test_transfer_insufficient_funds(client):
    logger.info("Test: Transferir con fondos insuficientes")
    with patch('builtins.input', side_effect=["1", "testuser", "password", "4", "targetuser", "50", "6"]):
        from bank_client import main_menu
        main_menu(client)
    response = client.transfer("targetuser", 50)
    logger.info(f"Respuesta: {response}")
    assert response == "Fondos insuficientes."

def test_get_transaction_history(client):
    logger.info("Test: Obtener historial de transacciones")
    with patch('builtins.input', side_effect=["1", "testuser", "password", "5", "6"]):
        from bank_client import main_menu
        main_menu(client)
    transactions = client.get_transaction_history()
    logger.info(f"Historial de transacciones: {transactions}")
    assert transactions == ["Depósito: 100", "Retiro: 50", "Transferencia a targetuser: 25"]

def test_get_notifications(client):
    logger.info("Test: Obtener notificaciones")
    with patch('builtins.input', side_effect=["1", "targetuser", "password", "6"]):
        from bank_client import main_menu
        main_menu(client)
    time.sleep(1)  # Espera un poco para asegurarse de que las notificaciones se procesen
    notifications = client.get_notifications()
    logger.info(f"Notificaciones recibidas: {notifications}")
    assert notifications == ["Transferencia recibida de testuser: 25"]

def test_logout(client):
    logger.info("Test: Cerrar sesión")
    with patch('builtins.input', side_effect=["1", "testuser", "password", "6"]):
        from bank_client import main_menu
        main_menu(client)
    client.logout()
    logger.info("Sesión cerrada.")
    assert client.current_account is None
"""


"""
import pytest
import threading
from xmlrpc.client import ServerProxy
from bank_server import run_server
from bank_client import BankClient
import time

@pytest.fixture(scope="module")
def server():
    # Inicia el servidor en un hilo separado
    server_thread = threading.Thread(target=run_server)
    server_thread.daemon = True
    server_thread.start()
    time.sleep(1)  # Espera un segundo para asegurarte de que el servidor esté completamente iniciado
    yield
    # Aquí podrías añadir código para detener el servidor si fuera necesario

@pytest.fixture(scope="module")
def client():
    # Crea un cliente para conectarse al servidor
    return BankClient('http://localhost:8000')

def test_create_account(client, server):
    response = client.create_account("testuser", "password")
    assert response == "Cuenta creada exitosamente."

def test_create_duplicate_account(client):
    response = client.create_account("testuser", "password")
    assert response == "La cuenta ya existe."

def test_authenticate(client):
    response = client.authenticate("testuser", "password")
    assert response

def test_authenticate_invalid(client):
    response = client.authenticate("testuser", "wrongpassword")
    assert not response

def test_get_balance(client):
    client.login("testuser", "password", notifications_enabled=False)
    response = client.get_balance()
    assert response == 0

def test_deposit(client):
    response = client.deposit(100)
    assert response == "Depósito de 100 en la cuenta testuser. Nuevo saldo es 100."

def test_withdraw(client):
    response = client.withdraw(50)
    assert response == "Retiro de 50 de la cuenta testuser. Nuevo saldo es 50."

def test_withdraw_insufficient_funds(client):
    response = client.withdraw(100)
    assert response == "Fondos insuficientes."

def test_transfer(client):
    client.create_account("targetuser", "password")
    client.login("testuser", "password", notifications_enabled=False)
    response = client.transfer("targetuser", 25)
    assert response == ("Transferencia de 25 desde la cuenta testuser "
                        "a la cuenta targetuser. Nuevos saldos: testuser: 25, targetuser: 25.")

def test_transfer_insufficient_funds(client):
    response = client.transfer("targetuser", 50)
    assert response == "Fondos insuficientes."

def test_get_transaction_history(client):
    transactions = client.get_transaction_history()
    assert transactions == ["Depósito: 100", "Retiro: 50", "Transferencia a targetuser: 25"]

def test_get_notifications(client):
    client.login("targetuser", "password", notifications_enabled=False)
    time.sleep(1)  # Espera un poco para asegurarse de que las notificaciones se procesen
    notifications = client.get_notifications()
    print(f"Notificaciones recibidas: {notifications}")  # Línea de depuración
    assert notifications == ["Transferencia recibida de testuser: 25"]

def test_logout(client):
    client.logout()
    assert client.current_account is None
"""