
from transformers import pipeline, Conversation

# Load the conversational model pipeline only once (saves time on each API call)
chatbot = pipeline("conversational")

def get_bot_response(user_input):
    """
    Takes user input (a string), creates a conversation object,
    passes it to the model, and returns the last response.
    """
    conversation = Conversation(user_input) #Creates an object that stores the user's message
    response = chatbot(conversation)
    return response.generated_responses[-1]
