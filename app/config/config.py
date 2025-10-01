
import os
from urllib.parse import quote_plus


AZURE_SQL_CONN_STRING = os.getenv("AZURE_SQL_CONN_STRING")

if not AZURE_SQL_CONN_STRING:
    DRIVER = "ODBC Driver 18 for SQL Server"
    SERVER = "lab-cloud-db.database.windows.net"
    DATABASE = "labdb"
    USER = "andrii"
    PASSWORD = "2706061905And"

    odbc_str = (
        f"Driver={{{DRIVER}}};"
        f"Server=tcp:{SERVER},1433;"
        f"Database={DATABASE};"
        f"Uid={USER};"
        f"Pwd={PASSWORD};"
        "Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;"
    )
    AZURE_SQL_CONN_STRING = f"mssql+pyodbc:///?odbc_connect={quote_plus(odbc_str)}"


class Config:
    SQLALCHEMY_DATABASE_URI = AZURE_SQL_CONN_STRING
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv("SECRET_KEY", "super-secret-key")
