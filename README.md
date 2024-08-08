# About
This program can be described as a combination of two ChatGPT-4 instances, managed with a straightforward control structure.

Typing "quit" will exit the program and save the conversation to a JSON file. Switching between the two bots is easy—just mention that you want a product suggestion. Each time you switch bots, the conversation history will also be saved in a JSON file.

## Ignore the main.ipynb

# How to Run
___
1. Create a virtual environment.
```
python -m venv <environment name>
```
2. Activate Environment.
```
venv/Scripts/venv
```
3. Install Packages.
```
pip install -r requirements.txt
```
4. Create a .env file, and paste your OPENAI api key.
```
OPENAI_API_KEY = "<YOUR_API_KEY>"
```
5. Run the py file.
```
Python main.py
```

# How to run if you received the zip file.
1. Activate the venv
```
venv/Scripts/venv
```
2. Run the .py file
```
python main.py
```