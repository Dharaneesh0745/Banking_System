# Banking_System

****

I have developed this console project using MVC architecture by applying DAO pattern and connected with MySQL local server.

****

**Run this project**

1. Create database

   (i) Create database on MySQL workbench.
   
   (ii) Inside Database, by using the database.sql file, create database and tables on workbench MySQL server.

   (iii) Change your root username, password, database_name in the Config/DB_Config.py file.


2. Create virtual environment
```commandline
    python -m venv .venv
```

3. Activate virtual environment
```commandline
    .venv\Scripts\activate.ps
```

4. Install required dependencies
```commandline
    pip install -r requirements.txt
```

5. Run project
```commandline
    python main.py
```