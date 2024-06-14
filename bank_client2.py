import xmlrpc.client
import threading
import time

class BankClient:
    def __init__(self, server_url):
        self.proxy = xmlrpc.client.ServerProxy(server_url)
        self.current_account = None
        self.notification_thread = None
        self.stop_notification_thread = False
        self.lock = threading.Lock()  # Añadido para sincronizar las solicitudes RPC

    def create_account(self, account_id, password):
        with self.lock:
            return self.proxy.create_account(account_id, password)

    def authenticate(self, account_id, password):
        with self.lock:
            return self.proxy.authenticate(account_id, password)

    def get_balance(self):
        with self.lock:
            return self.proxy.get_balance(self.current_account)

    def deposit(self, amount):
        with self.lock:
            return self.proxy.deposit(self.current_account, amount)

    def withdraw(self, amount):
        with self.lock:
            return self.proxy.withdraw(self.current_account, amount)

    def transfer(self, to_account, amount):
        with self.lock:
            return self.proxy.transfer(self.current_account, to_account, amount)

    def get_transaction_history(self):
        with self.lock:
            return self.proxy.get_transaction_history(self.current_account)

    def get_notifications(self):
        with self.lock:
            return self.proxy.get_notifications(self.current_account)

    def login(self, account_id, password, notifications_enabled=True):
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
        self.stop_notifications()
        self.current_account = None
        print("Sesión cerrada.")

    def stop_notifications(self):
        self.stop_notification_thread = True
        if self.notification_thread:
            self.notification_thread.join()

    def listen_for_notifications(self):
        while not self.stop_notification_thread:
            notifications = self.get_notifications()
            for notification in notifications:
                print(f"Notificación: {notification}")
            time.sleep(1)  # Ajuste del tiempo para recibir notificaciones más rápido

def main_menu(client, input_func=input):
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
