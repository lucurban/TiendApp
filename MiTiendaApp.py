'''
Este programa hace registro de ventas y modifica el inventario de una tienda
'''

# --- Importar paquetes
import pandas as pd

# --- Definir la clase inventario
class tienda:
    def __init__(self, inventario, producto):
        self.inventario = inventario
        self.producto = producto

    # --- Metodo de lectura del inventario
    def leer_inventario(self):
        try:
            df_inventario = pd.read_excel(self.inventario)

            for index, row in df_inventario.iterrows():
                if row['Producto'] == self.producto:
                    print(f'En inventario quedan {row['Cantidad']} {row['Unidad']} de {row['Producto']}')

                    return True
            
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

            with pd.ExcelWriter('Inventario_1.xlsx', mode='a',if_sheet_exists='overlay') as writer:
                nuevo_producto.to_excel(writer, sheet_name='Inventario', startrow=cant_productos+1, index=False, header=False)

            return f'{self.producto} se agrego al inventario con exito'
        
        except FileNotFoundError:
            with pd.ExcelWriter('Inventario_1.xlsx', mode='w') as writer:
                nuevo_producto.to_excel(writer, sheet_name='Inventario', index=False)

            return f'{self.producto} se agrego al inventario con exito'
        
    # --- Metodo para vender productos
    def vender(self):
        pass
        


# --- Declarar hoja de datos
inv = 'Inventario_1.xlsx'

# --- Definir producto a revisar
prod = 'Esencia'
#prod = 'Bolsa de Regalo'
#prod = 'Splash Pink'

# --- Definir el data frame de inventario como un objeto de la clase tienda
df_inventario = tienda(inv, prod)

# --- Leer el data frame de inventario
prod_en_inventario = df_inventario.leer_inventario()

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

df_inv = pd.read_excel(inv)

print(df_inv)

# --- Vender un producto
df_venta = pd.DataFrame(columns=['Producto', 'Cantidad', 'Unidad'])
agregar_producto = True

while agregar_producto:
    resp_correcta = False
    prod_venta = input('Que producto deseas: ')

    for index, row in df_inv.iterrows():
        if row['Producto'] == prod_venta:
            und = row['Unidad']
            cant_inv = row['Cantidad']

    if cant_inv > 0:
        if und == 'unidades':
            cant = int(input(f'cuantas {und} de {prod_venta} deseas: '))

        elif und == 'gramos':
            cant = int(input(f'cuantos {und} de {prod_venta} deseas: '))

    df_venta.loc[len(df_venta)] = [prod_venta, cant, und]

    while resp_correcta == False:
        nuevo_prod = input('¿Deseas algo mas? s|n: ')

        if nuevo_prod == 's':
            agregar_producto = True
            resp_correcta = True

        elif nuevo_prod == 'n':
            agregar_producto = False
            print('Ok!')
            resp_correcta = True

        else:
            resp_correcta = False

print(df_venta)



'''
df_inv.loc[len(df_inv)] = ['Loción Lotus', 14, 'unidades']

print(df_inv)
'''