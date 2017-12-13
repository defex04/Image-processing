import os

def get_url(name):
    """""
    Выдает путь на один уровень выше,
    чем местоположение данного скрипта.
    """""
    script_dir = os.path.dirname(__file__)
    file_path = os.path.join(script_dir, "../"+name)
    return file_path