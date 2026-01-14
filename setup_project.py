import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Cartelle del progetto
structure = [
    "data",
    "core_app",
    "core_app/api",
    "core_app/domain",
    "core_app/services",
    "core_app/repositories"
]

for rel_path in structure:
    full_path = os.path.join(BASE_DIR, rel_path)
    os.makedirs(full_path, exist_ok=True)
    print(f"Created directory: {rel_path}")

# File base
init_files = [
    "server.py",
    "config.py",
    "core_app/__init__.py",
    "core_app/api/__init__.py",
    "core_app/domain/__init__.py",
    "core_app/services/__init__.py",
    "core_app/repositories/__init__.py"
]

for rel_file in init_files:
    full_path = os.path.join(BASE_DIR, rel_file)
    if not os.path.exists(full_path):
        with open(full_path, "w", encoding="utf-8"):
            pass
        print(f"Created file: {rel_file}")


# requirements.txt
requirements = [
    "Flask==3.1.1",
    "Flask-SQLAlchemy==3.1.1",
    "SQLAlchemy==2.0.41",
    "python-dotenv==1.0.1",
    "gunicorn==22.0.0",
    "pydantic==2.8.2"
]

req_path = os.path.join(BASE_DIR, "requirements.txt")

if not os.path.exists(req_path):
    with open(req_path, "w", encoding="utf-8") as f:
        for pkg in requirements:
            f.write(pkg + "\n")
    print("Created file: requirements.txt")

print("\n Project structure created successfully.")
