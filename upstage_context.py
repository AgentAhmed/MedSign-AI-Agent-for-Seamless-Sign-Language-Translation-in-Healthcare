from openai import OpenAI
from llama_index.llms.upstage import Upstage
from llama_index.core.llms import ChatMessage
import requests

class MedicalContextualizer:
    def __init__(self, api_key):
        self.api_key = api_key
        self.endpoint = "https://api.upstage.ai/v1/solar"  

    def query_upstage(self, text):
        headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }
        data = {
            "text": text,
            "domain": "medical"
        }
        response = requests.post(self.endpoint, json=data, headers=headers)
        if response.status_code == 200:
            return response.json().get('translated_text', text)
        else:
            print(f"Error: {response.status_code} - {response.text}")
            return text

def get_upstage_response(api_key, user_input):
    # Using Upstage API directly
    contextualizer = MedicalContextualizer(api_key)
    return contextualizer.query_upstage(user_input)

def get_llama_index_response(api_key, user_input):
    # Using LlamaIndex
    llm = Upstage(api_key=api_key)
    response = llm.chat(messages=[
        ChatMessage(role="system", content="You are a helpful assistant."),
        ChatMessage(role="user", content=user_input)
    ])
    return response

# Example usage
api_key = "up_VcBniTeOjMk76acpRAqHUMyrvh9tK"  
user_input = "Patient has a severe headache."

# Get response from Upstage API
contextual_response = get_upstage_response(api_key, user_input)
print("Contextualized Response:", contextual_response)

# Get response from LlamaIndex
llama_response = get_llama_index_response(api_key, user_input)
print("LlamaIndex Response:", llama_response)
