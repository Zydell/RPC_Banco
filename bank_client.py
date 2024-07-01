import xmlrpc.client
import threading
import time

class BankClient:
    """
    Clase que representa un cliente del banco.

    Atributos:
        proxy (ServerProxy): Proxy para comunicarse con el servidor RPC.
        current_account (str): La cuenta actual autenticada.
        notification_thread (threading.Thread): Hilo para recibir notificaciones.
        stop_notification_thread (bool): Bandera para detener el hilo de notificaciones.
        lock (threading.Lock): Lock para sincronizar las solicitudes RPC.
    """

    def __init__(self, server_url):
        """
        Inicializa los atributos del cliente bancario.

        Args:
            server_url (str): URL del servidor RPC.
        """
        self.proxy = xmlrpc.client.ServerProxy(server_url)
        self.current_account = None
        self.notification_thread = None
        self.stop_notification_thread = False
        self.lock = threading.Lock()

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
            return self.proxy.create_account(account_id, password)

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
            return self.proxy.authenticate(account_id, password)

    def get_balance(self):
        """
        Obtiene el saldo de la cuenta actual.

        Returns:
            float: El saldo de la cuenta.
        """
        with self.lock:
            return self.proxy.get_balance(self.current_account)

    def deposit(self, amount):
        """
        Realiza un depósito en la cuenta actual.

        Args:
            amount (float): La cantidad a depositar.

        Returns:
            str: Mensaje de éxito o error.
        """
        with self.lock:
            return self.proxy.deposit(self.current_account, amount)

    def withdraw(self, amount):
        """
        Realiza un retiro de la cuenta actual.

        Args:
            amount (float): La cantidad a retirar.

        Returns:
            str: Mensaje de éxito o error.
        """
        with self.lock:
            return self.proxy.withdraw(self.current_account, amount)

    def transfer(self, to_account, amount):
        """
        Realiza una transferencia desde la cuenta actual a otra cuenta.

        Args:
            to_account (str): El ID de la cuenta de destino.
            amount (float): La cantidad a transferir.

        Returns:
            str: Mensaje de éxito o error.
        """
        with self.lock:
            return self.proxy.transfer(self.current_account, to_account, amount)

    def get_transaction_history(self):
        """
        Obtiene el historial de transacciones de la cuenta actual.

        Returns:
            list: Lista de transacciones.
        """
        with self.lock:
            return self.proxy.get_transaction_history(self.current_account)

    def get_notifications(self):
        """
        Obtiene las notificaciones de la cuenta actual.

        Returns:
            list: Lista de notificaciones.
        """
        with self.lock:
            return self.proxy.get_notifications(self.current_account)

    def login(self, account_id, password, notifications_enabled=True):
        """
        Autentica a un usuario y, opcionalmente, inicia el hilo de notificaciones.

        Args:
            account_id (str): El ID de la cuenta.
            password (str): La contraseña de la cuenta.
            notifications_enabled (bool): Si se deben habilitar las notificaciones.

        Returns:
            bool: True si la autenticación es exitosa, False en caso contrario.
        """
        if self.authenticate(account_id, password):
            self.current_account = account_id
            print("Ingreso exitoso.")
            if notifications_enabled:
                self.stop_notification_thread = False
                self.notification_thread = threading.Thread(target=self.listen_for_notifications)
                self.notification_thread.start()
            return True
        else:
            print("ID de cuenta o contraseña incorrectos.")
            return False

    def logout(self):
        """Cierra la sesión del usuario actual y detiene el hilo de notificaciones."""
        self.stop_notifications()
        self.current_account = None
        print("Sesión cerrada.")

    def stop_notifications(self):
        """Detiene el hilo de notificaciones."""
        self.stop_notification_thread = True
        if self.notification_thread:
            self.notification_thread.join()

    def listen_for_notifications(self):
        """Escucha y muestra las notificaciones de la cuenta actual."""
        while not self.stop_notification_thread:
            notifications = self.get_notifications()
            for notification in notifications:
                print(f"\nNotificación: {notification}")
            time.sleep(1)

def main_menu(client, input_func=input):
    """
    Muestra el menú principal para interactuar con el cliente bancario.

    Args:
        client (BankClient): El cliente bancario.
        input_func (function): Función para recibir entradas del usuario.
    """
    while True:
        print("\n1. Ingresar\n2. Crear cuenta\n3. Salir")
        choice = input_func("Ingrese su opción: ")
        if choice == '1':
            account_id = input_func("Ingrese su ID de cuenta: ")
            password = input_func("Ingrese su contraseña: ")
            if client.login(account_id, password):
                user_menu(client, input_func)
        elif choice == '2':
            account_id = input_func("Ingrese su ID de cuenta: ")
            password = input_func("Ingrese su contraseña: ")
            print(client.create_account(account_id, password))
        elif choice == '3':
            break
        else:
            print("Opción inválida. Intente de nuevo.")

def user_menu(client, input_func=input):
    """
    Muestra el menú de usuario para interactuar con la cuenta bancaria.

    Args:
        client (BankClient): El cliente bancario.
        input_func (function): Función para recibir entradas del usuario.
    """
    while True:
        print("\n1. Consultar saldo\n2. Depositar\n3. Retirar\n4. Transferir\n5. Estado de cuenta\n6. Cerrar sesión")
        sub_choice = input_func("Ingrese su opción: ")
        if sub_choice == '1':
            print(f"Saldo: {client.get_balance()}")
        elif sub_choice == '2':
            amount = float(input_func("Ingrese la cantidad a depositar: "))
            print(client.deposit(amount))
        elif sub_choice == '3':
            amount = float(input_func("Ingrese la cantidad a retirar: "))
            print(client.withdraw(amount))
        elif sub_choice == '4':
            to_account = input_func("Ingrese la cuenta de destino: ")
            amount = float(input_func("Ingrese la cantidad a transferir: "))
            print(client.transfer(to_account, amount))
        elif sub_choice == '5':
            transactions = client.get_transaction_history()
            if transactions:
                print("Historial de transacciones:")
                for transaction in transactions:
                    print(transaction)
            else:
                print("No hay transacciones.")
        elif sub_choice == '6':
            client.logout()
            break
        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    client = BankClient('http://localhost:8000')
    main_menu(client)
