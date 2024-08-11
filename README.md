# About
This program can be described as a combination of two ChatGPT-4 instances, managed with a straightforward control structure.

Typing "quit" will exit the program and save the conversation to a JSON file. Switching between the two bots is easy—just mention that you want a product suggestion. Each time you switch bots, the conversation history will also be saved in a JSON file.


# Pre-requisite:

1. To check if Python is installed on your computer, you can follow these steps:

* Open the Start menu and type "Command Prompt" or "PowerShell" in the search bar. Open either of these programs.

* In the Command Prompt or PowerShell window, type the following command and press Enter:

```
python --version
```
* If Python is installed, the command will display the version of Python installed on your system, such as "Python 3.9.7".

* If the command does not display a Python version, it means Python is not installed or is not in your system's PATH variabl

2. Then install virtual env python library.
```
pip install virtualenv
```

# How to Run
___
1. Create a .env file, and paste your OPENAI api key.
```
OPENAI_API_KEY = "<YOUR_API_KEY>"
```
2. Activate virtual environment. Enter this on the terminal.
```
venv\Scripts\activate
```
3. Run the py file.
```
Python main.py
```
