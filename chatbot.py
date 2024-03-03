
# Import the necessary libraries
import nltk
from nltk.chat.util import Chat, reflections

reflections = {
  "i am"       : "you are",
  "i was"      : "you were",
  "i"          : "you",
  "i'm"        : "you are",
  "i'd"        : "you would",
  "i've"       : "you have",
  "i'll"       : "you will",
  "my"         : "your",
  "you are"    : "I am",
  "you were"   : "I was",
  "you've"     : "I have",
  "you'll"     : "I will",
  "your"       : "my",
  "yours"      : "mine",
  "you"        : "me",
  "me"         : "you"
}

# Define the predefined responses for the chatbot
pairs = [
    [
        r"hi|hello|hey",
        ["Hello, how can I help you today?",
         "Hi there! What can I do for you?",
         "Hey! What's up?",]
    ],
    [
        r"thank you",
        ["You're welcome!",
         "No problem at all",]
    ],
    [
        r"tell me a joke",
        ["Why couldn't the bicycle stand up by itself? It was two tired!",]
    ],
    [
        r"I need help",
        ["Don't worry, I'm here to save the day. Or at least help with your questions.",]
    ],
    [
        r"how are you ?",
        ["I'm good, thank you. What about you?",]
    ],
    [
        r"where are you from?",
        ["I exist in the digital realm, here to assist you.", "I'm from the world wide web!",]
    ],
    [
        r"do you like music?",
        ["I don't have preferences, but I can play some tunes for you!", "Music is a universal language.",]
    ],
    [
        r"what is your name ?",
        ["You can call me Chatbot.",]
    ],
    [
        r"bye|goodbye",
        ["Goodbye! Have a great day.",
         "Goodbye! See you later.",
         "See you soon!",]
    ],
]

# Create a chatbot using NLTK
def chatbot():
    print("\n\nWelcome! Ask me anything or say bye to exit.\n")
    chat = Chat(pairs, reflections)
    while True:
        user_input = input("You: ")
        response = chat.respond(user_input)
        print("Chatbot:", response)
        if user_input.lower() == "bye":
            break
        print("\n")


# Start interacting with the chatbot
chatbot()
