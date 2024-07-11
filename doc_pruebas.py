"""
Módulo de pruebas de sistema para la aplicación bancaria.\n

Este módulo documenta las pruebas de sistema para la aplicación bancaria,\n 
detallando cada paso que debe seguir el usuario para llevar a cabo las pruebas.\n\n

Pruebas documentadas:\n
1. Creación de cuenta exitosa\n
2. Prueba de autenticación exitosa\n
3. Prueba de consulta de saldo exitosa\n
4. Prueba de depósito exitoso\n
5. Prueba de retiro exitoso\n
6. Prueba de transferencia exitosa\n
7. Prueba de estado de cuenta\n
8. Prueba de cierre de sesión exitoso\n
9. Logueo con credenciales no registradas\n
10. Intento de creación de una cuenta ya existente\n
11. Retiro de una cuenta sin fondos\n
12. Transferencia a una cuenta no existente\n
13. Ingreso de valores negativos en depósitos\n
"""

def test_creacion_cuenta_exitosa():
    """
    Prueba 1: Creación de cuenta exitosa\n

    Pasos:\n
    1. Levantar el servidor: Se abre la terminal y se ejecuta el comando “python .\ bank_server.py”.\n
    2. Levantar el cliente: Se abre una segunda terminal y se ejecuta el comando “python .\ bank_client_antiguo.py”.\n
    3. En “Ingrese su opción:” se ingresa el número 2 que corresponde a la opción del menú de “Crear cuenta”.\n
    4. Se ingresa un ID no existente de la cuenta a crearse.\n
    5. Se ingresa la contraseña para su nueva cuenta.\n
    6. Se confirma la creación de lacuenta con un mensaje de “Cuenta creada exitosamente”.\n

    Resultado esperado:\n
    Mensaje que indica "Cuenta creada exitosamente".\n
    """
    pass

def test_autenticacion_exitosa():
    """
    Prueba 2: Autenticación exitosa\n

    Pasos:\n
    1. Levantar el servidor: Se abre la terminal y se ejecuta el comando “python .\ bank_server.py”.\n
    2. Levantar el cliente: Se abre una segunda terminal y se ejecuta el comando “python .\ bank_client_antiguo.py”.\n
    3. Si aún no tiene una cuenta, debe crear una cuenta a través de los pasos para la "Creación de cuenta exitosa".\n
    4. En “Ingrese su opción:” se ingresa el número 1 que corresponde a la opción del menú de “Ingresar”.\n
    5. Se ingresa un ID existente, de una cuenta que ya haya creado previamente.\n
    6. Se ingresa la contraseña correspondiente a su "ID de cuenta".\n
    7. Se confirma el inicio de sesión exitoso con el mensaje "Ingreso exitoso".\n

    Resultado esperado:\n
    Mensaje que indica "Ingreso exitoso".\n
    """
    pass

def test_consulta_saldo_exitosa():
    """
    Prueba 3: Consulta de saldo exitosa\n

    Pasos:\n
    1. Levantar el servidor: Se abre la terminal y se ejecuta el comando “python .\ bank_server.py”.\n
    2. Levantar el cliente: Se abre una segunda terminal y se ejecuta el comando “python .\ bank_client_antiguo.py”.\n
    3. Si aún no tiene una cuenta, debe crear una cuenta a través de los pasos para la "Creación de cuenta exitosa".\n
    4. En “Ingrese su opción:” se ingresa el número 1 que corresponde a la opción del menú de “Ingresar”.\n
    5. Se ingresa un ID existente, de una cuenta que ya haya creado previamente.\n
    6. Se ingresa la contraseña correspondiente a su "ID de cuenta".\n
    7. Se confirma el inicio de sesión exitoso con el mensaje "Ingreso exitoso".\n
    8. Se presenta un menú de 6 opciones y un mensaje "Ingrese su opción" en cual se coloca el número 1 que corresponde a "Consultar saldo".\n
    9. En caso de tener notificaciones se le presentara el detalle de quién le ha realizado una transferenciay deberá ingresar el valor de la opción "1" después de la notificación.\n
    10. Se muestra un mensaje "Saldo:" indicando el valor que dispone en su cuenta. Ejemplo:  "Saldo:0". \n
    
    Resultado esperado:\n
    Mensaje que indica "Saldo:0".\n
    """
    pass

