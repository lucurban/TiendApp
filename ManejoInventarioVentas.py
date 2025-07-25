'''
Este programa hace registro de ventas y modifica el inventario de una tienda
'''
# --- Importar paquetes
import pandas as pd

# --- Definir la clase inventario
class inventario:
    def __init__(self, inv, prod):
        self.inventario = inv
        self.producto = prod

    # --- Metodo de lectura del inventario
    def leer(self):
        df_inventario = pd.read_excel(self.inventario)

        for index, row in df_inventario.iterrows():
            if row['Producto'] == self.producto:
                print(f'En inventario quedan {row['Cantidad']} {row['Unidad']} de {producto}')

# --- Declarar hoja de datos
datos = 'Inventario.xlsx'

# --- Definir producto a revisar
producto = 'Splash Victoria Secret'

# --- Definir data frame como un objeto de la clase inventario
df_inventario = inventario(datos, producto)

# --- Leer el data frame
df_inventario.leer()