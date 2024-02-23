from flask import Flask, request, jsonify, render_template
from openai_caller import openai_generator

app = Flask(__name__)
conversation_history = [
    {"role": "system", "content": "You are the Dungeon Master in a fantasy world."}
]

@app.route('/send_message', methods=['POST'])
def send_message():
    global llm, conversation_history
    user_message = request.json.get('message')
    #print(user_message)
    response, conversation_history = openai_generator(user_message, conversation_history)
    #user_messages.append(user_message)
    #response = f'{user_message}'
    #response = langchain2.query(user_message, llm=llm)
    return jsonify({'message': response})

@app.route('/get_messages', methods=['GET'])
def get_messages():
    return jsonify({'messages': user_messages})

@app.route('/')
def chat():
    global user_messages
    user_messages = []
    logo_url = 'static/logo.jpg'
    return render_template('index.html', logo_url=logo_url)
if __name__ == '__main__':
    #pipeline = langchain2.make_model()
    #llm = langchain2.run_model(pipeline=pipeline)
    app.run(debug=True, port=4040)
