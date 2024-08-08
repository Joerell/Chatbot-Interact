import json
import threading
import itertools
import time
from datetime import datetime
from openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv()

# Your OpenAI API key
bot1 = OpenAI(
    api_key=os.getenv('OPENAI_API_KEY')
)

customer_service_bot_system_prompt = {
    "role": "system", "content":
    """
    You are a helpful customer service bot that will help the customer with product information, pricing, and availability.
    
    But when the customer asks or mentions about product suggestions, 
     
    I want you to reply with "For more helpful product suggestions I will transfer you to Sales Bot"
    """
}

sales_bot_system_prompt = {
    "role": "system", "content":
    """
    You are a helpful sales bot that will help the customer with product suggestions
    """
}

# Initialize conversation history
conversation_history = []

# Spinner function that runs in a separate thread
def spinner():
    for char in itertools.cycle('|/-\\'):
        if not spin_flag:
            break
        print(f'\rProcessing {char}', end='', flush=True)
        time.sleep(0.1)
    print('\r', end='', flush=True)  # Clear the line when done


# Function to get a response from the ChatGPT API
def chatbot(messages):
    response = bot1.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        max_tokens=150
    )
    return response.choices[0].message.content


def date_and_time_gmt():
    now = datetime.utcnow()  # Get current time in GMT
    return now.strftime("conversation_%Y-%m-%d_%H-%M-%S.json")

# Function to save conversation history to a JSON file with a dynamic name
def save_conversation_to_json():
    file_name = date_and_time_gmt()
    with open(file_name, 'w') as file:
        json.dump(conversation_history, file, indent=4)

# Main chat loop
def chat(customer_service_or_sales: bool):
    if customer_service_or_sales:
        bot_system_prompt = customer_service_bot_system_prompt
        bot_type = "Customer Service Bot"
    else:
        bot_system_prompt = sales_bot_system_prompt
        bot_type = "Sales Bot"

    # Set the appropriate system prompt in the conversation history
    if conversation_history:
        conversation_history[0] = bot_system_prompt
    else:
        conversation_history.append(bot_system_prompt)

    greetings = f"Hi! How can I help you today?"
    print(f"{bot_type}: {greetings}")
    conversation_history.append({"role": "assistant", "content": greetings})


    while True:
        user_input = input("You: ")

        # Add user's message to conversation history
        conversation_history.append({"role": "user", "content": user_input})
        # print(f"You: {user_input}")

        # Start the spinner in a separate thread
        global spin_flag
        spin_flag = True
        spinner_thread = threading.Thread(target=spinner)
        spinner_thread.start()

        # Get response from ChatGPT
        response = chatbot(conversation_history)
        
        # Stop the spinner once the response is ready
        spin_flag = False
        spinner_thread.join()

        # Add the chatbot's response to conversation history
        conversation_history.append({"role": "assistant", "content": response})

        print(f"{bot_type}: {response}")

        if user_input.lower() in ['exit', 'quit', 'bye']:
            save_conversation_to_json()
            print("Chatbot: Goodbye!")
            break
        elif "transfer you to Sales Bot" in response:
            print("Transferring to Sales Bot...")
            save_conversation_to_json()
            chat(customer_service_or_sales=False)
            break
        elif "transfer you to Customer Service Bot" in response:
            print("Transferring to Customer Service Bot...")
            save_conversation_to_json()
            chat(customer_service_or_sales=True)
            break

if __name__ == "__main__":
    chat(customer_service_or_sales=True)

