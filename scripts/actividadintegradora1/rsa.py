from sympy import randprime, isprime


class Rsa:
    def __init__(self, ):
        self.__clave_publica
        self.__clave_privada
        self.__p = randprime(2**1023, 2**1024)
        self.__q = randprime(2**1023, 2**1024)
              
    def __calcular_euler(self):
        return (self.__p - 1) * (self.__q - 1)

    def __generar_claves(self):
        """Genera un par de claves RSA (pública y privada)."""
    
        n = self.__p * self.__q
    
        phi = self.__calcular_euler()
    
        e = 65537
    
        d = mod_inverse(e, phi)
        
        # Clave pública: (e, n) | Clave privada: (d, n)
        self.__clave_publica = (e, n)
        self.__clave_privada = (d, n)
        
       
    def __calcular_clave_publica(self):



    def __calcular_clave_privada(self):
       