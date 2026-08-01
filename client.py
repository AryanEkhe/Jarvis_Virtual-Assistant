import os 
from dotenv import load_dotenv
from google import genai
from google.genai import types

#load the environment variables from .env 
load_dotenv()

#Pass the loaded environment variables to client
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents="What is coding?",
    config=types.GenerateContentConfig(
        system_instruction="You are a virtual assistant named Jarvis skilled in general tasks like Alexa and Google Assistant."
    )
)

print(response.text)