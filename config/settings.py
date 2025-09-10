import os
from dotenv import load_dotenv

from autogen_ext.models.openai import OpenAIChatCompletionClient
#from autogen_ext.models.ollama import OllamaChatCompletionClient
from config.constant import MODEL

load_dotenv()
api_key = os.getenv('GROQ_API_KEY')

def get_model_client():
    #model_client = OpenAIChatCompletionClient(model=MODEL, api_key=api_key)
    #model_client = OllamaChatCompletionClient(model=MODEL)
    model_client = OpenAIChatCompletionClient(
    base_url="https://console.groq.com/docs/model/llama-3.1-8b-instant",
    model=MODEL,
    api_key = api_key,
    model_info={
        "family":'llama3',
        "vision" :True,
        "function_calling":True,
        "json_output": False,
        "api_type":'Groq',
        "frequency_penalty": 0.5,
        "max_tokens": 2048,
        "presence_penalty": 0.2,
        "seed": 42,
        "temperature": 0.5,
        "top_p": 0.2
    }
)
    return model_client