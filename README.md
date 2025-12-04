<h1 align="center">TiendApp</h1>

<h2>🏷️ Overview</h2>
<p>
  TiendaApp is an application developed in <strong>Python</strong> for managing inventory and sales in a store.
</p>
<p>
  Its objective is to facilitate the control of products, prices, and sales transactions by automating tasks that are normally performed manually.
</p>
<p>
  The program allows you to check inventory, update stock levels and prices, record sales, and generate sales summaries for user-specified dates, 
  all while working directly on an Excel file.
</p>
<p>
  Thanks to this, the information remains organized and easily accessible, without the need for a complex database.
</p>
<p>
  This project began as a practical exercise to apply object-oriented programming (OOP) concepts and data handling with Pandas and Openpyxl, demonstrating 
  how a simple solution can become a useful and flexible tool for any small business or local shop.
</p>

<h2>⚙️ Main features</h2>
<p>
  TiendaApp is designed so that anyone can manage the basics of their store without needing advanced technical knowledge.
</p>
<p>
  Its structure is based on simple but well-organized tasks, reflecting what happens day-to-day in a real business.
</p>
<p>
  Its main features include:
</p>
  <ul>
    <li>🧾 <strong>Inventory Management:</strong> allows you to review available products, their quantities, and units of measure (grams or units).</li>
    <li>✏️ <strong>Stock Update:</strong> easily adjusts quantities when new products arrive or inventory discrepancies are detected.</li>
    <li>💰 <strong>Price Control:</strong> keeps purchase and sale prices updated, automatically calculating the profit margin for each product.</li>
    <li>🛍️ <strong>Sales Log:</strong> saves daily sales, generating a history with date, product, quantity, price, and subtotal.</li>
    <li>📊 <strong>Sales Summary:</strong> generates reports showing sales made and the daily total on the date requested by the user.</li>
    <li>📁 <strong>Integration with Excel:</strong> uses .xlsx files to store all the information, leveraging the Pandas and Openpyxl libraries.</li>
  </ul>
<p>
  Together, these features allow TiendaApp to act as a small digital store assistant: organized, reliable, and always ready to record a new sale.
</p>

<h2>🧩 Project Structure</h2>
<p>
  The project is organized in a simple way to make it easy to understand, modify, and extend.
</p>
<p>
  Each part of the code serves a clear purpose within the application flow.
</p>
<p>
  The general structure is as follows:
  <code>
    TiendaApp/
    │
    ├── TiendaApp.py           # Main program file (entry point)
    ├── tienda.py              # File containing the 'store' class and its methods
    ├── Tienda.xlsx            # Excel file where inventory, prices, and sales are stored
    ├── Leeme.md               # Project description and guide document in Spanish
    └── README.md              # Project description and guide document in English
    
  </code>
</p>
<h3>📘 Component Description</h3>
<ul>
  <li><strong>TiendaApp.py:</strong> This is the heart of the program. It contains the main menu that allows the user to choose what they want to do (view, sell, update,   etc.). Here, the objects of the store class are created, and all user interaction is orchestrated.</li>
  <li><strong>tienda.py:</strong> Defines the store class, which contains all the program's logic. Within this class are the methods responsible for reading, updating,     selling, and summarizing inventory information.</li>
  <li><strong>Tienda.xlsx:</strong> This is the file where the information is stored. It contains several data sheets:
  <ul>
    <li><em>Inventory</em> (list of products and quantities)</li>
    <li><em>Prices</em> (purchase, sale, and profit prices)</li>
    <li><em>Sales</em> (historical record of sales made)</li>
  </ul>
  <li><strong>Leeme.md:</strong> Document explaining what the application does, how it is built, and what the user can achieve with it, in spanish.</li>
  <li><strong>README.md:</strong> Document explaining what the application does, how it is built, and what the user can achieve with it, in english.</li>
</ul>

<h2>🧠 Applied Concepts</h2>
<p>
  TiendaApp combines several fundamental programming and data handling concepts in Python.
</p>
<p>
  The idea is that the code not only works, but also provides a good foundation for learning and improving as a developer.
</p>
<h3>🧩 Object-Oriented Programming (OOP)</h3>
<p>
  The project is built around a class called Tienda (Store).
</p>
<p>
  This class groups the data (such as inventory and sales) and the actions that can be performed on it (such as adding products, selling, or updating prices).
</p>
<p>
  This approach allows you to:
