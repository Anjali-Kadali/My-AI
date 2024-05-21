import json
import requests
import openai

headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiY2U2YzAxNjktNTY3ZS00NzFjLTg1ZjctMzBjZjE2NzY3MDZiIiwidHlwZSI6ImFwaV90b2tlbiJ9.__qNaVZd1yMZQd904DEnf9_39nJ30nyHbeXc6vRAkRU"}

url = "https://api.edenai.run/v2/text/chat"
payload = {
    "providers": "openai",
    "text": "Tell me my name",
    "chatbot_global_action": "Act as an assistant",
    "previous_history": [],
    "temperature": 0.0,
    "max_tokens": 150,
    "fallback_providers": "Anjali"
}


def take(query):
    payload["text"]=query
    #print(payload)
    response = requests.post(url, json=payload, headers=headers)
    #print(response.text)
    result=json.loads(response.text)
    print(result['openai']['generated_text'])
take("How are you....")
    
    