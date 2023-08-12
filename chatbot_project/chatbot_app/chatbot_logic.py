def get_bot_response(user_message):
    responses = {
        "hello": "Hi there!",
        "how are you": "I'm just a bot, but I'm doing fine. How can I assist you?",
        "bye": "Goodbye! If you have more questions, just ask.",
    }

    # Convert user message to lowercase and remove any punctuation
    user_message = user_message.lower().strip()

     # Get the response from the dictionary, if it exists
    return responses.get(user_message, "I'm sorry, I didn't understand that.")

