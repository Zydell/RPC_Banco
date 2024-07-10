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
"""
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