

# Simulación del Protocolo BB84 en Python

Este proyecto implementa una simulación del protocolo de Distribución Cuántica de Claves (QKD) BB84, uno de los primeros y más conocidos protocolos cuánticos para el intercambio seguro de claves.

## 🧪 Tecnologías usadas

- **Python**: Lenguaje principal para la simulación.
- **PrettyTable**: Para mostrar resultados en tablas legibles por consola.
- **random**: Para generar secuencias de bits y bases aleatorias.
- **pandas** *(opcional)*: Se puede usar para análisis o exportación de datos.

## 🔐 ¿Qué es BB84?

BB84 es un protocolo de distribución de claves propuesto por Bennett y Brassard en 1984. Se basa en principios de la mecánica cuántica para garantizar que una clave compartida entre dos partes (Alice y Bob) sea secreta y cualquier intento de espionaje (por parte de Eve) pueda ser detectado.

## ✅ ¿Por qué se usó?

- **Seguridad cuántica**: Para ilustrar cómo la física cuántica puede garantizar seguridad sin depender de algoritmos matemáticos complejos.
- **Simplicidad y demostración educativa**: BB84 es ideal para comprender los conceptos básicos de QKD.

## 🔧 Componentes principales

- `simulador.py`: Contiene la lógica del protocolo BB84.
  - Generación de bits y bases.
  - Codificación de fotones.
  - Simulación de Bob y (opcionalmente) Eve.
  - Construcción de la clave secreta.
  - Impresión de resultados con PrettyTable.

## ▶️ Cómo correr el proyecto

1. Clona este repositorio o descarga los archivos.
2. Crea y activa un entorno virtual:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```
3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
4. Ejecuta la simulación:
   ```bash
   python simulador.py
   ```

- Puedes activar a Eve cambiando el parámetro:
  ```python
  simular_bb84(n=20, con_eve=True)
  ```

## 🧠 Ubicación de las tecnologías

| Tecnología    | Usada en                  | Propósito                                       |
|---------------|---------------------------|-------------------------------------------------|
| Python        | Todo el script             | Lógica general, control de flujo                |
| PrettyTable   | `simulador.py`             | Visualización clara de la simulación            |
| random        | `simulador.py`             | Generación de bits, bases y simulaciones aleatorias |
| pandas        | (comentado)                | Puede usarse si se desea análisis/exportación   |

---
Proyecto para la clase de Cifrados 2025 🚀