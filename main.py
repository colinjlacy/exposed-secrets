import os
import requests
import json

URL = "https://api.openai.com/v1/chat/completions"
API_KEY = os.environ.get('OPENAI_API_KEY')

payload = json.dumps({
  "model": "gpt-3.5-turbo",
  "messages": [
    {
      "role": "system",
      "content": "Hello!"
    }
  ]
})
headers = {
  'Content-Type': 'application/json',
  'Authorization': f'Bearer {API_KEY}',
}

response = requests.request("POST", 
                            URL, 
                            headers=headers, 
                            data=payload)

print(response.text)
