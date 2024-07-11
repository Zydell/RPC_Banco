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
    1. Seleccionar la opción "2. Crear cuenta" del menú principal.\n
    2. Ingresar "test_user_9120" como ID de cuenta.\n
    3. Ingresar "test_password" como contraseña.\n
    4. Confirmar la creación exitosa de la cuenta con el mensaje "Cuenta creada exitosamente."\n

    Resultado esperado:\n
    Cuenta creada exitosamente.\n
    """
    pass

def test_autenticacion_exitosa():
    """
    Prueba 2: Autenticación exitosa\n

    Pasos:\n
    1. Seleccionar la opción "1. Ingresar" del menú principal.\n
    2. Ingresar "test_user_9120" como ID de cuenta.\n
    3. Ingresar "test_password" como contraseña.\n
    4. Confirmar el inicio de sesión exitoso con el mensaje "Ingreso exitoso."\n

    Resultado esperado:\n
    Ingreso exitoso.\n
    """
    pass

def test_consulta_saldo_exitosa():
    """
    Prueba 3: Consulta de saldo exitosa\n

    Pasos:\n
    1. Seleccionar la opción "1. Consultar saldo" del menú de usuario.\n
    2. Verificar que el saldo de la cuenta sea mostrado correctamente.\n

    Resultado esperado:\n
    Saldo: 0\n
    """
    pass

def test_deposito_exitoso():
    """
    Prueba 4: Depósito exitoso\n

    Pasos:\n
    1. Seleccionar la opción "2. Depositar" del menú de usuario.\n
    2. Ingresar "100.0" como cantidad a depositar.\n
    3. Confirmar el depósito exitoso con el mensaje "Depósito de 100.0 en la cuenta test_user_9120. Nuevo saldo es 100.0."\n

    Resultado esperado:\n
    Depósito de 100.0 en la cuenta test_user_9120. Nuevo saldo es 100.0.\n
    """
    pass

def test_retiro_exitoso():
    """
    Prueba 5: Retiro exitoso\n

    Pasos:
    1. Seleccionar la opción "3. Retirar" del menú de usuario.\n
    2. Ingresar "50.0" como cantidad a retirar.\n
    3. Confirmar el retiro exitoso con el mensaje "Retiro de 50.0 de la cuenta test_user_9120. Nuevo saldo es 50.0."\n

    Resultado esperado:\n
    Retiro de 50.0 de la cuenta test_user_9120. Nuevo saldo es 50.0.\n
    """
    pass

def test_transferencia_exitosa():
    """
    Prueba 6: Transferencia exitosa\n

    Pasos:\n
    1. Seleccionar la opción "4. Transferir" del menú de usuario.\n
    2. Ingresar "test_user_9121" como cuenta de destino.\n
    3. Ingresar "25.0" como cantidad a transferir.\n
    4. Confirmar la transferencia exitosa con el mensaje "Transferencia de 25.0 desde la cuenta test_user_9120 a la cuenta test_user_9121. Nuevos saldos: test_user_9120: 75.0, test_user_9121: 75.0."\n

    Resultado esperado:
    Transferencia de 25.0 desde la cuenta test_user_9120 a la cuenta test_user_9121. Nuevos saldos: test_user_9120: 75.0, test_user_9121: 75.0.\n
    """
    pass

def test_estado_cuenta():
    """
    Prueba 7: Estado de cuenta\n

    Pasos:\n
    1. Seleccionar la opción "5. Estado de cuenta" del menú de usuario.\n
    2. Verificar que el historial de transacciones sea mostrado correctamente.\n

    Resultado esperado:\n
    Historial de transacciones:\n
    Depósito: 100.0\n
    Retiro: 50.0\n
    """
    pass

def test_cierre_sesion_exitoso():
    """
    Prueba 8: Cierre de sesión exitoso\n

    Pasos:\n
    1. Seleccionar la opción "6. Cerrar sesión" del menú de usuario.\n
    2. Confirmar el cierre de sesión exitoso con el mensaje "Sesión cerrada."\n

    Resultado esperado:\n
    Sesión cerrada.\n
    """
    pass

def test_logueo_credenciales_no_registradas():
    """
    Prueba 9: Logueo con credenciales no registradas\n

    Pasos:\n
    1. Seleccionar la opción "1. Ingresar" del menú principal.\n
    2. Ingresar "invalid_user" como ID de cuenta.\n
    3. Ingresar "invalid_password" como contraseña.\n
    4. Confirmar que el inicio de sesión falla con el mensaje "ID de cuenta o contraseña incorrectos."\n

    Resultado esperado:\n
    ID de cuenta o contraseña incorrectos.\n
    """
    pass

def test_creacion_cuenta_existente():
    """
    Prueba 10: Intento de creación de una cuenta ya existente\n

    Pasos:\n
    1. Seleccionar la opción "2. Crear cuenta" del menú principal.\n
    2. Ingresar "test_user_9120" como ID de cuenta.\n
    3. Ingresar "test_password" como contraseña.\n
    4. Confirmar que la creación de la cuenta falla con el mensaje "La cuenta ya existe."\n

    Resultado esperado:\n
    La cuenta ya existe.\n
    """
    pass

def test_retiro_sin_fondos():
    """
    Prueba 11: Retiro de una cuenta sin fondos\n

    Pasos:\n
    1. Seleccionar la opción "3. Retirar" del menú de usuario.\n
    2. Ingresar "750.0" como cantidad a retirar.\n
    3. Confirmar que el retiro falla con el mensaje "Fondos insuficientes."\n

    Resultado esperado:\n
    Fondos insuficientes.\n
    """
    pass

def test_transferencia_cuenta_no_existente():
    """
    Prueba 12: Transferencia a una cuenta no existente\n

    Pasos:\n
    1. Seleccionar la opción "4. Transferir" del menú de usuario.\n
    2. Ingresar "non_existent_account" como cuenta de destino.\n
    3. Ingresar "25.0" como cantidad a transferir.\n
    4. Confirmar que la transferencia falla con el mensaje "Una o ambas cuentas no existen."\n

    Resultado esperado:\n
    Una o ambas cuentas no existen.\n
    """
    pass

def test_deposito_negativo():
    """
    Prueba 13: Ingreso de valores negativos en depósitos\n

    Pasos:\n
    1. Seleccionar la opción "2. Depositar" del menú de usuario.\n
    2. Ingresar "-100.0" como cantidad a depositar.\n
    3. Confirmar que el depósito falla con el mensaje "La cantidad a depositar debe ser positiva."\n

    Resultado esperado:\n
    La cantidad a depositar debe ser positiva.\n
    """
    pass
