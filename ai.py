import random

# Function to simulate Gemini's response
def gemini_response(question):
    # You can implement your own logic here to generate responses based on the user's question
    responses = [
        "I'm sorry, I don't have the answer to that.",
        "Let me check that for you.",
        "I'm not sure, could you please provide more details?",
        "That's an interesting question. Give me a moment to think.",
        "Unfortunately, I don't have the information you're looking for."
    ]
    return random.choice(responses)

# Main chat loop
while True:
    user_input = input("You: ")
    response = gemini_response(user_input)
    print("Gemini: " + response)