from gpt_index import GPTSimpleVectorIndex, LLMPredictor, PromptHelper
import sys
import os
from dotenv import load_dotenv
from flask import Flask, request, jsonify, make_response

app = Flask(__name__)

Api_key = os.environ.get("OPENAI_API_KEY")

def chat_bot_gen(input_text):
    index = GPTSimpleVectorIndex.load_from_disk("index.json")
    response = index.query(input_text, response_mode="compact")
    return response.response

def chat_bot_client(input_text):
    index = GPTSimpleVectorIndex.load_from_disk("index_client.json")
    response = index.query(input_text, response_mode="compact")
    return response.response

app = Flask(__name__)


@app.route('/', methods=['GET'])
def welcome():
    return '¡Hola! Soy el asistente virtual de solsiete. ¿En qué puedo ayudarte hoy?'

@app.route('/chat', methods=['GET'])
def chatbot_gen():
    
    try:
        question = request.args.get('question')
        if question:
            response = chat_bot_gen(question)

            # Create a response object with plain text content
            response_text = make_response(response)
            response_text.headers['Content-Type'] = 'text/plain'
            
            return response_text
        else:
            return "Lo siento, no he entendido la pregunta."
    except Exception as e:
        return f"Error: {str(e)}"
    
@app.route('/chat_client', methods=['GET'])
def chatbot_client():
    try:
        question = request.args.get('question')
        if question:
            response = chat_bot_client(question)

            # Create a response object with plain text content
            response_text = make_response(response)
            response_text.headers['Content-Type'] = 'text/plain'
            
            return response_text
        else:
            return "Lo siento, no he entendido la pregunta."
    except Exception as e:
        return f"Error: {str(e)}"    
    
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=False),
    

 