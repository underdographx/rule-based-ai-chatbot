import random

def normalize_text(text):
    return text.lower().strip()

def chatbot_reply(user_text):

    replies = {

        "hello": [
            "Hello there! 👋",
            "Hi! Nice to chat with you.",
            "Hey! How can I assist you today?"
        ],

        "hi": [
            "Hi! 😊",
            "Hello!",
            "Hey there!"
        ],

        "how are you": [
            "I'm doing great today!",
            "Everything is running smoothly.",
            "I'm fine and ready to help!"
        ],

        "what is ai": [
            "Artificial Intelligence is the ability of machines to perform tasks that normally require human intelligence."
        ],

        "what is machine learning": [
            "Machine Learning is a branch of AI that allows computers to learn from data."
        ],

        "what is your name": [
            "I am IntelliBot, your AI assistant."
        ],

        "who made you": [
            "I was developed by Anuja as part of an AI internship project."
        ],

        "help": [
            "You can ask me questions like: hello, what is ai, what is machine learning, how are you, or what is your name."
        ],

        "bye": [
            "Goodbye! 👋 Have an amazing day."
        ],

        "exit": [
            "Closing chatbot session. See you later!"
        ],

        "quit": [
            "Chat ended successfully. Goodbye!"
        ]
    }

    return replies.get(
        user_text,
        ["Sorry, I couldn't understand that. Type 'help' to see available commands."]
    )

def start_chatbot():

    print("=" * 45)
    print("      🤖 INTELLIBOT AI CHATBOT")
    print("=" * 45)
    print("Type 'help' for available commands.")
    print("Type 'bye', 'exit', or 'quit' to end the chat.\n")

    while True:

        user_input = input("You: ")
        clean_text = normalize_text(user_input)

        bot_response = random.choice(chatbot_reply(clean_text))
        print("Bot:", bot_response)

        if clean_text in ["bye", "exit", "quit"]:
            break

start_chatbot()