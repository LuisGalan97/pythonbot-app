import os
import sqlite3 as sql

class Database:
    def __init__(self, dbName):
        self.conn = None
        self.dbName = dbName
        self.exist = True if os.path.exists("./DB/"+dbName) else False
        result = self.start_connection()
        if result is True:
            print(f"La conexion con la base de datos '{dbName}' fue establecida con exito")
        elif result is False:
            print(f"La conexion con la base de datos '{dbName}' ya existe.")
        else: 
            print(f"Ocurrio un error al intentar establecer la conexion: '{result}'")

    def getExist(self):
        return self.exist

    def check_connection(self):
        try:
            self.conn.execute("SELECT 1")
            return True
        except Exception as ex:
            return False

    def start_connection(self):
        try:
            if not self.check_connection():
                self.conn = sql.connect("./DB/"+self.dbName)
                self.cursor = self.conn.cursor()
                return True
            else:
                return False
        except Exception as ex:
            return str(ex)
    
    def close_connection(self):
        try:
            if self.check_connection():
                self.conn.close()
                return True
            else:
                return False
        except Exception as ex:
            return str(ex)
    
    def execute_script(self, script):
        try: 
            if self.check_connection():
                with open(script) as file:
                    sql_script = file.read()
        
                self.cursor.executescript(sql_script)
                self.conn.commit()
                return True
            else:
                return False
        except Exception as ex:
            return str(ex)

    def execute_query(self, query):
        try:
            if self.check_connection():
                self.cursor.execute(query)
                self.conn.commit()
                result = self.cursor.fetchall()
                return True if not result else result
            else: 
                return False
        except Exception as ex:
            return str(ex)


db = Database("avalon.db")
if not db.getExist():
    db.execute_script("./SQL/avalon-lite.sql")
    db.execute_script("./SQL/data.sql")
    print("Se ha realizado la creacion de tablas y la inserción de valores por defecto en la base de datos.")
else:
    print("No se han realizado modificaciones al contenido actual de la base de datos.")