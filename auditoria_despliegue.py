from pathlib import Path

print("\n=== AUDITORÍA SISTEMA LUHANA ===\n")

# 1. RUTA DB
db_path = Path.home() / "Documents" / "Sistema_Luhana" / "db" / "gym.db"
print("[DB]")
print("Ruta:", db_path)
print("Existe:", db_path.exists())
if db_path.exists():
    print("Tamaño:", db_path.stat().st_size, "bytes")
else:
    print("❌ DB NO EXISTE")

# 2. CONTENIDO DE CARPETA DB
db_dir = db_path.parent
print("\n[CONTENIDO db/]")
if db_dir.exists():
    for f in db_dir.iterdir():
        print("-", f.name, f.stat().st_size, "bytes")
else:
    print("❌ Carpeta db no existe")

# 3. ARCHIVOS CLAVE DE CÓDIGO
print("\n[CÓDIGO]")
main = Path("C:/Sistema_Dev/main.py")
print("main.py existe:", main.exists())

paths = Path("C:/Sistema_Dev/interfaz/utils/paths.py")
print("paths.py existe:", paths.exists())

print("\n=== FIN AUDITORÍA ===\n")
