# test_task_manager.py

import pytest

from task_manager import TaskManager

def test_add_and_complete_task():
    tm = TaskManager()
    tm.add_task("Купить продукты")
    assert len(tm.tasks) == 1
    assert tm.tasks[0]['description'] == "Купить продукты"
    assert tm.tasks[0]['completed'] is False

    tm.complete_task(0)
    assert tm.tasks[0]['completed'] is True


def test_remove_task():
    tm = TaskManager()
    tm.add_task("Купить продукты")
    tm.add_task("Погулять с собакой")
    assert len(tm.tasks) == 2

    tm.remove_task(0)
    assert len(tm.tasks) == 1
    assert tm.tasks[0]['description'] == "Погулять с собакой"


def test_save_and_load_json(tmpdir):
    tm = TaskManager()
    tm.add_task("Купить продукты")
    tm.complete_task(0)
    tm.add_task("Погулять с собакой")

    filename = tmpdir.join("tasks.json")
    tm.save_to_json(str(filename))

    tm2 = TaskManager()
    tm2.load_from_json(str(filename))

    assert len(tm2.tasks) == 2
    assert tm2.tasks[0]['description'] == "Купить продукты"
    assert tm2.tasks[0]['completed'] is True
    assert tm2.tasks[1]['description'] == "Погулять с собакой"
    assert tm2.tasks[1]['completed'] is False
