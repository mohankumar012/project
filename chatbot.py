import random

def get_response(user_input):
    responses = {
        "hi": "Hello! How can I help you?",
        "how are you": "I'm good, thank you. How about you?",
        "bye": "Goodbye! Have a great day.",
        "default": "I'm not sure how to respond to that."
    }

    user_input = user_input.lower()

    if user_input in responses:
        return responses[user_input]
    else:
        return responses["default"]

print("Welcome to Python Conversations Chatbot!")
print("You can start chatting with me. Type 'bye' to exit.")

while True:
    user_input = input("You: ")
    response = get_response(user_input)
    print("Chatbot:", response)

    if user_input.lower() == "bye":
        break