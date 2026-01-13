import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

structure = [
    "app",
    "app/api",
    "app/domain",
    "app/services",
    "app/repositories"
]

for rel_path_folder in structure:
    full_path_file = os.path.join(BASE_DIR, rel_path_folder)
    os.makedirs(full_path_file, exist_ok=True)
    print(f"Created path: {rel_path_folder}")

init_files = [
    "app/__init__.py",
    "app/api/__init__.py",
    "app/domain/__init__.py",
    "app/services/__init__.py",
    "app/repositories/__init__.py"
]

for rel_path_file in init_files:
    full_path_file = os.path.join(BASE_DIR, rel_path_file)
    if not os.path.exists(full_path_file):
        with open(full_path_file, "w") as f:
            f.write("")
        print(f"File created: {rel_path_file}")

print("\nProject structure created successfully.")