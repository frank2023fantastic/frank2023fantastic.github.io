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

# from geminipy import Geminipy

# # Create an instance of the GeminiAPI class
# api = Geminipy(api_key="AIzaSyAumXjD6LYcx069aOpXtpjikgJqnqadQp4")


# # Define a function to handle user questions
# def answer_question(question):
#     if question == "balances":
#         # Get account balances
#         balances = api.get_balances()
#         return str(balances)
#     elif question == "orders":
#         # Get open orders
#         orders = api.get_active_orders()
#         return str(orders)
#     else:
#         return "I'm sorry, I don't have an answer for that question."


# # Main program loop
# while True:
#     user_input = input("Enter your question (or 'exit' to quit): ")

#     if user_input.lower() == "exit":
#         break

#     answer = answer_question(user_input)
#     print("Answer: " + answer)

# import requests

# # Replace with your Gemini API credentials
# API_KEY = AIzaSyAumXjD6LYcx069aOpXtpjikgJqnqadQp4
# API_SECRET = 'your-api-secret'

# # Replace with the question you want to ask Gemini
# question = 'What is the current price of Bitcoin?'

# # Gemini API endpoint
# endpoint = 'https://api.gemini.com/v1/order/new'

# # Create the request headers with API key and secret
# payload = {
#     'request': '/v1/order/new',
#     'nonce': str(int(time.time() * 1000)),
# }

# # Generate the signature using the API secret
# payload_encoded = base64.urlsafe_b64encode(json.dumps(payload).encode('utf-8'))
# signature = hmac.new(API_SECRET.encode('utf-8'), payload_encoded, hashlib.sha384).hexdigest()

# headers = {
#     'Content-Type': 'text/plain',
#     'Content-Length': '0',
#     'X-GEMINI-APIKEY': API_KEY,
#     'X-GEMINI-PAYLOAD': payload_encoded,
#     'X-GEMINI-SIGNATURE': signature
# }

# # Send the request
# response = requests.post(endpoint, headers=headers)

# # Print the response
# print(response.text)

import google.generativeai as genai

genai.configure(api_key= 'AIzaSyAumXjD6LYcx069aOpXtpjikgJqnqadQp4' )

# Set up the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 0,
  "max_output_tokens": 8192,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

convo = model.start_chat(history=[
])

convo.send_message("hello")
print(convo.last.text)