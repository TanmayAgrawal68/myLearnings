print("test")
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_ollama import ChatOllama
from dotenv import load_dotenv
import os

load_dotenv()
model_name = os.getenv("MODEL_NAME")
print("using chat model : ", model_name)
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")
model_ollama = ChatOllama(model="gemma3:4b")
# For printing the response at once

# model_response = model.invoke("Write a poem about a lonely computer")

# print(model_response)


# For streaming the response

for chunk in model_ollama.stream("tell me a joke about computers"):
    if chunk.content:
        print(chunk.content, end=" ", flush=True)
