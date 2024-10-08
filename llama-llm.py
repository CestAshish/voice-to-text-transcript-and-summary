import os
import requests
def llm_llama(prompt):
    # Retrieve the Groq API key from environment variables
    groq_api_key = os.getenv('GROQ_API_KEY')

    # API endpoint for Groq (Replace with the correct endpoint if different)
    url = "https://api.groq.com/openai/v1/chat/completions"

    # Request payload
    payload = {
        "model": "llama3-8b-8192",  # Replace with your model ID
        "messages": [  # Use 'messages' instead of 'message'
            {
                "role": "user",
                "content": f"List the key points with details from the context: {prompt}"
            }
        ],
        "max_tokens": 800,
        "temperature": 0.1
    }

    # Headers for the request
    headers = {
        "Authorization": f"Bearer {groq_api_key}",
        "Content-Type": "application/json"
    }

    # Make the API request
    response = requests.post(url, json=payload, headers=headers)

    # Check for a successful response
    if response.status_code == 200:
        result = response.json()
        # Adjust based on the response structure; assuming 'choices' is present
        choices = result.get('choices', [])
        if choices:
            return choices[0].get('message', {}).get('content', 'No content in response')
        else:
            return 'No choices in response'
    else:
        return f"Error: {response.status_code} - {response.text}"


