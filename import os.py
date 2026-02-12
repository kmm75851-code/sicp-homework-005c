import os

# Функция для получения размера файла
def get_file_size(filename, directory="."):
    """Возвращает размер файла в байтах."""
    return os.path.getsize(os.path.join(directory, filename))

# Проверим, что get_files возвращает список файлов в текущей директории
def get_files(directory="."):
    """Возвращает список файлов в директории."""
    return sorted([f for f in os.listdir(directory) 
                   if os.path.isfile(os.path.join(directory, f))])

# Функция для получения всех размеров файлов в виде списка кортежей (filename, size)
def get_file_sizes(directory):
    """Возвращает список кортежей (filename, size)."""
    files = get_files(directory)
    return [(f, get_file_size(f, directory)) for f in files]

# Тестовая директория для проверки
TEST_DIR = "test_directory"

# Создадим тестовую директорию и файлы для проверки
os.makedirs(TEST_DIR, exist_ok=True)

# Создадим несколько файлов с разными размерами
with open(os.path.join(TEST_DIR, "small.txt"), "w") as f:
    f.write("Hello")  # Размер будет 5 байт
with open(os.path.join(TEST_DIR, "medium.txt"), "w") as f:
    f.write("Hello, World!")  # Размер будет 13 байт
with open(os.path.join(TEST_DIR, "large.txt"), "w") as f:
    f.write("A" * 762)  # Размер будет 762 байта

# Проверим размеры файлов
file_sizes = get_file_sizes(TEST_DIR)
print("File sizes:", file_sizes)

# Очистим тестовую директорию после проверки
for f in os.listdir(TEST_DIR):
    os.remove(os.path.join(TEST_DIR, f))
os.rmdir(TEST_DIR)
