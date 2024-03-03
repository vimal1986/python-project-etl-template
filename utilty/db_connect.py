import os
import pyodbc 
from dotenv import load_dotenv

SERVER_NAME = os.getenv("SERVER_NAME")
DB_NAME = os.getenv("DB_NAME")
DRIVER = os.getenv("DRIVER")
DB_USER = os.getenv("DB_USER")
DB_VERSION = os.getenv("DB_VERSION")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_PORT = os.getenv("DB_PORT")


def execute_db_query(sql):
    status = False
    try:
        cnxn = pyodbc.connect(server=SERVER_NAME,
                database=DB_NAME,
                user=DB_USER,
                tds_version=DB_VERSION,
                password=DB_PASSWORD,
                port=DB_PORT,
                driver='FreeTDS')
        crsr = cnxn.cursor()
        recordset = crsr.execute(sql).fetchall()
        status = True
        crsr.close()
        cnxn.close()
        return status, recordset
    except pyodbc.Error as ex:
        status = False
        sqlstate = ex.args[0]
        if sqlstate == '28000':
            print("LDAP Connection failed: check password")
        return status, ""
    finally:
        crsr.close()
        cnxn.close()
    