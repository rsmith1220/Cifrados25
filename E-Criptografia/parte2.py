""" Se usaron las siguientes paginas de referencia

https://www.geeksforgeeks.org/python-program-to-convert-binary-to-ascii/

https://www.geeksforgeeks.org/python-program-to-convert-ascii-to-binary/

https://stackoverflow.com/questions/19414093/how-to-xor-binary-with-python

https://chatgpt.com/share/679425b0-63f4-8005-a65e-feec683133d2
 """


""" EJEMPLOS 

Ingrese ASCII para pasar a binario: hola
Binario: 01101000 01101111 01101100 01100001

Ingrese el texto de base64 para binario: SGVsbG8=
010010000110010101101100011011000110111100

Ingrese texto binario para base64: 01100001
YQ=

Ingrese el binario para pasar a ASCII: 01100001
ASCII desde binario ingresado:  a

Ingrese texto base64 para ASCII: SGVsbG8=
Texto base64 a ASCII

Ingrese le primer binario: 01100001
Ingrese el segundo binario: 01101100
Resultado de XOR entre 01100001 y 01101100: 00001101

Ingrese la longitud de la llave a generar: 14
Llave generada: M]ny^ F21/BmYf

Ingrese la llave (sin espacios)buenas
Ingrese el mensaje a cifrar: holaa
Mensaje cifrado: n1+##

Ingrese la llave (sin espacios)tardes
Ingrese el mensaje a cifrar: solecito
Mensaje cifrado: 'Ug?13sU


"""

import random

base64_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

ascii_imprimibles = [chr(i) for i in range(32, 127)]  # Del espacio (' ') al '~'
permutacion = ascii_imprimibles[:]

""" 
1. Realizar la creación de un script que permita la conversión de palabras en texto ASCII a BINARIO 
"""
input1 = input("Ingrese ASCII para pasar a binario: ")

#pasa cada caracter a binario
b_repr = ' '.join(format(ord(char), '08b') for char in input1)

print("Binario:", b_repr)



""" 2. Realizar la creación de un script que permita la conversión de palabras en texto BASE64 a BINARIO
 """

def base64_a_binario(base64_string):
    # Crear un diccionario de decodificación para Base64
    
    base64_dict = {char: index for index, char in enumerate(base64_chars)}
    
    # Eliminar caracteres de relleno '=' y preparar los bits
    base64_string = base64_string.rstrip('=')
    bits = ""
    for char in base64_string:
        if char not in base64_dict:
            raise ValueError("Cadena Base64 inválida")
        # Obtener el índice del carácter y convertirlo a binario de 6 bits
        bits += f"{base64_dict[char]:06b}"
    
    return bits


base64_string = input("\nIngrese el texto de base64 para binario: ")
binario = base64_a_binario(base64_string)
print(binario)



""" 3. Realizar la creación de un script que permita la conversión de BINARIO a BASE64 """

