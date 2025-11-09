<h1 align="center">TiendApp</h1>

<h2>🏷️ Descripción general</h2>
<p>
  TiendaApp es una aplicación desarrollada en <strong>Python</strong> para la gestión de inventarios y ventas de una tienda.
</p>
<p>
  Su objetivo es facilitar el control de productos, precios y movimientos de venta mediante la automatización de tareas que normalmente se realizan de forma manual.
</p>
<p>
  El programa permite consultar el inventario, actualizar existencias y precios, registrar ventas y generar resúmenes de ventas en fechas solicitadas por el usuario, todo ello trabajando directamente sobre un archivo Excel.
</p>
<p>
  Gracias a esto, la información se mantiene organizada y fácilmente accesible, sin necesidad de usar una base de datos compleja.
</p>
<p>
  Este proyecto nació como un ejercicio práctico para aplicar conceptos de programación orientada a objetos (POO) y el manejo de datos con Pandas y Openpyxl, mostrando cómo una solución sencilla puede volverse una herramienta útil y flexible para cualquier pequeño negocio o tienda local.
</p>

<h2>⚙️ Características principales</h2>
<p>
  TiendaApp está pensada para que cualquier persona pueda llevar el control básico de su tienda sin necesidad de conocimientos técnicos avanzados.
</p>
<p>
  Su estructura se basa en tareas simples pero bien organizadas, que reflejan lo que ocurre día a día en un negocio real.
</p>
<p>
  Entre sus principales características se encuentran:
</p>
<ul>
  <li>🧾 <strong>Gestión de inventario:</strong> permite revisar los productos disponibles, sus cantidades y unidades de medida (gramos o unidades).</li>
  <li>✏️ <strong>Actualización de existencias:</strong> ajusta fácilmente las cantidades cuando llegan nuevos productos o se detectan diferencias en el inventario.</li>
  <li>💰 <strong>Control de precios:</strong> mantiene actualizados los precios de compra y venta, calculando automáticamente la utilidad de cada producto.</li>
  <li>🛍️ <strong>Registro de ventas:</strong> guarda las ventas diarias, generando un historial con fecha, producto, cantidad, precio y subtotal.</li>
  <li>📊 <strong>Resumen de ventas:</strong> genera reportes que muestran las ventas realizadas y el total del día en la fecha solicitada por el usuario.</li>
  <li>📁 <strong>Integración con Excel:</strong> usa archivos .xlsx para almacenar toda la información, aprovechando las librerías Pandas y Openpyxl.</li>
</ul>
<p>
  En conjunto, estas funciones permiten que TiendaApp actúe como un pequeño asistente digital de tienda: ordenado, confiable y siempre listo para registrar una nueva venta.
</p>

<h2>🧩 Estructura del proyecto</h2>
<p>
  El proyecto está organizado de forma sencilla para que sea fácil de entender, modificar y ampliar.
</p>
<p>
  Cada parte del código cumple un propósito claro dentro del flujo de la aplicación.
</p>
<p>
  La estructura general es la siguiente:
  <code>
    TiendaApp/
    │
    ├── TiendaApp.py           # Archivo principal del programa (punto de entrada)
    ├── tienda.py              # Archivo que contiene la clase 'tienda' y sus métodos
    ├── Tienda.xlsx            # Archivo Excel donde se guarda el inventario, precios y ventas
    │
    ├── README.md              # Documento de descripción y guía del proyecto
    └── requirements.txt       # (Opcional) Lista de dependencias necesarias, como pandas y openpyxl
