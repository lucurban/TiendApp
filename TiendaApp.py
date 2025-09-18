'''
Este programa hace registro de ventas y actualiza el inventario de una tienda
'''

# --- Importar paquetes
import pandas as pd
from openpyxl import load_workbook

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
                   return True
            
            return False
                
        except FileNotFoundError:
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

        precio_compra = int(input('Ingresa el precio de compra: '))
        precio_venta = int(input('Ingresa el precio de venta: '))
        utilidad = precio_venta - precio_compra

        df_nuevo_producto = pd.DataFrame({'Producto': [self.producto],
                                       'Cantidad': [cantidad],
                                       'Unidad': [unidad]
                                       }) 

        df_precios_np = pd.DataFrame({'Producto': [self.producto],
                                   'Precio Compra': [precio_compra],
                                   'Precio Venta': [precio_venta],
                                   'Utilidad': [utilidad]
                                   })

        try:
            df_inventario = pd.read_excel(self.inventario, sheet_name='Inventario')
            #df_precios = pd.read_excel(self.inventario, sheet_name='precios')
            cant_productos = len(df_inventario)

            with pd.ExcelWriter('Inventario_1.xlsx', 
                                mode='a',
                                if_sheet_exists='overlay'
                                ) as writer:
                df_nuevo_producto.to_excel(writer,
                                           sheet_name='Inventario',
                                           startrow=cant_productos+1,
                                           index=False,
                                           header=False
                                           )
                
                df_precios_np.to_excel(writer,
                                       sheet_name='precios',
                                       startrow=cant_productos+1,
                                       index=False,
                                       header=False
                                       )

            return f'{self.producto} se agrego al inventario con exito'
        
        except FileNotFoundError:
            with pd.ExcelWriter('Inventario_1.xlsx',
                                mode='w') as writer:
                df_nuevo_producto.to_excel(writer,
                                           sheet_name='Inventario',
                                           index=False
                                           )
                
                df_precios_np.to_excel(writer,
                                       sheet_name='precios',
                                       startrow=cant_productos+1,
                                       index=False
                                       )

            return f'{self.producto} se agrego al inventario con exito'
        
    # --- Metodo para actualizar los precios del inventario
    def actualizar_precios(self):
        pass
        
    # --- Metodo para vender productos
    def vender(self):
        df_venta = pd.DataFrame(columns=['Fecha', 'Producto', 'Cantidad', 'Unidad'])
        df_inventario = pd.read_excel(self.inventario)
        nuevo_prod = self.producto
        agregar_producto = True

        while agregar_producto:
            resp_correcta = False

            for index, row in df_inventario.iterrows():
                if row['Producto'] == nuevo_prod:
                    fecha = pd.Timestamp.today().date()
                    cant_inv = row['Cantidad']
                    und = row['Unidad']

            if cant_inv > 0:
                if und == 'unidades':
                    cant = int(input(f'cuantas {und} de {nuevo_prod} deseas: '))

                elif und == 'gramos':
                    cant = int(input(f'cuantos {und} de {nuevo_prod} deseas: '))

            df_venta.loc[len(df_venta)] = [fecha, nuevo_prod, cant, und]

            while resp_correcta == False:
                print(df_venta)

                otro_prod = input('¿Deseas algo mas? s|n: ')

                if otro_prod == 's':
                    nuevo_prod = input('¿Que producto deseas?: ')
                    
                    agregar_producto = True
                    resp_correcta = True

                elif otro_prod == 'n':
                    agregar_producto = False
                    resp_correcta = True

                    try:
                        libro = load_workbook(self.inventario)
                        hojas = libro.sheetnames

                    except FileNotFoundError:
                        hojas = []


                    if 'ventas' in hojas:
                        df_ventas_dia = pd.read_excel(self.inventario, sheet_name='ventas')

                        with pd.ExcelWriter('Inventario_1.xlsx',
                                            mode='a',
                                            if_sheet_exists='overlay'
                                            ) as writer:
                            df_venta.to_excel(writer,
                                              sheet_name='ventas', 
                                              startrow=len(df_ventas_dia)+1, 
                                              index=False, 
                                              header=False
                                              )
                            
                    else:
                        with pd.ExcelWriter('Inventario_1.xlsx',
                                            mode='a',
                                            if_sheet_exists='new'
                                            ) as writer:
                            df_venta.to_excel(writer,
                                              sheet_name='ventas', 
                                              index=False, 
                                              header=True
                                              )
                    
                    print('Venta registrada con exito')
                    print('Vuelve pronto!')

                else:
                    print('La opción ingresada no es valida')
                    resp_correcta = False

                #Continuar aqui


# --- Declarar hoja de datos
inv = 'Inventario_1.xlsx'

# --- Definir producto a revisar
#prod = 'Esencia'
prod = 'Bolsa de Regalo'
#prod = 'Splash Pink'

# --- Definir el inventario como un objeto de la clase tienda
inventario = tienda(inv, prod)

# --- Leer el inventario
prod_en_inventario = inventario.leer_inventario()

resp_correcta = False

try:
    df_inv = pd.read_excel(inv)

# --- Agregar un productos al inventario
except FileNotFoundError:
    print(f'{prod} no se encuentra en el inventario')

    nuevo_prod = input(f'¿Deseas incluir {prod} en el inventario? s|n: ')

    while resp_correcta == False:
        if nuevo_prod == 's':
            agregar = inventario.agregar()
 
            print(agregar)

            resp_correcta = True

        elif nuevo_prod == 'n':
            print(f'{prod} no será agregado al inventario')
                
            resp_correcta = True

        else:
            resp_correcta = False

# --- Leer el inventario
if prod_en_inventario:
    for index, row in df_inv.iterrows():
        if row['Producto'] == prod:
            print(f'En inventario quedan {row['Cantidad']} {row['Unidad']} de {row['Producto']}')

# --- Agregar un producto al inventario
else:
    while resp_correcta == False:
        print(f'{prod} no se encuentra en el inventario')

        nuevo_prod = input(f'¿Deseas incluir {prod} en el inventario? s|n: ')

        if nuevo_prod == 's':
            agregar = inventario.agregar()
 
            print(agregar)

            resp_correcta = True

        elif nuevo_prod == 'n':
            print(f'{prod} no será agregado al inventario')
                
            resp_correcta = True

        else:
            resp_correcta = False




#df_inv = pd.read_excel(inv)
#print(df_inv)

# --- Vender productos
prod_venta = input('¿Que producto deseas? ')

# --- Definir venta como un objeto de la clase tienda
venta = tienda(inv, prod_venta)

venta.vender()