def binario_a_base64(bin_string):
    
    # Asegurarse de que la longitud de la cadena binaria sea múltiplo de 6
    while len(bin_string) % 6 != 0:
        bin_string += "0"
    
    # Dividir en bloques de 6 bits
    bloques = [bin_string[i:i+6] for i in range(0, len(bin_string), 6)]
    
    # Convertir cada bloque a decimal y luego a Base64
    base64_string = ""
    for bloque in bloques:
        decimal = int(bloque, 2)
        base64_string += base64_chars[decimal]
    
    # Calcular y añadir el relleno '=' si es necesario
    relleno = len(bin_string) % 24
    if relleno:
        base64_string += "=" * ((24 - relleno) // 8)
    
    return base64_string


bin_string = input("\nIngrese texto binario para base64: ")
base64_string = binario_a_base64(bin_string)
print(base64_string)



""" 
4. Realizar la creación de un script que permita la conversión de BINARIO a ASCII
"""
def binascii(bits):
	return ''.join([chr(int(i, 2)) for i in bits])

# Driver Code
input2 = input("\nIngrese el binario para pasar a ASCII: ")
# This is the binary equivalent of string "GFG"
bin_values = [input2] 

# calling the function
# and storing the result in variable 's'
s = binascii(bin_values)

# Printing the result
print("ASCII desde binario ingresado: ",s)

""" 
5. Realizar la creación de un script que permita la conversión de BASE64 a ASCII 

    Recuerda pasar por binario para poder hacer las conversiones
"""

input5=input("\nIngrese texto base64 para ASCII: ")
bin5=base64_a_binario(input5)
as5=binascii(bin5)

print("Texto base64 a ASCII "+as5)


""" 6. Realizar la creación de un script que permita aplicar XOR a un BINARIO  """


def aplicar_xor(binario1, binario2):
    # Verificar que las cadenas tengan la misma longitud
    if len(binario1) != len(binario2):
        raise ValueError("Las cadenas binarias deben tener la misma longitud")
    
    # Aplicar XOR bit a bit
    resultado = ""
    for b1, b2 in zip(binario1, binario2):
        # Convertir los bits a enteros, aplicar XOR, y agregar al resultado
        xor_bit = int(b1) ^ int(b2)
        resultado += str(xor_bit)
    
    return resultado

binario1 = input("\nIngrese el primer binario: ")
binario2 = input("Ingrese el segundo binario: ")
resultado_xor = aplicar_xor(binario1, binario2)
print(f"Resultado de XOR entre {binario1} y {binario2}: {resultado_xor}")


""" 7. Realizar la creación de un script que permita generar llaves dinámicas (utilizar ASCII) """



def generar_llave_ascii(longitud):
    """
    Genera una llave dinámica utilizando caracteres ASCII imprimibles.
    
    :param longitud: Longitud de la llave deseada.
    :return: Una cadena representando la llave.
    """
    # Rango de caracteres ASCII imprimibles
    ascii_imprimibles = [chr(i) for i in range(32, 127)]  # Del espacio (' ') al '~'
    
    # Generar llave seleccionando caracteres aleatorios
    llave = ''.join(random.choice(ascii_imprimibles) for _ in range(longitud))
    return llave

# Ejemplo de uso
try:
    longitud_llave=int(input("\nIngrese la longitud de la llave a generar: "))
except:
    print("No se ha ingresado un numero valido, se usara el default(16)")
    longitud_llave = 16  # Define la longitud deseada para la llave
llave_generada = generar_llave_ascii(longitud_llave)
print(f"Llave generada: {llave_generada}")

""" 8. Realizar la creación de un script que generar un nuevo cypher en ASCII con una llave k de tamaño fijo  """



def generar_cifrado_ascii(llave):
    """
    Genera un nuevo cifrado ASCII basado en una llave de tamaño fijo.
    
    :param llave: Una cadena que actúa como llave (de tamaño fijo).
    :return: Un diccionario que mapea caracteres originales a caracteres cifrados.
    """
    # Rango de caracteres ASCII imprimibles
    
    
    # Generar semilla basada en la llave
    random.seed(llave)
    
    # Crear una permutación de los caracteres imprimibles
    
    random.shuffle(permutacion)
    
    # Crear el diccionario de mapeo
    cifrado = {original: cifrado for original, cifrado in zip(ascii_imprimibles, permutacion)}
    return cifrado

def cifrar_mensaje(mensaje, cifrado):
    """
    Cifra un mensaje usando el cifrado generado.
    
    :param mensaje: La cadena original a cifrar.
    :param cifrado: El diccionario de cifrado generado.
    :return: El mensaje cifrado.
    """
    return ''.join(cifrado[char] if char in cifrado else char for char in mensaje)

# Ejemplo de uso
llave = input("\nIngrese la llave (sin espacios)")
mensaje_original = input("Ingrese el mensaje a cifrar: ")

# Generar el cifrado
cifrado = generar_cifrado_ascii(llave)

# Cifrar el mensaje
mensaje_cifrado = cifrar_mensaje(mensaje_original, cifrado)
print(f"Mensaje cifrado: {mensaje_cifrado}")






"""9. Realizar la creación de un script que generar un nuevo cypher en ASCII con una llave k de tamaño dinámico """
def generar_cifrado_ascii_dinamico(llave):
    """
    Genera un cifrado ASCII basado en una llave de tamaño dinámico.
    
    :param llave: Una cadena que actúa como llave (de tamaño dinámico).
    :return: Un diccionario que mapea caracteres originales a caracteres cifrados.
    """
    
    # Convertir la llave a un valor numérico como semilla
    semilla = sum(ord(char) for char in llave)
    random.seed(semilla)
    
    random.shuffle(permutacion)
    
    # Crear el diccionario de mapeo
    cifrado = {original: cifrado for original, cifrado in zip(ascii_imprimibles, permutacion)}
    return cifrado

def cifrar_dinamico(mensaje, cifrado):
    """
    Cifra un mensaje usando el cifrado generado.
    
    :param mensaje: La cadena original a cifrar.
    :param cifrado: El diccionario de cifrado generado.
    :return: El mensaje cifrado.
    """
    return ''.join(cifrado[char] if char in cifrado else char for char in mensaje)

# Ejemplo de uso
llave = input("\nIngrese la llave (sin espacios)")
mensaje_original = input("Ingrese el mensaje a cifrar: ")

# Generar el cifrado
cifrado = generar_cifrado_ascii_dinamico(llave)

# Cifrar el mensaje
mensaje_cifrado = cifrar_dinamico(mensaje_original, cifrado)
print(f"Mensaje cifrado: {mensaje_cifrado}")
