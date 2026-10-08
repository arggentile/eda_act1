from sympy import randprime, mod_inverse
from math import gcd

class Rsa:
    """
    Implementación demostrativa de RSA.
    """
    def __init__(self, bits=1024):
        # Generamos dos primos grandes p y q, de 'bits' bits cada uno.
        self.__p = self.__primo_grande(bits)
        self.__q = self.__primo_grande(bits)

        # Nos aseguramos que p != q (muy improbable que coincidan, pero por las dudas)
        while self.__p == self.__q:
            self.__q = self.__primo_grande(bits)


        # n es el módulo público, producto de los dos primos.
        # Su longitud (en bits) es el "tamaño" de la clave RSA.
        self.__n = self.__p * self.__q
       
        self.__phi = self.__calcular_euler()

        # Generamos el par de claves (pública y privada)
        self.__clave_publica = None
        self.__clave_privada = None
        self.__generar_claves()

    def __primo_grande(self, bits):
        """ Genera un numro primo grande """
        return randprime(2**(bits - 1), 2**bits)

    def __calcular_euler(self):
        """
        Calcula phi(n) = (p - 1) * (q - 1).
        Esto funciona porque p y q son primos: la cantidad de números coprimos
        con n menores que n es exactamente (p-1)(q-1).
        """
        return (self.__p - 1) * (self.__q - 1)

    def __generar_claves(self):
        """
        Genera el par de claves RSA.
        - Clave pública: (e, n)  -> para cifrar / verificar firmas
        - Clave privada: (d, n)  -> para descifrar / firmar
        """
        # e es el exponente público. Se usa 65537 por convención: es primo,
        # tiene pocos bits en 1 (10000000000000001), lo que hace el cifrado rápido,
        # y es lo suficientemente grande para evitar ataques por e chico.
        e = 65537

        # Verificamos que gcd(e, phi) == 1, condición necesaria para que exista
        # el inverso modular. Con primos de 1024 bits y e = 65537 casi siempre se cumple,
        # pero el chequeo es barato.
        if gcd(e, self.__phi) != 1:
            raise ValueError("e y phi(n) no son coprimos, regenerar primos")

        # d es el inverso modular de e módulo phi(n).
        # Es decir: (e * d) mod phi(n) == 1.
        # Este es el "secreto" matemático de RSA.
        d = mod_inverse(e, self.__phi)

        self.__clave_publica = (e, self.__n)
        self.__clave_privada = (d, self.__n)

    def obtener_clave_publica(self):
        """Devuelve la clave pública (e, n) para compartir con otros."""
        return self.__clave_publica

    def obtener_clave_privada(self):
        """
        Devuelve la clave privada (d, n).
        En un sistema real NO se expondría así; está acá solo para fines didácticos.
        """
        return self.__clave_privada

    def cifrar(self, mensaje, clave_publica=None):
        """
        Cifra un mensaje usando una clave pública.
        Si no se pasa una, usa la propia (útil para pruebas).

        Fórmula: c = m^e mod n

        El mensaje debe ser un entero menor que n.
        """
        if clave_publica is None:
            clave_publica = self.__clave_publica

        e, n = clave_publica

        if isinstance(mensaje, str):
            # Convertimos el string a un entero usando sus bytes
            mensaje = int.from_bytes(mensaje.encode("utf-8"), "big")

        if mensaje >= n:
            raise ValueError("El mensaje es demasiado grande para esta clave")

        # pow(base, exp, mod) hace exponenciación modular eficiente
        return pow(mensaje, e, n)

    def descifrar(self, mensaje_cifrado):
        """
        Descifra un mensaje usando la clave privada propia.

        Fórmula: m = c^d mod n
        """
        d, n = self.__clave_privada
        mensaje = pow(mensaje_cifrado, d, n)
        return mensaje

    def descifrar_a_texto(self, mensaje_cifrado):
        """Descifra y convierte el entero resultante nuevamente a string."""
        mensaje_int = self.descifrar(mensaje_cifrado)
        # Calculamos cuántos bytes ocupa el número para reconstruir el string original
        longitud = (mensaje_int.bit_length() + 7) // 8
        return mensaje_int.to_bytes(longitud, "big").decode("utf-8")


if __name__ == "__main__":
    print("Generando claves RSA (puede tardar unos segundos)...")
    rsa = Rsa(bits=1024)

    print("\nClave pública (e, n):")
    e, n = rsa.obtener_clave_publica()
    print(f"  e = {e}")
    print(f"  n = {n}")

    mensaje_original = "Hola RSA, esto es una prueba"
    print(f"\nMensaje original: {mensaje_original}")

    cifrado = rsa.cifrar(mensaje_original)
    print(f"\nMensaje cifrado (entero):\n  {cifrado}")

    descifrado = rsa.descifrar_a_texto(cifrado)
    print(f"\nMensaje descifrado: {descifrado}")

    # Verificación
    assert descifrado == mensaje_original, "El descifrado no coincide con el original"
    print("\n✔ Cifrado y descifrado correctos.")