def test_deposito_exitoso():
    """
    Prueba 4: Deposito exitosa\n

    Pasos:\n
    1. Levantar el servidor: Se abre la terminal y se ejecuta el comando “python .\ bank_server.py”.\n
    2. Levantar el cliente: Se abre una segunda terminal y se ejecuta el comando “python .\ bank_client_antiguo.py”.\n
    3. Si aún no tiene una cuenta, debe crear una cuenta a través de los pasos para la "Creación de cuenta exitosa".\n
    4. En “Ingrese su opción:” se ingresa el número 1 que corresponde a la opción del menú de “Ingresar”.\n
    5. Se ingresa un ID existente, de una cuenta que ya haya creado previamente.\n
    6. Se ingresa la contraseña correspondiente a su "ID de cuenta".\n
    7. Se confirma el inicio de sesión exitoso con el mensaje "Ingreso exitoso".\n
    8. Se presenta un menú de 6 opciones y un mensaje "Ingrese su opción" en cual se coloca el número 2 que corresponde a "Depositar".\n
    9. En caso de tener notificaciones se le presentara el detalle de quién le ha realizado una transferenciay deberá ingresar el valor de la opción "2" después de la notificación.\n
    10. Se muestra un mensaje "Ingrese la cantidad a depositar" indicando el valor que quiere depositar a su cuenta. Por ejemplo para depositar $50 sería "Ingrese la cantidad a depositar: 50" \n
    11. Se muestra un mensaje "Depósito de 50.0 en la cuenta test_user_9120. Nuevo saldo es 50.0" indicando el valor que ha depositado a su cuenta y actualizando el saldo que tiene despues del depósito. \n
    
    Resultado esperado:\n
    Mensaje que indica "Depósito de 50.0 en la cuenta test_user_9120. Nuevo saldo es 50.0.\n
    """
    pass

def test_retiro_exitoso():
    """
    Prueba 5: Retiro exitoso\n

    Pasos:\n
    1. Levantar el servidor: Se abre la terminal y se ejecuta el comando “python .\ bank_server.py”.\n
    2. Levantar el cliente: Se abre una segunda terminal y se ejecuta el comando “python .\ bank_client_antiguo.py”.\n
    3. Si aún no tiene una cuenta, debe crear una cuenta a través de los pasos para la "Creación de cuenta exitosa".\n
    4. En “Ingrese su opción:” se ingresa el número 1 que corresponde a la opción del menú de “Ingresar”.\n
    5. Se ingresa un ID existente, de una cuenta que ya haya creado previamente.\n
    6. Se ingresa la contraseña correspondiente a su "ID de cuenta".\n
    7. Se confirma el inicio de sesión exitoso con el mensaje "Ingreso exitoso".\n
    8. Se presenta un menú de 6 opciones y un mensaje "Ingrese su opción" en cual se coloca el número 3 que corresponde a "Retirar".\n
    9. En caso de tener notificaciones se le presentara el detalle de quién le ha realizado una transferenciay deberá ingresar el valor de la opción "3" después de la notificación.\n
    10. Se muestra un mensaje "Ingrese la cantidad a retirar" indicando el valor que quiere retirar de su cuenta. Por ejemplo si en la cuenta se tiene $50, se puede retirar $25 así: "Ingrese la cantidad a retirar: 25", el valor del retiro debe ser menor al valor que tiene en la cuenta. \n
    11. Se muestra un mensaje "Retiro de 25.0 de la cuenta test_user_9120. Nuevo saldo es 25.0" indicando el valor que ha retirado de su cuenta y actualizando el saldo que tiene después del retiro. \n

    Resultado esperado:\n
    Mensaje que indica "Retiro de 25.0 en la cuenta test_user_9120. Nuevo saldo es 25.0.\n
    """
    pass

