# import random

# # Function to simulate Gemini's response
# def gemini_response(question):
#     # You can implement your own logic here to generate responses based on the user's question
#     responses = [
#         "I'm sorry, I don't have the answer to that.",
#         "Let me check that for you.",
#         "I'm not sure, could you please provide more details?",
#         "That's an interesting question. Give me a moment to think.",
#         "Unfortunately, I don't have the information you're looking for."
#     ]
#     return random.choice(responses)

# # Main chat loop
# while True:
#     user_input = input("You: ")
#     response = gemini_response(user_input)
#     print("Gemini: " + response)

from geminipy import Geminipy
# Create an instance of the GeminiAPI class
api = Geminipy(api_key='', api_secret='')
# Define a function to handle user questions
def answer_question(question):
    if question == "balances":
        # Get account balances
        balances = api.get_balances()
        return str(balances)
    elif question == "orders":
        # Get open orders
        orders = api.get_active_orders()
        return str(orders)
    else:
        return "I'm sorry, I don't have an answer for that question."

# Main program loop
while True:
    user_input = input("Enter your question (or 'exit' to quit): ")
    
    if user_input.lower() == "exit":
        break
    
    answer = answer_question(user_input)
    print("Answer: " + answer)