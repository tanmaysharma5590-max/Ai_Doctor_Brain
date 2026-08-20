#1.Setup GROQ API Key
import os
from dotenv import load_dotenv

load_dotenv()
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")


#2.Convert image to required format
import base64
image_path="acne.jpg"
image_file = open(image_path, "rb")
encoded_image = base64.b64encode(image_file.read()).decode("utf-8")

#3.Setup Multimodal LLM
from groq import Groq
client = Groq()
query='Is there something wrong with my skin?'
model='llama-3.2-90b-vision-preview'
messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text", 
                    "text": query
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{encoded_image}",
                    },
                },
            ],
        }]
chat_completion = client.chat.completions.create(
    model=model,
    messages=messages,)
print(chat_completion)