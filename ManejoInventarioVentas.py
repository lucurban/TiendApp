'''
Este programa hace registro de ventas y modifica el inventario de una tienda
'''
# --- Importar paquetes
import pandas as pd

inventario = 'Inventario.xlsx'

df_inventario = pd.read_excel(inventario)

print(df_inventario)

print(df_inventario['Producto'])
'''
producto = input('producto: ')

verificar = df_inventario['Cantidad'] = producto

print(verificar)
'''