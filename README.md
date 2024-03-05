# Lab - Class 42

## Project: Pythonisms

### Author: [Immanuel Shin](https://github.com/ImmanuelShin)

### Setup

**How to initialize/run your application:**
  1. Clone the repository.
   ```bash
   git clone
   ```
  2. Navigate to the project directory.
   ```bash
   cd pythonisms
   ```
  3. Activate your virtual environment (if applicable).
   ```bash
   python3 -m venv .venv
   source .venv/Scripts/activate
   ```
  4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
  5. **(Optional)** Run `python decorators/decorators.py` to see decorators in action.

### Tests

Run `pytest iterators/test_dictionary_tree.py` to see custom tree class in action.

## Findings

### Treectionary

I wasn't really sure what I was doing with this one. The only thing I was trying to do was make a tree act as if it were a dictionary. I learned how the getter and setter magic methods worked and how they can be used to sort of turn anything into dictionaries with enough effort. As it is now, Treectionary is not really that useful. I'm not entirely sure what the use case a tree that can be used as a dictionary would look like. Nonetheless, it was fun trying to make this work.

### Decorators

Decorators, to me, are one of those things that you don't really start off thinking about. You start a project, write a lot of code, realize that you are using a specific methods in various different ways, and then, finally, write decorators to ease the process of utilizing those methods in those various differnt ways. There are definitely many useful decorators, such as logging or memoization, so I'm sure I will just have to keep looking out for situations to use them. 