</p>
  <ul>
    <li>Reuse code in an organized way.</li>
    <li>Maintain a clean and easily extensible structure.</li>
    <li>Work with objects that represent real-world concepts (in this case, a store).</li>
  </ul>
<h3>📊 Data Handling with Pandas</h3>
<p>
  TiendaApp uses pandas to read, modify, and write data stored in Excel spreadsheets.
</p>
<p>
  Thanks to its DataFrame structures, operations such as filtering products, calculating subtotals, or updating quantities are performed quickly and readably.
</p>
<p>
Furthermore, pd.ExcelWriter is used to write to specific sheets, adding or overwriting information without losing the rest of the data in the file.
</p>
<h3>📘 Interaction with Excel Files (Openpyxl)</h3>
<p>
  The <strong>openpyxl</strong> library allows you to verify and manipulate the sheets within the Tienda.xlsx file. This makes it easy to check if sheets like              “Inventory” or “Sales” exist before writing to them, and to manage the data flow without errors.
</p>
<h3>💬 User Interaction</h3>
<p>
  The program runs in the console and guides the user with clear messages and step-by-step questions. This interaction makes TiendaApp intuitive, even for someone          without technical knowledge.
</p>
<h3>🔁 Modular Structure and Flow Logic</h3>
<p>
  The main program (TiendaApp.py) acts as a control point: it displays the menu, receives the options, and calls the corresponding methods of the Tienda class. This        creates a natural flow where the user can review, update, sell, or query without complications. 
</p>

<h2>📊 Technologies Used</h2>
<p>
  TiendaApp is developed entirely in Python, combining libraries that facilitate working with data, file persistence, and user interaction.
</p>
<p>
  Below, I'll tell you about the main tools and why they were used 👇
</p>
<h3>🐍 Python 3</h3>
<p>
  The project's base language.
<p>
  Its clear and readable syntax makes it an excellent choice for creating applications that handle data and simple automations.
</p>
<p>
  Furthermore, its multipurpose approach allows TiendaApp to easily grow with new features.
</p>
<h3>🧮 Pandas</h3>
<p>
  I  t's the backbone of data handling.
</p>
<p>
  It allows you to work with DataFrame-type structures, which function like Excel tables within the code.
</p>
<p>
  With pandas, TiendaApp can:
<ul>
  <li>Read and write data from specific sheets.</li>
  <li>Calculate subtotals, totals, and profits.</li>
  <li>Filter and update records with just a few lines of code.</li>
</ul>
</p>

<h3>📗 Openpyxl</h3>
<p>
  It is used to interact directly with .xlsx files.
</p>
<p>
  Thanks to this library, TiendaApp can:
  <ul>
    <li>Check if a sheet exists before writing to it.</li>
    <li>Maintain the Excel file's formatting.</li>
    <li>Add information without deleting previous data.</li>
  </ul>
</p>
<h3>💻 Interactive Console</h3>
<p>
  Although not a library, the console is the primary means of user interaction.
</p>
<p>
  Through guided questions, the program receives user input (such as product names or quantities) and responds with clear messages.
</p>
<p>
  This makes the experience simple and practical, without the need for a graphical interface.
</p>

<h2>🔄 General Operating Flow</h2>
<p>
  TiendaApp is designed to mimic the daily operations of a real store, but from the console.
</p>
<p>
  Each menu option represents an action that the salesperson might perform during their workday.
</p>
<p>
  The general flow is organized into four main stages 👇
</p>
<ol>
  <strong><li>🏁 Program Startup:</li></strong>
  <p>
  When TiendaApp is launched, the user is greeted with a welcome message and an interactive menu.
    <p>
    From there, they can choose what they want to do: check inventory, update prices, register a sale, or view a summary of the day.
    </p>
    <p>
    Everything is managed with numbers, making the process quick and easy.
    </p>
  <strong><li>📋 Inventory Management</li></strong>
    <p>
      Inventory is the heart of the system.
    </p>
    <p>
    The user can:
      <ul>
        <li>View existing products.</li>
        <li>Add new items with their quantities, units, and prices.</li>
        <li>Update the values ​​or stock of a product.</li>
      </ul>
    </p>
    <p>
      All this information is stored in the Tienda.xlsx file, within the Inventory and Prices sheets.
    </p>
    <strong><li>💰 Sales Log</li></strong>
    <p>
      When a sale is made, the program:
    </p>
    <p>
      <ol>
        <li>Checks that the product is available in inventory.</li>
        <li>Requests the desired quantity and calculates the subtotal.</li>
        <li>Records the sale in an Excel sheet called Sales.</li>
        <li>Automatically updates the inventory by subtracting the units sold.</li>
      </ol>
    </p>
    <p>
      This way, the file always reflects the actual state of the store.
    </p>
    <strong><li>📊 Sales Summary</li></strong>
    <p>
      The user can generate a summary of sales for a specific day.
    </p>
    <p>
      The program displays:
      <ul>
        <li>Which products were sold.</li>
        <li>How many units.</li>
        <li>The subtotals and the daily total.</li>
      </ul>
    </p>
    <p>
      This allows for clear control of profits and best-selling products.
    </p>
