"""
Домашка 005c: Практическая работа с файлами

Применяем функции высшего порядка к реальным задачам.
"""

import os


def get_files(directory="."):
    """Возвращает список файлов в директории."""
    return sorted([f for f in os.listdir(directory) 
                   if os.path.isfile(os.path.join(directory, f))])


def get_file_size(filename, directory="."):
    """Возвращает размер файла в байтах."""
    return os.path.getsize(os.path.join(directory, filename))


def get_extension(filename):
    """Возвращает расширение файла."""
    parts = filename.split(".")
    return parts[-1] if len(parts) > 1 else ""


# === ЗАДАНИЕ 1: apply_to_all ===

def apply_to_all(f, items):
    """
    Применяет функцию f к каждому элементу списка.
    
    >>> apply_to_all(lambda x: x * 2, [1, 2, 3])
    [2, 4, 6]
    """
    pass


# === ЗАДАНИЕ 2: filter_by ===

def filter_by(predicate, items):
    """
    Возвращает элементы, для которых predicate(item) == True.
    
    >>> filter_by(lambda x: x > 0, [-1, 2, -3, 4])
    [2, 4]
    """
    pass


# === ЗАДАНИЕ 3: compose ===

def compose(f, g):
    """
    Возвращает функцию h(x) = f(g(x)).
    
    >>> compose(lambda x: x * 2, lambda x: x + 1)(5)
    12
    """
    pass


# === ЗАДАНИЕ 4: Практика с файлами ===

def find_large_files(directory, min_size):
    """
    Находит файлы больше min_size байт.
    Используй filter_by и get_file_size.
    """
    files = get_files(directory)
    pass


def get_python_files(directory):
    """
    Находит все .py файлы.
    Используй filter_by и get_extension.
    """
    files = get_files(directory)
    pass


def get_file_sizes(directory):
    """
    Возвращает список кортежей (filename, size).
    Используй apply_to_all.
    """
    files = get_files(directory)
    pass


# === БОНУС: make_file_filter ===

def make_file_filter(extension):
    """
    Возвращает функцию-фильтр для файлов с данным расширением.
    
    >>> py_filter = make_file_filter("py")
    >>> py_filter("main.py")
    True
    """
    pass
