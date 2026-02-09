import sqlite3
from interfaz.utils.paths import DB_PATH

def limpiar_base_de_datos():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("DELETE FROM clientes_mensuales")
    cursor.execute("DELETE FROM ingresos")
    cursor.execute("DELETE FROM asistencias")

    conn.commit()
    conn.close()

    print("Datos eliminados correctamente.")

limpiar_base_de_datos()
