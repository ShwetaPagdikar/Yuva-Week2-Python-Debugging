# Week 2 Task: Debugging and Troubleshooting Python Applications

## 1. Project Overview

**Project Name:** Python To-Do List Manager  
**Programming Language:** Python  
**Testing Framework:** Python unittest  

**Objective:** To identify, reproduce, and fix common Python programming errors, improve code readability, and verify the corrected application through testing.

The application allows users to add tasks, view tasks, remove tasks, and save tasks to a file. An intentionally buggy version was created for practicing debugging because no separate Python script was supplied with the internship instructions.

## 2. Initial Code Review

The original script was reviewed, focusing on conditional statements, loops, list indexing, user input, and error handling.

The review identified the following potential problems:

1. Incorrect comparison of the menu choice.
2. An incorrect loop range when displaying tasks.
3. Incorrect list indexing when removing a task.
4. Missing validation for empty tasks and invalid task numbers.
5. Missing file storage and error-handling features.

## 3. Bug Reports and Root-Cause Analysis

### Bug 1: Incorrect Menu-Choice Comparison

**Before:**
```python
if choice == 1:
```

**Problem:** The `input()` function returns a string, but the code compares the value with an integer.

**Expected behavior:** Selecting option 1 should open the add-task operation.

**Root cause:** A data-type mismatch in the conditional statement.

**Fix:**
```python
if choice == "1":
```

**Verification:** Run the application, enter option 1, and check whether it prompts for a task.

### Bug 2: Index Error While Displaying Tasks

**Before:**
```python
for i in range(len(tasks) + 1):
    print(i + 1, tasks[i])
```

**Problem:** The loop attempts to access an index outside the valid list range.

**Expected behavior:** Every task should be displayed without an error.

**Root cause:** The loop runs one iteration too many.

**Fix:**
```python
for number, task in enumerate(tasks, start=1):
    print(f"{number}. {task}")
```

**Verification:** Add one or more tasks and select the view option.

### Bug 3: Incorrect Task Removal

**Before:**
```python
index = int(input("Enter task number: "))
tasks.pop(index)
```

**Problem:** The displayed task number starts at 1, but Python list indexes start at 0.

**Expected behavior:** Entering task number 1 should remove the first task.

**Root cause:** The displayed number was used directly as a list index.

**Fix:**
```python
tasks.pop(task_number - 1)
```

The corrected application also checks that the task number is valid before removing a task.

**Verification:** Add two tasks and remove task number 1. Confirm that the first task is removed.

### Bug 4: Missing Input Validation

**Problem:** The original code does not properly validate empty task names or invalid task numbers.

**Expected behavior:** Invalid input should produce a clear error message instead of causing unexpected behavior.

**Before — Original Code:**

```python
task = input("Enter task: ")
tasks.append(task)

index = int(input("Enter task number: "))
tasks.pop(index)
```


**Root Cause:** The original code did not validate empty task names or check whether the task number was within the valid range. Non-numeric input could also cause a conversion error.

**Fix:** Added input validation to reject empty task names and invalid task numbers.
**After — Task Validation:**

```python
title = title.strip()

if not title:
    raise ValueError("Task cannot be empty.")
```

**After — Task-Number Validation:**

```python
if not isinstance(task_number, int):
    raise ValueError("Task number must be an integer.")

if task_number < 1 or task_number > len(tasks):
    raise ValueError("Invalid task number.")

return tasks.pop(task_number - 1)
```

**Verification:** Test an empty task name and an invalid task number. Confirm that the application displays the appropriate error messages.

### Bug 5: Missing File Persistence

**Problem:** The original script stores tasks only in memory. All tasks are lost when the program exits.

**Expected behavior:** Tasks should remain available after restarting the application.

**Root Cause:** The original script does not contain file-saving or file-loading functions.

**Before — Original Code:**

```python
tasks = []
```

The original application stored tasks in a list but did not save them to a file.

**After — Corrected Code:**

```python
def save_tasks(tasks, filename):
    with Path(filename).open("w", encoding="utf-8") as file:
        for task in tasks:
            file.write(task + "\n")


def load_tasks(filename):
    path = Path(filename)

    if not path.exists():
        return []

    with path.open("r", encoding="utf-8") as file:
        return [line.strip() for line in file if line.strip()]
```

