'''
Este programa hace registro de ventas y actualiza el inventario de una tienda
'''

# --- Importar paquetes
import pandas as pd
from openpyxl import load_workbook

# --- Definir la clase inventario
class tienda:
    def __init__(self, inventario, producto=''):
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
        
    # --- Metodo para revisar el inventario
    def revisar(self):
        try:
            df_inventario = pd.read_excel(self.inventario)

            print('\n', df_inventario)

            #return True

        except FileNotFoundError:
            print('\nAun no se ha creado un inventario')

            #return False

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
            df_precios = pd.read_excel(self.inventario, sheet_name='Precios')
            cant_productos = len(df_inventario)
            cant_prod_precios = len(df_precios)

            with pd.ExcelWriter(self.inventario, 
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
                                       sheet_name='Precios',
                                       startrow=cant_prod_precios+1,
                                       index=False,
                                       header=False
                                       )

            print(f'{self.producto} se agrego al inventario con exito')
        
        except FileNotFoundError:
            with pd.ExcelWriter(self.inventario,
                                mode='w') as writer:
                df_nuevo_producto.to_excel(writer,
                                           sheet_name='Inventario',
                                           index=False
                                           )
                
                df_precios_np.to_excel(writer,
                                       sheet_name='Precios',
                                       index=False
                                       )

            print(f'{self.producto} se agrego al inventario con exito')
        
    # --- Metodo para actualizar los precios del inventario
    def actualizar_precios(self):
        pass
        
    # --- Metodo para vender productos
    def vender(self):
        df_venta = pd.DataFrame(columns=['Fecha', 'Producto', 'Cantidad', 'Unidad', 'Precio', 'Subtotal'])
        df_inventario = pd.read_excel(self.inventario, sheet_name='Inventario')
        df_precios = pd.read_excel(self.inventario, sheet_name='Precios')
        nuevo_prod = self.producto
        agregar_producto = True

        while agregar_producto:

            for index, row in df_inventario.iterrows():
                if row['Producto'] == nuevo_prod:
                    fecha = pd.Timestamp.today().date()
                    cant_inv = row['Cantidad']
                    und = row['Unidad']

            for index, row in df_precios.iterrows():
                if row['Producto'] == nuevo_prod:
                    precio = row['Precio Venta']

            if cant_inv > 0:
                if und == 'unidades':
                    cant = int(input(f'cuantas {und} de {nuevo_prod} deseas: '))

                elif und == 'gramos':
                    cant = int(input(f'cuantos {und} de {nuevo_prod} deseas: '))

            subtotal = cant * precio

            df_venta.loc[len(df_venta)] = [fecha, nuevo_prod, cant, und, precio, subtotal]

            total = df_venta['Subtotal'].sum()

            resp_correcta = False

            while resp_correcta == False:
                print(df_venta)
                print(f'Total a pagar: {total}')

                otro_prod = input('¿Deseas algo mas? s|n: ')

                if otro_prod == 's':
                    nuevo_prod = input('¿Que producto deseas?: ')
                    
                    agregar_producto = True
                    resp_correcta = True

                elif otro_prod == 'n':
                    print(df_venta)
                    print(f'Total a pagar: {total}')
                    agregar_producto = False
                    resp_correcta = True

                    try:
                        libro = load_workbook(self.inventario)
                        hojas = libro.sheetnames

                    except FileNotFoundError:
                        hojas = []


                    if 'Ventas' in hojas:
                        df_ventas_dia = pd.read_excel(self.inventario, sheet_name='Ventas')

                        with pd.ExcelWriter(self.inventario,
                                            mode='a',
                                            if_sheet_exists='overlay'
                                            ) as writer:
                            df_venta.to_excel(writer,
                                              sheet_name='Ventas', 
                                              startrow=len(df_ventas_dia)+1, 
                                              index=False, 
                                              header=False
                                              )
                            
                    else:
                        with pd.ExcelWriter(self.inventario,
                                            mode='a',
                                            if_sheet_exists='new'
                                            ) as writer:
                            df_venta.to_excel(writer,
                                              sheet_name='Ventas', 
                                              index=False, 
                                              header=True
                                              )
                    
                    print('Venta registrada con exito')
                    print('Vuelve pronto!')
                    return df_venta

                else:
                    print('La opción ingresada no es valida')
                    resp_correcta = False

    # --- Metodo para actualizar el inventario despues de una venta
    def actualizar_inventario(self, venta):
        print('Actualizando inventario...')
        df_venta = venta
        df_inventario = pd.read_excel(self.inventario, sheet_name='Inventario')

        for index, row in df_venta.iterrows():
                for index2, row2 in df_inventario.iterrows():
                    if row['Producto'] == row2['Producto']:
                            row2['Cantidad'] = row2['Cantidad'] - row['Cantidad']
                            df_inventario.at[index2, 'Cantidad'] = row2['Cantidad']
                            
        with pd.ExcelWriter(self.inventario,
                            mode='a',
                            if_sheet_exists='overlay'
                            ) as writer:
             df_inventario.to_excel(writer,
                               sheet_name='Inventario', 
                               index=False, 
                               header=True
                               )

        print('Inventario actualizado con exito')


# --- Inicio del programa principal
# --- Declarar hoja de datos
inv = 'Tienda.xlsx'

# --- Definir el inventario como un objeto de la clase tienda
inventario = tienda(inv)

# --- Menu principal
print('\nBienvenido a la tienda')

opcion_valida = False

while opcion_valida == False:
    print('\n¿Qué deseas hacer?')

    opcion = int(input('1 -> Revisar el inventario \n' \
                       '2 -> Agregar un producto al inventario \n' \
                       '3 -> Vender productos \n' \
                       '4 -> Salir \n' \
                       '\nIngresa el numero de la opcion deseada: '))

    if (opcion < 1) or (opcion > 4):
        print('La opción ingresada no es valida')
        print('Por favor ingresa un numero del 1 al 4')

        opcion_valida = False

    elif opcion == 1:
        inventario.revisar()

        opcion_valida = False

    elif opcion == 2:
        prod = input('¿Que producto deseas agregar al inventario? ')
        
        inventario = tienda(inv, prod)

        prod_en_inventario = inventario.leer_inventario()

        if prod_en_inventario:
            print(f'{prod} ya se encuentra en el inventario')

        else:
            inventario.agregar()
        
        opcion_valida = False


    elif opcion == 3:
        prod_venta = input('¿Que producto deseas? ')

        venta = tienda(inv, prod_venta)
        ultima_venta = venta.vender()

        inventario.actualizar_inventario(ultima_venta)

        opcion_valida = False

    elif opcion == 4:
        print('Hasta pronto!')

        opcion_valida = True