</ol>

<h2>🌱 Learning and objectives</h2>
<p>
Throughout the development of TiendaApp, I was able to strengthen several key concepts while building a useful and complete project. This section summarizes what I learned and also the objectives that guided each part of the process.
</p>
<h3>Learning</h3>
<ul> 
  <li><strong>Structuring a real project:</strong> It goes from an initial idea to an organized program, with clear functions and a main class that manages the entire flow of work.</li> 
  <li><strong>Practical use of OOP:</strong> Understand how to encapsulate the logic within methods and how the attributes of a class facilitate the management of the state (product, inventory, prices, etc.).</li> 
  <li><strong>Excel file handling:</strong> Implements try/except blocks to prevent the program from crashing when a file does not exist or when a controlled error occurs.</li> 
  <li><strong>Interaction with the user:</strong> Designs clear flows with messages that guide the experience of anyone using the application, ensuring that it always Separate what to do.</li> 
  <li><strong>Organization of the code:</strong> Separates each action into specialized methods, which makes the code much more understandable and easy to maintain.</li>
</ul>
<h3>Project objectives</h3>
<ul> 
  <li>Create a small tool that allows you to manage a store's inventory in a simple and clear way.</li> 
  <li>Build a realistic sales flow: choose products, validate stocks, register each sale and update inventories.</li> 
  <li>Maintain a historical record of sales per day, accessible for later consultation.</li> 
  <li>Learn to work with external files as a lightweight database, using Excel.</li> 
  <li>Put my knowledge of Python into practice and strengthen applied logic in a real project.</li> 
  <li>To create a solid foundation for future improvements, such as adding a visual interface or automating reports.</li>
</ul>
<h2>🚀 Next steps</h2>
<p> 
  TiendaApp works very well as a basic management tool, but it still has a lot of potential for growth. These are some of the next steps that I would like to implement to continue taking it to the next level:
</p>
<h3>🌱 Technical improvements</h3>
  <ul> 
    <li><strong>Optimize the code</strong> to make it more efficient, eliminating repetitions and making better use of the capabilities of Pandas and OOP.</li> 
    <li><strong>Separate the logic into modules</strong> (for example: inventory, sales, reports), which will make the project easier to maintain and scale.</li> 
    <li><strong>Add more robust validations,</strong> such as checking data types or restricting invalid values ​​in user input.</li> 
    <li><strong>Create a service layer</strong> to better manage reading and writing Excel files, avoiding code duplication.</li>
  </ul>
  <h3> 🖥️ New interface</h3>
<ul> 
  <li><strong>Design a simple graphical interface</strong> (maybe with Tkinter or PyQt) so that the app is more user-friendly and does not depend on the console.</li> 
  <li><strong>Show inventory and sales tables in a visual way,</strong>(with buttons to add, update and sell products.</li>
</ul>
<h3> 📊 Additional features</h3>
<ul> 
  <li><strong>Generate automatic reports</strong> in PDF or Excel for daily, weekly or monthly sales. 
  <li><strong>Add minimum stock control,</strong> sending alerts when a product is running out.</li> 
  <li><strong>History by product,</strong> to see how your inventory has varied and your sales over time. 
  <li><strong>Include authentication or roles,</strong> by itself several people will be able to use the application.
</ul>
<h3> ☁️ More advanced future</h3>
  <ul> 
    <li><strong>Migrate the database</strong> from Excel to SQLite or PostgreSQL for greater security and scalability. 
    <li><strong>Convert TiendaApp into an API,</strong> allowing you to connect it to a modern frontend or a mobile app.</li> 
    <li><strong>Deploy it online</strong> and offer it as a service for small stores.
  </ul>
