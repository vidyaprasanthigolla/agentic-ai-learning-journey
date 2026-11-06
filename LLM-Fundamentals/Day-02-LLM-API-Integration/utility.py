from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Read API credentials
api_key = os.getenv("OPENROUTER_API_KEY")
model_name = os.getenv("OPENROUTER_MODEL")

if not api_key:
    raise ValueError("OPENROUTER_API_KEY is missing")

if not model_name:
    raise ValueError("OPENROUTER_MODEL is missing")

from langchain_openai import ChatOpenAI

# Configure LLM
def get_open_router():
    llm = ChatOpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
        model=model_name,
        temperature=0
    )
    return llm