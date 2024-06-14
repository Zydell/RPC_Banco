from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import threading
import hashlib
import queue

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

class BankServer:
    def __init__(self):                 # atributos
        self.accounts = {}
        self.credentials = {}
        self.transaction_history = {}
        self.notifications = {}
        self.lock = threading.Lock()        # control del acceso concurrente

    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()        # encriptacion de las contraseñas

    def create_account(self, account_id, password):
        with self.lock:
            if account_id in self.accounts:
                return "La cuenta ya existe."
            self.accounts[account_id] = 0
            self.credentials[account_id] = self.hash_password(password)
            self.transaction_history[account_id] = []
            self.notifications[account_id] = queue.Queue()
            return "Cuenta creada exitosamente."

    def authenticate(self, account_id, password):
        with self.lock:
            if account_id not in self.credentials:
                return False
            return self.credentials[account_id] == self.hash_password(password)

    def get_balance(self, account_id):
        with self.lock:
            if account_id not in self.accounts:
                return "La cuenta no existe."
            return self.accounts[account_id]

    def deposit(self, account_id, amount):
        if amount <= 0:
            return "La cantidad a depositar debe ser positiva."
        with self.lock:
            if account_id not in self.accounts:
                return "La cuenta no existe."
            self.accounts[account_id] += amount
            self.transaction_history[account_id].append(f"Depósito: {amount}")
            return f"Depósito de {amount} en la cuenta {account_id}. Nuevo saldo es {self.accounts[account_id]}."

    def withdraw(self, account_id, amount):
        if amount <= 0:
            return "La cantidad a retirar debe ser positiva."
        with self.lock:
            if account_id not in self.accounts:
                return "La cuenta no existe."
            if self.accounts[account_id] < amount:
                return "Fondos insuficientes."
            self.accounts[account_id] -= amount
            self.transaction_history[account_id].append(f"Retiro: {amount}")
            return f"Retiro de {amount} de la cuenta {account_id}. Nuevo saldo es {self.accounts[account_id]}."

    def transfer(self, from_account, to_account, amount):
        if amount <= 0:
            return "La cantidad a transferir debe ser positiva."
        with self.lock:
            if from_account not in self.accounts or to_account not in self.accounts:
                return "Una o ambas cuentas no existen."
            if self.accounts[from_account] < amount:
                return "Fondos insuficientes."
            self.accounts[from_account] -= amount
            self.accounts[to_account] += amount
            self.transaction_history[from_account].append(f"Transferencia a {to_account}: {amount}")
            self.transaction_history[to_account].append(f"Transferencia de {from_account}: {amount}")
            self.notifications[to_account].put(f"Transferencia recibida de {from_account}: {amount}")
            return (f"Transferencia de {amount} desde la cuenta {from_account} "
                    f"a la cuenta {to_account}. Nuevos saldos: {from_account}: {self.accounts[from_account]}, {to_account}: {self.accounts[to_account]}.")

    def get_transaction_history(self, account_id):
        with self.lock:
            if account_id not in self.transaction_history:
                return "La cuenta no existe."
            return self.transaction_history[account_id]

    def get_notifications(self, account_id):
        if account_id not in self.notifications:
            return []
        notifications = []
        while not self.notifications[account_id].empty():
            notifications.append(self.notifications[account_id].get())
        return notifications

def run_server():
    server = SimpleXMLRPCServer(('localhost', 8000), requestHandler=RequestHandler, allow_none=True)
    #sserver = SimpleXMLRPCServer(('172.25.233.8', 8000), requestHandler=RequestHandler, allow_none=True)
    server.register_instance(BankServer())
    print("Servidor bancario corriendo en el puerto 8000...")
    server.serve_forever()

if __name__ == "__main__":
    run_server()
