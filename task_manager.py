# task_manager.py

import json
from typing import List

class TaskManager:
    def __init__(self):
        self.tasks: List[dict] = []

    def add_task(self, description: str):
        task = {"description": description, "completed": False}
        self.tasks.append(task)

    def complete_task(self, index: int):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["completed"] = True
        else:
            raise IndexError("Задача с таким индексом не найдена")

    def remove_task(self, index: int):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
        else:
            raise IndexError("Задача с таким индексом не найдена")

    def save_to_json(self, filename: str):
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(self.tasks, f, ensure_ascii=False, indent=4)

    def load_from_json(self, filename: str):
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                self.tasks = json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError(f"Файл {filename} не найден")