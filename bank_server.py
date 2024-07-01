from xmlrpc.server import SimpleXMLRPCServer, SimpleXMLRPCRequestHandler
import threading
import hashlib
import queue

class RequestHandler(SimpleXMLRPCRequestHandler):
    """Clase para manejar solicitudes RPC."""
    rpc_paths = ('/RPC2',)

class BankServer:
    """
    Clase que representa un servidor bancario.

    Atributos:
        accounts (dict): Diccionario de cuentas con sus saldos.
        credentials (dict): Diccionario de credenciales de las cuentas.
        transaction_history (dict): Historial de transacciones por cuenta.
        notifications (dict): Notificaciones en cola por cuenta.
        lock (threading.Lock): Lock para control de acceso concurrente.
    """

    def __init__(self):
        """Inicializa los atributos del servidor bancario."""
        self.accounts = {}
        self.credentials = {}
        self.transaction_history = {}
        self.notifications = {}
        self.lock = threading.Lock()

    def hash_password(self, password):
        """
        Genera el hash de una contraseña.

        Args:
            password (str): La contraseña a hashear.

        Returns:
            str: El hash de la contraseña.
        """
        return hashlib.sha256(password.encode()).hexdigest()

    def create_account(self, account_id, password):
        """
        Crea una nueva cuenta en el servidor bancario.

        Args:
            account_id (str): El ID de la cuenta.
            password (str): La contraseña de la cuenta.

        Returns:
            str: Mensaje de éxito o error.
        """
        with self.lock:
            if account_id in self.accounts:
                return "La cuenta ya existe."
            self.accounts[account_id] = 0
            self.credentials[account_id] = self.hash_password(password)
            self.transaction_history[account_id] = []
            self.notifications[account_id] = queue.Queue()
            return "Cuenta creada exitosamente."

    def authenticate(self, account_id, password):
        """
        Autentica a un usuario.

        Args:
            account_id (str): El ID de la cuenta.
            password (str): La contraseña de la cuenta.

        Returns:
            bool: True si la autenticación es exitosa, False en caso contrario.
        """
        with self.lock:
            if account_id not in self.credentials:
                return False
            return self.credentials[account_id] == self.hash_password(password)

    def get_balance(self, account_id):
        """
        Obtiene el saldo de una cuenta.

        Args:
            account_id (str): El ID de la cuenta.

        Returns:
            str: El saldo de la cuenta o un mensaje de error.
        """
        with self.lock:
            if account_id not in self.accounts:
                return "La cuenta no existe."
            return self.accounts[account_id]

    def deposit(self, account_id, amount):
        """
        Realiza un depósito en una cuenta.

        Args:
            account_id (str): El ID de la cuenta.
            amount (float): La cantidad a depositar.

        Returns:
            str: Mensaje de éxito o error.
        """
        if amount <= 0:
            return "La cantidad a depositar debe ser positiva."
        with self.lock:
            if account_id not in self.accounts:
                return "La cuenta no existe."
            self.accounts[account_id] += amount
            self.transaction_history[account_id].append(f"Depósito: {amount}")
            return f"Depósito de {amount} en la cuenta {account_id}. Nuevo saldo es {self.accounts[account_id]}."

    def withdraw(self, account_id, amount):
        """
        Realiza un retiro de una cuenta.

        Args:
            account_id (str): El ID de la cuenta.
            amount (float): La cantidad a retirar.

        Returns:
            str: Mensaje de éxito o error.
        """
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
        """
        Realiza una transferencia entre cuentas.

        Args:
            from_account (str): El ID de la cuenta de origen.
            to_account (str): El ID de la cuenta de destino.
            amount (float): La cantidad a transferir.

        Returns:
            str: Mensaje de éxito o error.
        """
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
        """
        Obtiene el historial de transacciones de una cuenta.

        Args:
            account_id (str): El ID de la cuenta.

        Returns:
            list: Lista de transacciones o un mensaje de error.
        """
        with self.lock:
            if account_id not in self.transaction_history:
                return "La cuenta no existe."
            return self.transaction_history[account_id]

    def get_notifications(self, account_id):
        """
        Obtiene las notificaciones de una cuenta.

        Args:
            account_id (str): El ID de la cuenta.

        Returns:
            list: Lista de notificaciones.
        """
        if account_id not in self.notifications:
            return []
        notifications = []
        while not self.notifications[account_id].empty():
            notifications.append(self.notifications[account_id].get())
        return notifications

def run_server():
    """Inicia el servidor bancario."""
    server = SimpleXMLRPCServer(('localhost', 8000), requestHandler=RequestHandler, allow_none=True)
    server.register_instance(BankServer())
    print("Servidor bancario corriendo en el puerto 8000...")
    server.serve_forever()

if __name__ == "__main__":
    run_server()
