'''
Este programa hace registro de ventas y modifica el inventario de una tienda
'''
# --- Importar paquetes
import pandas as pd

inventario = 'Inventario.xlsx'

df_inventario = pd.read_excel(inventario)

print(df_inventario)


print(df_inventario['Cantidad'] = )

'''
df_add_inventario = pd.DataFrame([['Loción California', 16, 'und']],
                     index=[7],
                     columns=['Producto', 'Cantidad', 'Unidad'])

with pd.ExcelWriter(inventario, mode='a') as writer:
    df_add_inventario.to_excel(writer, 'sheet2')
    
print(df_inventario)

producto = input('producto: ')

verificar = df_inventario['Cantidad'] = producto

print(verificar)
'''