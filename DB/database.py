import os
dir = os.path.dirname(os.path.abspath(__file__))
import sqlite3 as sql

class Database:
    def __init__(self, dbName, scriptStruct, scriptData):
        self.__conn = None
        self.__dbName = dbName
        self.__exist = True if os.path.exists(f"{dir}/DB/{dbName}") else False
        self.__created = self.start_connection()
        self.__loaded = self.load_data(f"{dir}/SQL/{scriptStruct}", f"{dir}/SQL/{scriptData}")

    def getExist(self):
        return self.__exist

    def getCreated(self):
        return self.__created

    def getDBName(self):
        return self.__dbName

    def getLoaded(self):
        return self.__loaded

    def check_connection(self):
        try:
            self.__conn.execute("SELECT 1")
            return True
        except Exception as ex:
            return False

    def start_connection(self):
        try:
            if not self.check_connection():
                self.__conn = sql.connect(f"{dir}/DB/"+self.__dbName)
                self.__conn.execute("PRAGMA foreign_keys = ON")
                self.__cursor = self.__conn.cursor()
                print(f"-> La conexion con la base de datos '{self.__dbName}' fue inicializada con exito.")
                return True
            else:
                print(f"-> La conexion con la base de datos '{self.__dbName}' ya existe.")
                return True
        except Exception as ex:
            print(f"-> Error al intentar conectar con la base de datos '{self.__dbName}' : '{str(ex)}'.")
            return False

    def close_connection(self):
        try:
            if self.check_connection():
                self.__conn.close()
                print(f"-> Desconectado satisfactoriamente de la base de datos '{self.__dbName}'.")
                return True
            else:
                print(f"-> Ya se encuentra desconectado de la base de datos '{self.__dbName}'.")
                return True
        except Exception as ex:
            print(f"-> Error al intentar desconectar de la base de datos '{self.__dbName}' : '{str(ex)}'.")
            return False

    def execute_script(self, script):
        try:
            if self.check_connection():
                with open(script) as file:
                    sql_script = file.read()
                self.__cursor.executescript(sql_script)
                self.__conn.commit()
                print(f"-> El script '{script}' se ha cargado satisfactoriamente en la base de datos '{self.__dbName}'.")
                return True
            else:
                print(f"-> No fue posible cargar el script '{script}' debido a una ausencia de conexion con la base de datos '{self.__dbName}'.")
                return False
        except Exception as ex:
            print(f"-> Error al intentar cargar el script '{script}' en la base de datos '{self.__dbName}' : '{str(ex)}'.")
            return False

    def execute_query(self, query, parameters = None):
        try:
            if self.check_connection():
                if parameters is None:
                    self.__cursor.execute(query)
                else:
                    self.__cursor.execute(query, parameters)
                self.__conn.commit()
                result = self.__cursor.fetchall()
                print(f"-> La consulta '{query.split()[0]}' se ha realizado satisfactoriamente en la base de datos '{self.__dbName}'.")
                return True if not result else result
            else:
                print(f"-> No fue posible realizar la consulta '{query.split()[0]}' debido a una ausencia de conexion con la base de datos '{self.dbName}'.")
                return False
        except Exception as ex:
            print(f"-> Error al intentar realizar la consulta '{query.split()[0]}' en la base de datos '{self.__dbName}' : '{str(ex)}'.")
            return False

    def removeDB(self):
        try:
            os.remove(f"{dir}/DB/"+self.__dbName)
            print(f"-> La base de datos '{self.__dbName}' se ha eliminado correctamente.")
            return True
        except Exception as ex:
            print(f"-> Error al intentar eliminar la base de datos '{self.__dbName}' : '{str(ex)}'.")
            return False

    def load_data(self, scriptStruct, scriptData):
        if self.__created:
            if not self.__exist:
                if self.execute_script(scriptStruct) and self.execute_script(scriptData):
                    print(f"-> Nueva base de datos '{self.__dbName}' creada satisfactoriamente.")
                    self.close_connection()
                    return True
                else:
                    print(f"-> Ocurrio un error al intentar crear la base de datos '{self.__dbName}'.")
                    self.close_connection()
                    self.removeDB()
                    return False
            else:
                print("-> No se han realizado modificaciones al contenido actual de la base de datos.")
                self.close_connection()
                return True