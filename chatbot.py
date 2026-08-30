def get_bot_response(user_input):
    user_input = user_input.lower().strip()

    if "hello" in user_input or "hi" in user_input:
        return "Hi!"
    elif "how are you" in user_input:
        return "I'm fine, thanks!"
    elif "bye" in user_input:
        return "Goodbye!"
    elif "name" in user_input:
        return "I am a simple rule-based Chatbot."
    else:
        return "Sorry, I don't understand that."


print("--- Basic Chatbot ---")
print("Type 'bye' to exit\n")

while True:
    user_message = input("You: ")
    response = get_bot_response(user_message)
    print(f"Bot: {response}")

    if user_message.lower().strip() == "bye":
        break