def test_transferencia_exitosa():
    """
    Prueba 6: Transferencia exitosa\n

    Pasos:\n
    1. Levantar el servidor: Se abre la terminal y se ejecuta el comando “python .\ bank_server.py”.\n
    2. Levantar el cliente: Se abre una segunda terminal y se ejecuta el comando “python .\ bank_client_antiguo.py”.\n
    3. Si aún no tiene una cuenta, debe crear una cuenta a través de los pasos para la "Creación de cuenta exitosa".\n
    4. En “Ingrese su opción:” se ingresa el número 1 que corresponde a la opción del menú de “Ingresar”.\n
    5. Se ingresa un ID existente, de una cuenta que ya haya creado previamente.\n
    6. Se ingresa la contraseña correspondiente a su "ID de cuenta".\n
    7. Se confirma el inicio de sesión exitoso con el mensaje "Ingreso exitoso".\n
    8. Se presenta un menú de 6 opciones y un mensaje "Ingrese su opción" en cual se coloca el número 4 que corresponde a "Transferir".\n
    9. En caso de tener notificaciones se le presentara el detalle de quién le ha realizado una transferenciay deberá ingresar el valor de la opción "4" después de la notificación.\n
    10. Se muestra un mensaje "Ingrese la cuenta destino" , se ingresa el ID del usuario , debe ser un usuario existente al que se va a realizar la transferencia. Por ejemplo "Ingrese la cuenta de destino: test_user_9122" \n
    11. Se muestra un mensaje "Ingrese la cantidad a transferir", ingresa un valor que puede ser igual o menor al que tiene en la cuenta. Por ejemplo si en la cuenta tiene $25 puede transferir máximo hasta los $25, "Ingrese la cantidad a transferir: 10" \n
    12. Se muestra un mensaje "Transferencia de 10.0 desde la cuenta Berna2002 a la cuenta Omar2004. Nuevos saldos: test_user_9120: 15.0, test_user_9122: 10.0." se indica la cantidad transferida entre la cuenta que realiza la transacción a quien recibe eldinero y actualiza los saldos de ambas cuentas. \n

    Resultado esperado:
    Mensaje que indica "Transferencia de 10.0 desde la cuenta test_user_9120 a la cuenta test_user_9122. Nuevos saldos: test_user_9120: 15.0, test_user_9122: 10.0".\n
    """
    pass

def test_estado_cuenta():
    """
    Prueba 7: Estado de cuenta\n

    Pasos:\n
    1. Levantar el servidor: Se abre la terminal y se ejecuta el comando “python .\ bank_server.py”.\n
    2. Levantar el cliente: Se abre una segunda terminal y se ejecuta el comando “python .\ bank_client_antiguo.py”.\n
    3. Si aún no tiene una cuenta, debe crear una cuenta a través de los pasos para la "Creación de cuenta exitosa".\n
    4. En “Ingrese su opción:” se ingresa el número 1 que corresponde a la opción del menú de “Ingresar”.\n
    5. Se ingresa un ID existente, de una cuenta que ya haya creado previamente.\n
    6. Se ingresa la contraseña correspondiente a su "ID de cuenta".\n
    7. Se confirma el inicio de sesión exitoso con el mensaje "Ingreso exitoso".\n
    8. Se presenta un menú de 6 opciones y un mensaje "Ingrese su opción" en cual se coloca el número 5 que corresponde a "Estado de cuenta".\n
    9. En caso de tener notificaciones se le presentara el detalle de quién le ha realizado una transferencia y deberá ingresar el valor de la opción "5" después de la notificación.\n
    9. Se muestra en pantalla:
       "Historial de transacciones:
        Depósito: 50.0
        Retiro: 25.0
        Transferencia a test_user_9122: 10.0"
        indicando todas las transacciones que se han realizado en la cuenta respecto a : Depositar, Retirar, Transferir \n

    Resultado esperado:\n
    Historial de transacciones:\n
    Depósito: 50.0\n
    Retiro: 25.0\n
    Transferencia a test_user_9122: 10.0\n
    """
    pass

