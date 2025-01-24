""" Se usaron las siguientes paginas de referencia
s
https://www.geeksforgeeks.org/python-program-to-convert-binary-to-ascii/

https://www.geeksforgeeks.org/python-program-to-convert-ascii-to-binary/

https://stackoverflow.com/questions/19414093/how-to-xor-binary-with-python
 """



base64_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
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




""" 

7. Realizar la creación de un script que permita generar llaves dinámicas (utilizar ASCII)
8. Realizar la creación de un script que generar un nuevo cypher en ASCII con una llave k de tamaño fijo 
9. Realizar la creación de un script que generar un nuevo cypher en ASCII con una llave k de tamaño dinámico 
"""