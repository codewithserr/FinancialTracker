# This file manages everything related with the database which contains
# all transactions

import sqlite3

###############################################################
# This function creates the Database in case it does not exist,
# and connects to the one created in case it exist.
###############################################################
def createDatabase():
    # Create the SQLite database called "transactions.db"
    conn = sqlite3.connect("data/transactions.db")

    # Create a cursor for execute SQL commands
    cursor = conn.cursor()

    # Create a table for saving all transactions
    # Each transaction should have the next information:
    # [TRANSACTION_ID    DATE    TITTLE  TYPE(EXPENSE/INCOME)    CATEGORY    SUBCATEGORY TYPE2(FIXED/VARIABLE)   AMMOUNT]
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS transacciones (
            id_transaccion INTEGER PRIMARY KEY AUTOINCREMENT,
            fecha TEXT NOT NULL,
            descripcion TEXT,
            tipo TEXT,
            categoria TEXT NOT NULL,
            subcategoria TEXT NOT NULL,
            tipo2 TEXT NOT NULL,
            cantidad REAL NOT NULL
        )
    ''')

    # Confirm the changes on the database
    conn.commit()

    # Close the database
    conn.close()


###############################################################
# This function add transactions to the database 
###############################################################
def addTransaction():
    pass

###############################################################
# This function search for transaction in the database 
###############################################################
def addTransaction():
    pass



###############################################################
# This function delete an specific transaction fom the database 
###############################################################
def deleteTransaction(ID):
    pass








