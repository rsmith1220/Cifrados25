import random
import pandas as pd
from prettytable import PrettyTable

def simular_bb84(n=20, con_eve=False):
    bits_alice = [random.randint(0, 1) for _ in range(n)]
    bases = ['↕', '↗']
    bases_alice = [random.choice(bases) for _ in range(n)]
    bases_bob = [random.choice(bases) for _ in range(n)]

    polarization_map = {
        ('↕', 0): '↑', ('↕', 1): '↓',
        ('↗', 0): '↗', ('↗', 1): '↙'
    }

    fotones = [polarization_map[(base, bit)] for base, bit in zip(bases_alice, bits_alice)]

    bits_bob = []
    for i in range(n):
        if con_eve:
            base_eve = random.choice(bases)
            if base_eve == bases_alice[i]:
                intercepted_bit = bits_alice[i]
            else:
                intercepted_bit = random.randint(0, 1)
            # reenviado con base de Eve
            if bases_bob[i] == base_eve:
                bit_bob = intercepted_bit
            else:
                bit_bob = random.randint(0, 1)
        else:
            if bases_bob[i] == bases_alice[i]:
                bit_bob = bits_alice[i]
            else:
                bit_bob = random.randint(0, 1)
        bits_bob.append(bit_bob)

    coincidencias = [bases_alice[i] == bases_bob[i] for i in range(n)]
    clave_secreta = [bits_bob[i] for i in range(n) if coincidencias[i]]

    tabla = PrettyTable()
    tabla.field_names = [
        "N°", "Bit de Alice", "Base de Alice", "Fotón",
        "Base de Bob", "Bit recibido por Bob", "¿Bases coinciden?", "¿Usar bit?"
    ]

    for i in range(n):
        tabla.add_row([
            i + 1,
            bits_alice[i],
            bases_alice[i],
            fotones[i],
            bases_bob[i],
            bits_bob[i],
            'sí' if coincidencias[i] else 'no',
            'sí' if coincidencias[i] else 'no'
        ])

    print(tabla)
    print("\nClave secreta:", clave_secreta)
    print(f"Total de bits usados: {len(clave_secreta)} ({100 * len(clave_secreta) / n:.2f}%)")

if __name__ == "__main__":
    simular_bb84(n=20, con_eve=False)  # Cambiar a con_eve=True para incluir a Eve