</code>
</p>
<h3>📘 Descripción de los componentes</h3>
<ul>
  <li><strong>TiendaApp.py:</strong> Es el corazón del programa. Contiene el menú principal que permite al usuario elegir qué desea hacer (consultar, vender, actualizar, etc.).
  Aquí se crean los objetos de la clase tienda y se orquesta toda la interacción con el usuario.</li>
  <li><strong>tienda.py:</strong> Define la clase tienda, que concentra toda la lógica del programa. Dentro de esta clase se encuentran los métodos encargados de leer, actualizar, vender y resumir la información del inventario.</li>
  <li><strong>Tienda.xlsx:</strong>Es el archivo donde se almacena la información.
  Contiene varias hojas de datos:
    <ul>
      <li><em>Inventario</em> (lista de productos y cantidades)</li>
      <li><em>Precios</em> (precios de compra, venta y utilidad)</li>
      <li><em>Ventas</em> (registro histórico de ventas realizadas)</li>
    </ul>
  </li>
  <li><strong>README.md:</strong> Documento donde se explica qué hace la aplicación, cómo está construida y qué puede lograr el usuario con ella.</li>
  <li><strong>requirements.txt (opcional):</strong> Archivo que lista las dependencias del proyecto (por ejemplo: pandas, openpyxl).
Es útil si en el futuro se desea compartir o ejecutar TiendaApp en otro entorno.</li>
</ul>

<h2>🧠 Conceptos aplicados</h2>
<p>
  TiendaApp combina varios conceptos fundamentales de la programación y del manejo de datos en Python.
</p>
<p>
  La idea es que el código no solo funcione, sino que también sea una buena base para aprender y mejorar como desarrollador.
</p>
<h3>🧩 Programación orientada a objetos (POO)</h3>
<p>
  El proyecto se construye alrededor de una clase llamada tienda.
</p>
<p>
  Esta clase agrupa los datos (como el inventario y las ventas) y las acciones que se pueden realizar sobre ellos (como agregar productos, vender o actualizar precios).
</p>
<p>
  Este enfoque permite:
</p>
<ul>
  <li>Reutilizar código de forma ordenada.</li>
  <li>Mantener una estructura limpia y fácil de extender.</li>
  <li>Trabajar con objetos que representan conceptos del mundo real (en este caso, una tienda).</li>
</ul>
<h3>📊 Manejo de datos con Pandas</h3>
<p>
  TiendaApp utiliza pandas para leer, modificar y escribir los datos que están en hojas de Excel.
</p>
<p>
  Gracias a sus estructuras tipo DataFrame, las operaciones como filtrar productos, calcular subtotales o actualizar cantidades se hacen de forma rápida y legible.
</p>
<p>
  Además, se usa pd.ExcelWriter para escribir en hojas específicas, agregando o sobreescribiendo información sin perder el resto de los datos del archivo.
</p>
<h3>📘 Interacción con archivos Excel (Openpyxl)</h3>
<p>
  La librería <strong>openpyxl</strong> permite verificar y manipular las hojas dentro del archivo Tienda.xlsx. Esto facilita comprobar si existen hojas como “Inventario” o “Ventas” antes de escribir en ellas, y manejar el flujo de datos sin errores.
</p>
<h3>💬 Interacción con el usuario</h3>
<p>
  El programa se ejecuta en consola y guía al usuario con mensajes claros y preguntas paso a paso. Esta interacción hace que TiendaApp sea intuitiva, incluso para alguien sin conocimientos técnicos.
</p>
<h3>🔁 Estructura modular y lógica de flujo</h3>
<p>
  El programa principal (TiendaApp.py) actúa como punto de control: muestra el menú, recibe las opciones y llama a los métodos correspondientes de la clase tienda. Esto crea un flujo natural donde el usuario puede revisar, actualizar, vender o consultar sin complicaciones.
</p>

<h2>📊 Tecnologías utilizadas</h2>
<p>
  TiendaApp está desarrollada completamente en Python, combinando librerías que facilitan el trabajo con datos, la persistencia en archivos y la interacción con el usuario.
</p>
<p>
  A continuación te cuento cuáles son las principales herramientas y por qué se usaron 👇
</p>
<h3>🐍 Python 3</h3>
<p>
  El lenguaje base del proyecto.
<p>
  Su sintaxis clara y legible lo convierte en una excelente opción para crear aplicaciones que manejen datos y automatizaciones sencillas.
</p>
<p>
  Además, su enfoque multipropósito permite que TiendaApp crezca fácilmente con nuevas funciones.
