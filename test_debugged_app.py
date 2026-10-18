
import tempfile
import unittest
from pathlib import Path

from debugged_app import (
    add_task,
    remove_task,
    save_tasks,
    load_tasks,
)


class TestTodoApplication(unittest.TestCase):

    def test_add_task(self):
        tasks = []
        add_task(tasks, "Study Python")
        self.assertEqual(tasks, ["Study Python"])

    def test_add_task_removes_extra_spaces(self):
        tasks = []
        add_task(tasks, "  Learn Python  ")
        self.assertEqual(tasks, ["Learn Python"])

    def test_empty_task_is_rejected(self):
        with self.assertRaises(ValueError):
            add_task([], "   ")

    def test_remove_first_task(self):
        tasks = ["Study", "Practice"]
        removed = remove_task(tasks, 1)

        self.assertEqual(removed, "Study")
        self.assertEqual(tasks, ["Practice"])

    def test_invalid_task_number(self):
        with self.assertRaises(ValueError):
            remove_task(["Study"], 2)

    def test_invalid_task_number_type(self):
        with self.assertRaises(ValueError):
            remove_task(["Study"], "1")

    def test_save_and_load_tasks(self):
        with tempfile.TemporaryDirectory() as folder:
            filename = Path(folder) / "tasks.txt"
            original = ["Study Python", "Complete assignment"]

            save_tasks(original, filename)
            loaded = load_tasks(filename)

            self.assertEqual(loaded, original)

    def test_missing_file_returns_empty_list(self):
        with tempfile.TemporaryDirectory() as folder:
            filename = Path(folder) / "missing.txt"

            self.assertEqual(load_tasks(filename), [])


if __name__ == "__main__":
    unittest.main()
