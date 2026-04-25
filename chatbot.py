def chatbot_reply(message):

    message = message.lower()

    if "steganography" in message:
        return "Steganography hides secret messages inside images."

    elif "detect" in message:
        return "The AI analyzes image patterns to detect hidden data."

    else:
        return "Ask me about steganography detection."