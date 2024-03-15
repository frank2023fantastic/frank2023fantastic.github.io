from flask import Flask, render_template, request
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/save_conversation', methods=['POST'])
def save_conversation():
    conversation = request.form.get('conversation')
    save_chat_to_markdown(conversation)
    return 'Conversation saved successfully.'

def save_chat_to_markdown(conversation):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    filename = f"conversation_{timestamp}.md"

    with open(filename, "w") as file:
        file.write("# Conversation\n\n")
        file.write(conversation)

    print(f"Conversation saved to {filename}")

if __name__ == '__main__':
    app.run()