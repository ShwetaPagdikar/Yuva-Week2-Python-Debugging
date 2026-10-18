# Week 2: Debugging and Troubleshooting Python Applications

## Project Name
Python To-Do List Manager

## Objective
The objective of this project is to identify and fix common errors in a Python application and verify the corrections through automated and manual testing.

## Technologies Used
- Python
- VS Code
- Python unittest module

## Project Files
- `buggy_app.py` – Contains the original code with intentional bugs.
- `debugged_app.py` – Contains the corrected application.
- `test_debugged_app.py` – Contains 8 automated unit tests.
- `DEBUGGING_LOG.md` – Describes the identified bugs, fixes, and testing process.
- `tasks.txt` – Stores tasks saved by the application during execution.

## Bugs Identified and Fixed
1. Corrected the menu-choice comparison.
2. Fixed the task-viewing loop to prevent an index error.
3. Corrected task removal using displayed task numbers.
4. Added validation for empty tasks and invalid task numbers.
5. Added file handling to save and load tasks.

## How to Run the Application
1. Open the project folder in VS Code.
2. Open the terminal.
3. Run `python debugged_app.py`.
4. Follow the menu options to add, remove, and view tasks.
5. Select option 4 to save tasks and exit.

## How to Run Tests
Run the following command in the terminal:

`python -m unittest -v`

## Conclusion
The project demonstrates debugging, error handling, file operations, and automated testing in Python. The corrected application was tested using unit tests and can also be checked manually through its menu.