**Improvement:** The `save_tasks()` function writes tasks to a file, while `load_tasks()` reads saved tasks when the application starts.

**Verification:** Add a task named `Study Python`, select option 4 to save and exit, and restart the application. Confirm that the task appears again.



## 4. Step-by-Step Debugging Process

### Step 1: Initial Code Review
The original Python script was reviewed to understand how the application works. Special attention was given to conditional statements, loops, list indexing, user input, and file operations.

### Step 2: Identify Potential Bugs
The review identified issues in menu-choice comparison, task display, task removal, and input validation. These problems could cause incorrect behavior or runtime errors.

### Step 3: Analyze Root Causes
The menu-choice problem was caused by comparing a string with an integer. The display loop used an incorrect range, and task removal did not account for the difference between displayed task numbers and Python list indexes.

### Step 4: Apply Corrections
The conditional statement was corrected to compare strings. The `enumerate()` function was used to display tasks, and the removal function was updated to validate task numbers and use the correct list index.

### Step 5: Improve Code Structure
The application was divided into separate functions for adding, removing, displaying, saving, and loading tasks. Input validation and clear error messages were added to improve maintainability.

### Step 6: Verify the Fixes
The application was tested manually by adding, viewing, and removing tasks, checking invalid menu input, and confirming that saved tasks could be loaded after restarting the application. Automated tests were run using Python's `unittest` framework.

### Debugging Method
The code was inspected and corrected, then verified through automated and manual testing. An interactive debugger such as `pdb` or the VS Code debugger was not used.

## 5. Code Structure Improvements

The corrected application was refactored to improve clarity and maintainability.

- Separate functions were created for adding, removing, displaying, saving, and loading tasks.
- Descriptive function and variable names were used.
- Input validation was added.
- `enumerate()` was used to display task numbers clearly.
- `pathlib.Path` was used for file operations.
- Error messages were added for invalid input.
- Unit tests were created to verify important functions.

## 6. Automated Testing

**Test file:** `test_debugged_app.py`  
**Testing framework:** Python `unittest`  
**Number of test cases:** 8

The tests cover:

1. Adding a task.
2. Removing extra spaces from a task name.
3. Rejecting an empty task.
4. Removing the first task correctly.
5. Rejecting an invalid task number.
6. Rejecting an incorrect task-number type.
7. Saving and loading tasks.
8. Handling a missing task file.

**Command used:**
```bash
python -m unittest -v
```

**Actual result:** Ran 8 tests in 0.008s.

**Status:** All 8 tests passed. The terminal displayed `OK`.

## 7. Manual Testing

The application was tested manually to verify that its main features work correctly.

**Test Case 1: Add a Valid Task**

- **Expected Result:** The task should be added successfully.
- **Actual Result:** The task "Study Python" was added successfully.
- **Status:** Passed

**Test Case 2: View Tasks**

- **Expected Result:** Tasks should appear with numbers.
- **Actual Result:** The task appeared in the numbered list.
- **Status:** Passed

**Test Case 3: Remove a Valid Task**

- **Expected Result:** The selected task should be removed.
- **Actual Result:** "Study Python" was removed successfully.
- **Status:** Passed

**Test Case 4: Enter an Invalid Menu Choice**

- **Expected Result:** An error message should appear.
- **Actual Result:** The application displayed "Invalid choice. Enter 1, 2, 3, or 4."
- **Status:** Passed

**Test Case 5: Save and Restart**

- **Expected Result:** Saved tasks should load again after restarting the application.
- **Actual Result:** "Study Python" appeared after restarting the application.
- **Status:** Passed

**Result:** All five manual test cases passed.

## 8. Conclusion

This project demonstrates the process of reviewing Python code, identifying bugs, analyzing their causes, correcting faulty logic, improving code structure, and verifying behavior through automated and manual testing.

The corrected To-Do List Manager provides basic task management, input validation, and file persistence. The debugging log records the problems, proposed fixes, and testing evidence.

