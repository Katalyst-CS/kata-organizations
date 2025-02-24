import os

from flask.cli import load_dotenv
from peewee import PostgresqlDatabase

load_dotenv()

db = PostgresqlDatabase(
    os.getenv('DB_NAME'),
    user=os.getenv('DB_USER'),
    password=os.getenv('DB_PASSWORD'),
    host=os.getenv('DB_HOST'),
    port=int(os.getenv('DB_PORT')),
)

# Conexion de la base de datos
try:
    db.connect(reuse_if_open=True)
    print("Conexion realizada con exito")
except Exception as e:
    print(f"error conectando a la base de datos.{e}")