def test_cierre_sesion_exitoso():
    """
    Prueba 8: Cierre de sesión exitoso\n

    1. CASO EN EL QUE SE ENCUENTRE EN EL MENÚ PRINCIPAL: 
    "   1. Ingresar    
        2. Crear cuenta
        3. Salir  "

        Pasos:\n
        1. Levantar el servidor: Se abre la terminal y se ejecuta el comando “python .\ bank_server.py”.\n
        2. Levantar el cliente: Se abre una segunda terminal y se ejecuta el comando “python .\ bank_client_antiguo.py”.\n
        3. En “Ingrese su opción:” se ingresa el número 3 que corresponde a la opción del menú de “Salir”.\n
        4. Se muestra un mensaje de "Sesión cerrada". \n
        5. Se acaba el proceso y ha salido del programa exitosamente.\n
        
    2. CASO EN EL QUE SE ENCUENTRE EN EL SUBMENÚ: 
    "   1. Consultar saldo
        2. Depositar
        3. Retirar
        4. Transferir
        5. Estado de cuenta
        6. Cerrar sesión "

        Pasos:\n
        1. Levantar el servidor: Se abre la terminal y se ejecuta el comando “python .\ bank_server.py”.\n
        2. Levantar el cliente: Se abre una segunda terminal y se ejecuta el comando “python .\ bank_client_antiguo.py”.\n
        3. Si aún no tiene una cuenta, debe crear una cuenta a través de los pasos para la "Creación de cuenta exitosa".\n
        4. En “Ingrese su opción:” se ingresa el número 1 que corresponde a la opción del menú de “Ingresar”.\n
        5. Se ingresa un ID existente, de una cuenta que ya haya creado previamente.\n
        6. Se ingresa la contraseña correspondiente a su "ID de cuenta".\n
        7. Se confirma el inicio de sesión exitoso con el mensaje "Ingreso exitoso".\n
        8. Se presenta un menú de 6 opciones y un mensaje "Ingrese su opción" en cual se coloca el número 6 que corresponde a "Cerrar Sesión".\n
        9. En caso de tener notificaciones se le presentara el detalle de quién le ha realizado una transferenciay deberá ingresar el valor de la opción "6" después de la notificación.\n
        10. Se muestra un mensaje de "Sesión cerrada". \n
        11. Se acaba el proceso y ha salido del programa exitosamente.\n

    Resultado esperado:\n
    Mensaje que indica "Sesión cerrada".\n
    """
    pass

def test_logueo_credenciales_no_registradas():
    """
    Prueba 9: Logueo con credenciales no registradas\n

    Pasos:\n
    1. Levantar el servidor: Se abre la terminal y se ejecuta el comando “python .\ bank_server.py”.\n
    2. Levantar el cliente: Se abre una segunda terminal y se ejecuta el comando “python .\ bank_client_antiguo.py”.\n
    4. En “Ingrese su opción:” se ingresa el número 1 que corresponde a la opción del menú de “Ingresar”.\n
    5. Se puede ingresa un ID no existente:"invalid_user" o un ID existente:"valid_user".\n
    6. Se ingresa una contraseña cualquiera para el caso de un ID no existente:"password_123" y en el caso de un ID existente se ingresa una contraseña incorrecta "invalid_password" ".\n
    7. Se muestra un mensaje de "ID de cuenta o contraseña incorrectos".\n
    8. Se confirma que el inicio de sesión falla con el mensaje "ID de cuenta o contraseña incorrectos."\n

    Resultado esperado:\n
    Mensaje que indica "ID de cuenta o contraseña incorrectos".\n
    """
    pass

def test_creacion_cuenta_existente():
    """
    Prueba 10: Intento de creación de una cuenta ya existente\n

    Pasos:\n
    1. Levantar el servidor: Se abre la terminal y se ejecuta el comando “python .\ bank_server.py”.\n
    2. Levantar el cliente: Se abre una segunda terminal y se ejecuta el comando “python .\ bank_client_antiguo.py”.\n
    3. En “Ingrese su opción:” se ingresa el número 2 que corresponde a la opción del menú de “Crear cuenta”.\n
    4. Se ingresa un ID existente test_user_9120 de la cuenta crearse.\n
    5. Se ingresa la contraseña para su nueva cuenta.\n
    6. Se confirma que la creación de la cuenta no ha sido exitoso con un mensaje de “La cuenta ya existe”.\n

    Resultado esperado:\n
    Mensaje que indica "La cuenta ya existe".\n
    """
    pass

def test_retiro_sin_fondos():
    """
    Prueba 11: Retiro de una cuenta sin fondos\n

    Pasos:\n
    1. Levantar el servidor: Se abre la terminal y se ejecuta el comando “python .\ bank_server.py”.\n
    2. Levantar el cliente: Se abre una segunda terminal y se ejecuta el comando “python .\ bank_client_antiguo.py”.\n
    3. Si aún no tiene una cuenta, debe crear una cuenta a través de los pasos para la "Creación de cuenta exitosa".\n
    4. En “Ingrese su opción:” se ingresa el número 1 que corresponde a la opción del menú de “Ingresar”.\n
    5. Se ingresa un ID existente, de una cuenta que ya haya creado previamente.\n
    6. Se ingresa la contraseña correspondiente a su "ID de cuenta".\n
    7. Se confirma el inicio de sesión exitoso con el mensaje "Ingreso exitoso".\n
    8. Se presenta un menú de 6 opciones y un mensaje "Ingrese su opción" en cual se coloca el número 3 que corresponde a "Retirar".\n
    9. En caso de tener notificaciones se le presentara el detalle de quién le ha realizado una transferenciay deberá ingresar el valor de la opción "3" después de la notificación.\n
    10. Se muestra un mensaje "Ingrese la cantidad a retirar" indicando el valor que quiere retirar de su cuenta. Por ejemplo si en la cuenta se tiene $50, y coloca para retirar $60 así: "Ingrese la cantidad a retirar: 60", el valor del retiro debe ser mayorr al valor que tiene en la cuenta. \n
    11. Se confirma de que el retiro ha fallado con el mensaje “Fondos insuficientes”.\n

    Resultado esperado:\n
    Mensaje que indica "Fondos insuficientes".\n
    """
    pass

