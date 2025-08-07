'''
Este programa hace registro de ventas y modifica el inventario de una tienda
'''

# --- Importar paquetes
import pandas as pd

# --- Definir la clase inventario
class inventario:
    def __init__(self, inventario, producto):
        self.inventario = inventario
        self.producto = producto

    # --- Metodo de lectura del inventario
    def leer(self):
        try:
            df_inventario = pd.read_excel(self.inventario)

            for index, row in df_inventario.iterrows():
                if row['Producto'] == self.producto:
                    print(f'En inventario quedan {row['Cantidad']} {row['Unidad']} de {row['Producto']}')

                    return True
            
                else:
                    print(f'{self.producto} no se encuentra en el inventario')

                    return False
                
        except FileNotFoundError:
            print(f'{self.producto} no se encuentra en el inventario')

            return False

    # --- Metodo para agregar un producto al inventario
    def agregar(self):
        cantidad = int(input(f'Ingresa la cantidad de {self.producto} que debe ingresarse al inventario: '))
        und_correcta = False

        while und_correcta == False:
                unidad = input(f'{self.producto} se mide en gramos o unidades: ')

                if (unidad == 'gramos') or (unidad == 'unidades'):
                    und_correcta = True

                else:
                    print('La unidad especificada no es correcta')

        nuevo_producto = pd.DataFrame({'Producto': [self.producto],
                                       'Cantidad': [cantidad],
                                       'Unidad': [unidad]}) 
        
        try:
            df_inventario = pd.read_excel(self.inventario)
            cant_productos = len(df_inventario)

            with pd.ExcelWriter('Inventario_2.xlsx', mode='a',if_sheet_exists='overlay') as writer:
                nuevo_producto.to_excel(writer, sheet_name='Inventario', startrow=cant_productos+1, index=False, header=False)

            return f'{self.producto} se agrego al inventario con exito'
        
        except FileNotFoundError:
            with pd.ExcelWriter('Inventario_2.xlsx', mode='w') as writer:
                nuevo_producto.to_excel(writer, sheet_name='Inventario', index=False)

            return f'{self.producto} se agrego al inventario con exito'


# --- Declarar hoja de datos
inv = 'Inventario_2.xlsx'

# --- Definir producto a revisar
#prod = 'Esencia'
prod = 'Bolsa de Regalo'

# --- Definir data frame como un objeto de la clase inventario
df_inventario = inventario(inv, prod)

# --- Leer el data frame
prod_en_inventario = df_inventario.leer()

# --- Agregar un producto al inventario

resp_correcta = False

if prod_en_inventario == False:
    while resp_correcta == False:
        nuevo_prod = input(f'¿Deseas incluir {prod} en el inventario? s|n: ')

        if nuevo_prod == 's':
            agregar = df_inventario.agregar()
 
            print(agregar)

            resp_correcta = True

        elif nuevo_prod == 'n':

            print(f'{prod} no será agregado al inventario')

            resp_correcta = True

        else:
            resp_correcta = False
