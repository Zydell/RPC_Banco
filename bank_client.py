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

    def delete_account(self, account_id):
        """
        Elimina una cuenta del servidor bancario.

        Args:
            account_id (str): El ID de la cuenta.

        Returns:
            str: Mensaje de éxito o error.
        """
        with self.lock:
            return self.proxy.delete_account(account_id)
    
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

def automated_test(client):
    """
    Simula la interacción automática con el cliente bancario.

    Args:
        client (BankClient): El cliente bancario.
    """
    steps = [
        ('2', "\nPrueba 1: Creación de cuenta (test_user_9120)...\n"),  # Crear cuenta
        ('test_user_9120', None),  # Crear cuenta
        ('test_password', None),  # Contraseña
        ('1', "\nPrueba 2: Autenticación (test_user_9120)...\n"),  # Ingresar
        ('test_user_9120', None),  # ID de cuenta
        ('test_password', None),  # Contraseña
        ('1', "\nPrueba 3: Consulta de saldo...\n"),  # Consultar saldo
        ('2', "\nPrueba 4: Depósito (100.0)...\n"),  # Depositar
        ('100.0', None),  # Monto a depositar
        ('1', "\nPrueba 5: Consulta de saldo después de depósito...\n"),  # Consultar saldo
        ('3', "\nPrueba 6: Retiro (50.0)...\n"),  # Retirar
        ('50.0', None),  # Monto a retirar
        ('1', "\nPrueba 7: Consulta de saldo después de retiro...\n"),  # Consultar saldo
        ('5', "\nPrueba 8: Consulta de estado de cuenta...\n"),  # Estado de cuenta
        ('6', "\nPrueba 9: Cierre de sesión...\n"),  # Cerrar Sesion
        ('2', "\nPrueba 10: Creación de otra cuenta (test_user_9121)...\n"),  # Crear otra cuenta
        ('test_user_9121', None),  # Crear cuenta
        ('test_password2', None),  # Contraseña
        ('1', "\nPrueba 11: Autenticación con otra cuenta (test_user_9121)...\n"),  # Ingresar
        ('test_user_9121', None),  # ID de cuenta
        ('test_password2', None),  # Contraseña
        ('2', "\nPrueba 12: Depósito en la segunda cuenta (100.0)...\n"),  # Depositar en cuenta 2
        ('100.0', None),  # Monto a depositar
        ('4', "\nPrueba 13: Transferencia entre cuentas (25.0)...\n"),  # Transferir
        ('test_user_9120', None),  # Cuenta de destino
        ('25.0', None),  # Monto a transferir
        ('5', "\nPrueba 14: Consulta de estado de cuenta después de transferencia...\n"),  # Estado de cuenta
        ('6', "\nPrueba 15: Cierre de sesión de la otra cuenta (cuenta 2)...\n"),  # Cerrar Sesion
        ('1', "\nPrueba 16: Inicio de sesión en la cuenta 1...\n"),  # Ingresar
        ('test_user_9120', None),  # ID de cuenta
        ('test_password', None),  # Contraseña
        ('1', "\nPrueba 17: Consulta de saldo después de transferencia...\n"),  # Consultar saldo
        ('6', "\nPrueba 18: Cierre de sesión...\n"),  # Cerrar Sesion
        ('1', "\nPrueba 19: Inicio de sesión con credenciales incorrectas...\n"),  # Intento de login con credenciales incorrectas
        ('invalid_user', None),  # ID de cuenta incorrecto
        ('invalid_password', None),  # Contraseña incorrecta
        ('2', "\nPrueba 20: Creación de cuenta ya existente...\n"),  # Crear una cuenta ya existente
        ('test_user_9120', None),  # ID de cuenta existente
        ('test_password', None),  # Contraseña
        ('1', "\nPrueba 21: Retiro con fondos insuficientes...\n"),  # Ingresar
        ('test_user_9120', None),  # ID de cuenta
        ('test_password', None),  # Contraseña
        ('3', "\nPrueba 22: Retiro con fondos insuficientes (750.0)...\n"),  # Retiro con fondos insuficientes
        ('750.0', None),  # Monto a retirar mayor al saldo disponible
        ('4', "\nPrueba 23: Transferencia a cuenta inexistente...\n"),  # Transferencia a cuenta inexistente
        ('non_existent_account', None),  # Cuenta de destino inexistente
        ('25.0', None),  # Monto a transferir
        ('2', "\nPrueba 24: Depósito con monto negativo (-100.0)...\n"),  # Depositar monto negativo
        ('-100.0', None),  # Monto negativo
        ('6', "\nPrueba 25: Cierre de sesión final...\n"),  # Cerrar Sesion
        ('3', "\nPruebas completadas exitosamente.\n")  # Salir
    ]

    step_index = 0

    def input_func(prompt):
        nonlocal step_index
        if step_index < len(steps):
            response, message = steps[step_index]
            if message:
                print(message)
                time.sleep(0)  # Simulación de la demora al mostrar el mensaje
            step_index += 1
            print(f"{prompt} {response}")
            time.sleep(0)  # Simulación de la demora al ingresar los datos
            return response
        return ""

    main_menu(client, input_func)

if __name__ == "__main__":
    client = BankClient('http://localhost:8000')
    automated_test(client)