def test_transferencia_cuenta_no_existente():
    """
    Prueba 12: Transferencia a una cuenta no existente\n

    Pasos:\n
    1. Levantar el servidor: Se abre la terminal y se ejecuta el comando “python .\ bank_server.py”.\n
    2. Levantar el cliente: Se abre una segunda terminal y se ejecuta el comando “python .\ bank_client_antiguo.py”.\n
    3. Si aún no tiene una cuenta, debe crear una cuenta a través de los pasos para la "Creación de cuenta exitosa".\n
    4. En “Ingrese su opción:” se ingresa el número 1 que corresponde a la opción del menú de “Ingresar”.\n
    5. Se ingresa un ID existente, de una cuenta que ya haya creado previamente.\n
    6. Se ingresa la contraseña correspondiente a su "ID de cuenta".\n
    7. Se confirma el inicio de sesión exitoso con el mensaje "Ingreso exitoso".\n
    8. Se presenta un menú de 6 opciones y un mensaje "Ingrese su opción" en cual se coloca el número 4 que corresponde a "Transferir".\n
    9. En caso de tener notificaciones se le presentara el detalle de quién le ha realizado una transferenciay deberá ingresar el valor de la opción "4" después de la notificación.\n
    10. Se muestra un mensaje "Ingrese la cuenta destino" , se ingresa el ID del usuario no existente , debe ser un usuario que no exista al que se va a realizar la transferencia. Por ejemplo "Ingrese la cuenta de destino: non_existent_account" \n
    11. Se muestra un mensaje "Ingrese la cantidad a transferir", ingresa un valor cualquiera en este caso. Ingresar "25.0" como cantidad a transferir \n
    12. Se confirma de que la transferencia ha fallado con el mensaje "Una o ambas cuentas no existen" \n

    Resultado esperado:\n
    Mensaje que indica "Una o ambas cuentas no existen".\n
    """
    pass

def test_deposito_negativo():
    """
    Prueba 13: Ingreso de valores negativos en depósitos\n

    Pasos:\n
    1. Levantar el servidor: Se abre la terminal y se ejecuta el comando “python .\ bank_server.py”.\n
    2. Levantar el cliente: Se abre una segunda terminal y se ejecuta el comando “python .\ bank_client_antiguo.py”.\n
    3. Si aún no tiene una cuenta, debe crear una cuenta a través de los pasos para la "Creación de cuenta exitosa".\n
    4. En “Ingrese su opción:” se ingresa el número 1 que corresponde a la opción del menú de “Ingresar”.\n
    5. Se ingresa un ID existente, de una cuenta que ya haya creado previamente.\n
    6. Se ingresa la contraseña correspondiente a su "ID de cuenta".\n
    7. Se confirma el inicio de sesión exitoso con el mensaje "Ingreso exitoso".\n
    8. Se presenta un menú de 6 opciones y un mensaje "Ingrese su opción" en cual se coloca el número 2 que corresponde a "Depositar".\n
    9. En caso de tener notificaciones se le presentara el detalle de quién le ha realizado una transferenciay deberá ingresar el valor de la opción "2" después de la notificación.\n
    10. Se muestra un mensaje "Ingrese la cantidad a depositar" indicando el valor que quiere depositar a su cuenta. Por ejemplo : "Ingrese la cantidad a depositar: -100" \n
    11. Se confirma de que la transferencia ha fallado con el mensaje "La cantidad a depositar debe ser positiva" . \n

    Resultado esperado:\n
    Mensaje que indica "La cantidad a depositar debe ser positiva".\n
    """
    pass
