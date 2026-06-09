import os
from google import genai

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

response = client.models.generate_content(
    model="gemini-2.5-flash-lite",
    contents="Explain Law VS Justice to a 5 year old in 5 sentences."
)

print(response.text)