</p>
<h3>🧮 Pandas</h3>
<p>
  Es la columna vertebral del manejo de datos.
</p>
<p>
  Permite trabajar con estructuras tipo DataFrame, que funcionan como tablas de Excel dentro del código.
</p>
<p>
  Con pandas, TiendaApp puede:
  <ul>
    <li>Leer y escribir datos de hojas específicas.</li>
    <li>Calcular subtotales, totales y utilidades.</li>
    <li>Filtrar y actualizar registros con pocas líneas de código.</li>
  </ul>
</p>
<h3>📗 Openpyxl</h3>
<p>
  Se usa para interactuar directamente con los archivos .xlsx.
</p>
<p>
  Gracias a esta librería, TiendaApp puede:
  <ul>
    <li>Verificar si una hoja existe antes de escribir en ella.</li>
    <li>Mantener el formato del archivo Excel.</li>
    <li>Añadir información sin borrar los datos previos.</li>
  </ul>
</p>
<h3>💻 Consola interactiva</h3>
<p>
  Aunque no es una librería, la consola es el medio principal de interacción con el usuario.
</p>
<p>
  A través de preguntas guiadas, el programa recibe las entradas del usuario (como nombres de productos o cantidades) y responde con mensajes claros.
</p>
<p>
  Esto hace que la experiencia sea simple y práctica, sin necesidad de una interfaz gráfica.
</p>

<h2>🔄 Flujo General de Funcionamiento</h2>
<p>
  TiendaApp está pensada para imitar el día a día de una tienda real, pero desde la consola.
</p>
<p>
  Cada opción del menú representa una acción que el vendedor podría realizar durante su jornada.
</p>
<p>
  El flujo general se organiza en cuatro grandes etapas 👇
</p>
<ol>
  <strong><li>🏁 Inicio del programa:</li></strong>
    <p>
      Al ejecutar TiendaApp, el usuario es recibido con un mensaje de bienvenida y un menú interactivo.
    <p>
      Desde allí puede elegir qué desea hacer: revisar el inventario, actualizar precios, registrar una venta, o consultar el resumen del día en especial.
    </p>
    <p>
      Todo se maneja con números, lo que hace el proceso rápido y sencillo.
    </p>
  <strong><li>📋 Gestión del inventario</li></strong>
    <p>
      El inventario es el corazón del sistema.
    </p>
    <p>
      El usuario puede:
    </p>
      <ul>
        <li>Consultar los productos existentes.</li>
        <li>Agregar nuevos artículos con sus cantidades, unidades y precios.</li>
        <li>Actualizar los valores o existencias de un producto.</li>
      </ul>
    <p>
      Toda esta información se almacena en el archivo Tienda.xlsx, dentro de las hojas Inventario y Precios.
    </p>
  <strong><li>💰 Registro de ventas</li></strong>
    <p>
      Cuando se realiza una venta, el programa:
    </p>
    <p>
      <ol>
        <li>Verifica que el producto esté disponible en el inventario.</li>
        <li>Solicita la cantidad deseada y calcula el subtotal.</li>
        <li>Registra la venta en una hoja de Excel llamada Ventas.</li>
        <li>Actualiza automáticamente el inventario restando las unidades vendidas.</li>
      </ol>
    </p>
    <p>
      De esta manera, el archivo siempre refleja el estado real de la tienda.
    </p>
  <strong><li>📊 Resumen de ventas</li></strong>
    <p>
      El usuario puede generar un resumen de las ventas de un día específico.
    </p>
    <p>
      El programa muestra:
      <ul>
        <li>Qué productos se vendieron.</li>
        <li>Cuántas unidades.</li>
        <li>Los subtotales y el total del día.</li>
      </ul>
    </p>
    <p>
      Esto permite tener un control claro de las ganancias y de los productos con más movimiento.
    </p>
</ol>

<h2>🌱 Aprendizajes y objetivos</h2>
<h2>🚀 Próximos pasos</h2>
